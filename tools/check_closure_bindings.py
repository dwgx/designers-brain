#!/usr/bin/env python3
"""Check current public closure bindings without rerendering or rewriting evidence."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, sys

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent)
    ap.add_argument('--report',type=Path)
    args=ap.parse_args();root=args.root.resolve();errors=[];groups={}
    def read(rel):return json.loads((root/rel).read_text('utf-8'))
    def check(group,rel,expected,size=None):
        groups[group]=groups.get(group,0)+1
        pp=PurePosixPath(rel)
        if pp.is_absolute() or '..' in pp.parts or '\\' in rel:
            errors.append({'group':group,'path':rel,'reason':'unsafe path'});return
        p=root.joinpath(*pp.parts)
        if not p.is_file():errors.append({'group':group,'path':rel,'reason':'missing'});return
        data=p.read_bytes()
        if hashlib.sha256(data).hexdigest()!=expected:errors.append({'group':group,'path':rel,'reason':'SHA mismatch'})
        if size is not None and len(data)!=size:errors.append({'group':group,'path':rel,'reason':'byte length mismatch'})
    seen={}
    for row in read('docs/audit/current19/CURRENT-DELIVERY-MAPPING.json')['rows']:
        for kind in row['current_kind_mapping']:
            for item in kind.get('current_artifacts',[]):
                rel=item['repo_relative_path'];obs=item['observed_final']
                if rel in seen and seen[rel]!=obs['sha256']:errors.append({'group':'current19','path':rel,'reason':'conflicting binding'})
                seen[rel]=obs['sha256']
    for rel,h in seen.items():check('current19',rel,h)
    for row in read('docs/audit/corpus/PATCH-MANIFEST.json')['files']:check('corpus-delivery',row['path'],row['after_sha256'],row['after_bytes'])
    for row in read('docs/audit/corpus/PATCH-MANIFEST.json')['source_guards']:check('corpus-source',row['path'],row['sha256'],row['bytes'])
    for handle,seed in read('experiments/designer_seeds/PACKAGE-MANIFEST.json')['seeds'].items():
        base=PurePosixPath('experiments/designer_seeds')/handle/seed['path_base']
        for row in seed['files']:check('seed-package',str(base/row['path']),row['packaged_sha256'],row.get('bytes_packaged'))
    for row in read('docs/audit/closure-20261118/runtime/PROJECTION-MANIFEST.json')['files']:check('runtime-projection',row['public_path'],row['public_sha256'],row['public_bytes'])
    for row in read('experiments/consumer_skill/C1-closure/PUBLIC-PROJECTION.json')['files']:check('C1-public-projection','experiments/consumer_skill/C1-closure/'+row['public_path'],row['public_sha256'])
    for line in (root/'experiments/consumer_skill/SHA256SUMS.txt').read_text('utf-8').splitlines():
        if not line.strip() or line.startswith('#'):continue
        h,rel=line.split(maxsplit=1);check('historical-consumer','experiments/consumer_skill/'+rel.lstrip('*'),h)
    for row in read('experiments/consumer_skill/HISTORICAL32-PROJECTION.json')['rows']:
        rel='experiments/consumer_skill/'+row['path'].removeprefix('./')
        check('historical-consumer-projection',rel,row['root_working_sha256'])
        data=(root/rel).read_bytes()
        reconstructed=data.replace(b'\n',b'\r\n') if row['normalization']=='CRLF_to_LF_only' else data
        if hashlib.sha256(reconstructed).hexdigest()!=row['source_recorded_sha256']:
            errors.append({'group':'historical-consumer-projection','path':rel,'reason':'original digest reconstruction mismatch'})
    preservation=read('docs/audit/closure-20261118/PRESERVATION.json')
    cm=preservation['central_manifest']
    check('preserved-central-manifest',cm['path'],cm['raw_sha256']['e0'],cm['bytes']['e0'])
    assets=root/'knowledge/domains/painters/dossiers/_images'
    jpgs=sorted(assets.rglob('*.jpg'))
    ledger=''.join(p.relative_to(root).as_posix()+'\t'+hashlib.sha256(p.read_bytes()).hexdigest()+'\n' for p in jpgs)
    groups['preserved-images']=len(jpgs)
    if len(jpgs)!=739 or hashlib.sha256(ledger.encode()).hexdigest()!=preservation['images']['tree_sha256']['e0']:
        errors.append({'group':'preserved-images','reason':'image inventory or byte ledger mismatch'})
    for card,row in preservation['old5_motion'].items():
        check('preserved-motion','experiments/motion_closure/media/MOTION-'+card+'.mp4',row['e0_sha256'])
    manifest=root/'docs/audit/closure-20261118/DELIVERY-SHA256SUMS.txt'
    if manifest.exists():
        for line in manifest.read_text('utf-8').splitlines():
            if not line.strip() or line.startswith('#'):continue
            h,rel=line.split(maxsplit=1);check('closure-delivery',rel.lstrip('*'),h)
    else:errors.append({'group':'closure-delivery','reason':'delivery manifest absent'})
    result={'schema':'closure-binding-check@1','ok':not errors,'groups':groups,'errors':errors,'scope':'Current public bytes only. Historical claim/original-source hashes and human or learning outcomes are not upgraded. Motion full decode is a separate gate.'}
    out=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if args.report:args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_bytes(out.encode())
    print(out,end='');return 0 if not errors else 1

if __name__=='__main__':
    if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
    raise SystemExit(main())
