from pathlib import Path
import json, hashlib, datetime, xml.etree.ElementTree as ET
import numpy as np
from PIL import Image

B=Path(__file__).resolve().parent
plan=json.loads((B/'measurement-plan.json').read_bytes())
assert hashlib.sha256(Path(__file__).read_bytes()).hexdigest()==plan['checker_sha256']
seal=json.loads((B/'PRE-HOLDOUT-SEAL.json').read_bytes())
for row in seal['locked_files']:
    b=(B/row['path']).read_bytes()
    assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256'], 'premeasurement locked-file drift'

def inspect(label,svg_path,png_path,configuration):
    root=ET.fromstring(svg_path.read_bytes())
    fill_values=sorted({e.attrib['fill'] for e in root.iter() if e.attrib.get('fill') not in (None,'none')})
    strokes=[e.attrib.get('id','unnamed') for e in root.iter() if e.attrib.get('stroke') not in (None,'none')]
    rgb=np.array(Image.open(png_path).convert('RGB'))
    assert rgb.shape==(640,960,3)
    assert np.all(rgb[:,:,0]==rgb[:,:,1]) and np.all(rgb[:,:,1]==rgb[:,:,2])
    raw=rgb[:,:,0].astype(np.int16)
    palette=np.array(plan['rgb_grey_values'],dtype=np.int16)
    quant=palette[np.abs(raw[:,:,None]-palette).argmin(axis=2)]
    counts={str(int(v)):int(np.sum(quant==v)) for v in palette}
    x0,y0,x1,y1=configuration['focus_roi_xyxy']
    roi=quant[y0:y1,x0:x1]
    fracs={str(int(v)):float(np.mean(roi==v)) for v in palette}
    errors=[]
    if fill_values!=plan['svg_fill_values']:errors.append('SVG_FILL_SET_MISMATCH')
    if strokes:errors.append('UNEXPECTED_OUTLINE_STROKE')
    if fracs['64']<plan['focus_min_fraction_each_extreme']:errors.append('FOCUS_DARK_MASS_MISSING')
    if fracs['208']<plan['focus_min_fraction_each_extreme']:errors.append('FOCUS_LIGHT_MASS_MISSING')
    span=int(roi.max()-roi.min())
    if span<plan['focus_min_rgb_span']:errors.append('FOCUS_VALUE_SPAN_TOO_SMALL')
    edge_rows=[]
    for edge in configuration['lost_edge_samples']:
        y=edge['y'];x0=edge['x_start'];x1=edge['x_end_inclusive']
        sample=quant[y,x0:x1+1]
        jump=int(np.abs(np.diff(sample)).max(initial=0))
        code='LOST_EDGE_'+edge['id']+'_ADJACENCY_BROKEN'
        if jump>plan['lost_edge_max_adjacent_step']:errors.append(code)
        edge_rows.append({'id':edge['id'],'pixel_row':y,'x_range_inclusive':[x0,x1],'quantized_grey_values':sample.tolist(),'max_adjacent_rgb_step':jump,'allowed_step':plan['lost_edge_max_adjacent_step'],'error_code':code if code in errors else None})
    return {'label':label,'png_size':[960,640],'source_svg_fill_values':fill_values,'source_svg_stroke_nodes':strokes,'source_svg_node_count':sum(1 for _ in root.iter()),'png_unique_greys':int(len(np.unique(raw))),'png_anti_aliasing_extra_greys':int(len(set(np.unique(raw).tolist())-set(palette.tolist()))),'nearest_grey_area_pixels':counts,'nearest_grey_area_fraction':{k:v/(960*640) for k,v in counts.items()},'focus_roi_xyxy':configuration['focus_roi_xyxy'],'focus_grey_fractions':fracs,'focus_rgb_span':span,'lost_edge_samples':edge_rows,'specific_errors':errors,'local_checks_pass':not errors}

cases=[inspect('A',B.parent/'A/02-three-value-sketch.svg',B/'A-render.png',plan['compositions']['A']),inspect('B',B/'second-topic.svg',B/'B-render.png',plan['compositions']['B']),inspect('A_bad_outline',B/'bad-outline.svg',B/'bad-outline.png',plan['compositions']['A'])]
bad=cases[2]
rejected='LOST_EDGE_A_E1_ADJACENCY_BROKEN' in bad['specific_errors']
result={'measured_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checker_sha256':plan['checker_sha256'],'plan_sha256':hashlib.sha256((B/'measurement-plan.json').read_bytes()).hexdigest(),'cases':cases,'bad_example_expected_rejection':{'required_error':'LOST_EDGE_A_E1_ADJACENCY_BROKEN','observed':rejected,'actual_errors':bad['specific_errors']},'scope':'Only frozen local composition checks. RGB is not CIELAB L; mechanical local checks are not visual attention, sfumato, aesthetics, or learning validation.'}
with (B/'measurement-results.json').open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False,indent=2))
