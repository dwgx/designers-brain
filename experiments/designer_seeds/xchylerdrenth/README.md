# xchylerdrenth — local research prototype

**E1 seed; researcher-authored operationalisation.** This is not a validated reproduction of the named designer, an E2/E3 result, or human aesthetic evidence.

A fixed 8-node / 10-edge diagram with bounded projection, decoration and occlusion controls.

## Run

Requires Python 3 and Pillow. From this directory:

```sh
python -B prototype/build.py fresh-output
```

The relative output directory is resolved under `prototype/`; pass an absolute temporary directory to leave the checkout unchanged. A nonzero exit means the bounded positive/negative checks did not all meet their recorded conditions. `prototype/outputs/` contains an actual fresh run. No network, API key, model, designer media or global skill installation is needed.

## Evidence and scope

`ORIGIN.json` binds original local source/config and historical receipt identities. Historical hashes do not constitute current acceptance or public availability of the archived private records. `FRESH-RUN.json` binds the current packaged source and generated files. Images are project-created geometry, not copied author/client artwork.

The checks cover the implemented fixture only. They do not establish the designer's algorithm, causal design principles, reader comprehension, generalisation or aesthetic quality. Human judgments remain pending. Local generation is separate from corpus/domain promotion.

The current checker additionally verifies serialized M/L path endpoints against serialized node centers; a label-preserving disconnected-line mutation is rejected. `GEOMETRY-CHECK.patch` records the narrow change from historical code. This is not a general SVG validator.
