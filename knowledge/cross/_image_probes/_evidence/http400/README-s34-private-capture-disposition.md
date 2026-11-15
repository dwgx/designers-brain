# Historical HTTP 400 capture disposition

This is a provenance summary of the existing HTTP 400 investigation, not a new API run.
Four request snapshots were removed from the public candidate because their message/tool context was private.
Root must preserve the exact original bytes outside the candidate before removal. Original source/archive/history is unchanged.
Authorization was already redacted in the inspected snapshots; this does not claim four plaintext keys were found.

| Historical capture | Original SHA-256 | Bytes | Message entries | Tool schemas | Streaming |
| --- | --- | ---: | ---: | ---: | --- |
| p1b_no_tools_400.json | 84c49750f9e908cdede22a145eb8045d816677803322cce1176578be20940af3 | 87797 | 2 | 47 | true |
| p2_grok-imagine-image-2.0_400.json | aebc161e855948fd6870329533266c579c270b9a9e468efed8d715fbeb06c82d | 56407 | 2 | 11 | true |
| p3_grok-imagine-image-edit_400.json | 2b27e3b2805fdcfa450710bf401aeaafc5c6803fdfd3b1f15f3d6d3a5be34e7d | 56529 | 2 | 11 | true |
| p4_grok-imagine-image-lite_400.json | 53011d4f96de8615d1b9f7d965bdd4c19a9a67c98a41dd01e1e8f36c95c158ab | 56411 | 2 | 11 | true |

The request containers included model/messages/stream/tool-schema fields. Counts describe the captured request only.
The filename `p1b_no_tools` is historical; its inspected request actually contains 47 tool schemas.
The other three inspected captures each contain 11 tool schemas. Do not infer the cause of HTTP 400 from a filename.
No message text, tool definitions, header values, private endpoint or personal locator is reproduced here.
Public historical context and limits remain in [the earlier minimal record](README-minimal-400-repro.md) and
[the image channel record](../../../image_channel.md). A source hash proves bytes, not a new response or causal diagnosis.
There was no new HTTP/model call for this disposition.
