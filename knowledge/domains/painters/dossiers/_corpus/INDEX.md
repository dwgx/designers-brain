# 原话语料 INDEX（A-10）

> 8 位画家（wave1），共 **126 条引文**（每文件 ≥10；逐条带来源行 + 类型标注）。
> **wave12 追加**：克里姆特（klimt）1 文件 11 条（2026-10-15，ArtistKlimt / A-22）→ **合计 9 文件 137 条**。
> **wave13 追加**：修拉（seurat）1 文件 19 条（2026-10-15，ArtistSeurat / A-24）→ **合计 10 文件 156 条**。
> **wave14 加固**（2026-10-15）：8 位核心语料扩容（126→200；+74）；caravaggio / vermeer / durer 语料补建（22 / 22 / 27 条）。
> **wave16 收口合并**（2026-10-16，IndexMerge / A-51）：并入 wave12/13 新档 7 文件（turner / rembrandt / goya / hopper / bada_shanren / qi_baishi / ito_jakuchu，154 条）→ **合计 20 文件 455 条**（20 位画家）。
> **wave15/17 并入**（2026-10-16，IndexMerge2）：并入 wave15×8 + wave17×7 共 15 文件（mucha / munch / kandinsky / velazquez / bosch / huang_gongwang / kahlo / behzad / friedrich / repin / ravi_varma / degas / gauguin / van_eyck / kngwarreye，389 条）→ **合计 35 文件 844 条**（35 位画家）。
> **wave18/19/20 并入**（2026-10-16，IndexMerge3）：并入 wave18×7 + wave19×10 + wave20×10 共 27 文件（hiroshige / sargent / piero_della_francesca / artemisia_gentileschi / namatjira / el_salahi / wu_guanzhong / fan_kuan / sesshu / constable / poussin / bruegel / el_greco / holbein / aivazovsky / okeeffe / rivera / zhao_mengfu / ni_zan / qiu_ying / ogata_korin / blake / chardin / manet / sorolla / zorn / sultan_mohammed，769 条）→ **合计 62 文件 1613 条**（62 位画家）。
> **wave21 并入**（2026-10-16，IndexMerge4）：并入 wave21×10 共 10 文件（xu_beihong / li_keran / sher_gil / tarsila / chen_hongshou / xu_wei / hogarth / mir_sayyid_ali / de_chirico / rockwell，321 条）→ **合计 72 文件 1934 条**（72 位画家）。
> 底本：Trattato 全 8 部、Rime/Varchi/Condivi、vangoghletters 13 封原文信、Perry 1927、Geffroy 1922、Clemenceau 1928、Gasquet/Bernard、Wikiquote fr/en/ja 转录；**wave15/17 批摘**：eMunch（munch）·《论艺术中的精神》德/英双底本 +《点线面》（kandinsky）· Noa Noa / Avant et Après（gauguin）· ru.wikisource（repin）· Pacheco / Palomino（velazquez）·《辍耕录》维基文库（huang_gongwang）· Mucha Foundation（mucha）；**wave18/19/20 批摘**：Charteris 1927（sargent）·《De prospectiva pingendi》（piero）· 庭审记录/书信（artemisia）·《宋朝名画评》四库本（fan_kuan）· Jouanny 1911（poussin）· Erdman 1988（blake）· Jansson 2022（zorn）；**wave21 批摘**：讲演辞/年谱（xu_beihong）· 基金会语录（li_keran）· 书信转引级（sher_gil）· 信影印（tarsila）·《陈老莲别传》（chen_hongshou）· 馆藏题跋（xu_wei）·《美的分析》（hogarth）· Seyller/Welch OCR（mir_sayyid_ali）· 基金会 Scritti（de_chirico）· New Yorker 1945（rockwell）；各文件底本另见文件头。
> 标注计数为**出现次数**（含正文提及），非条目数；条目数 = `grep -c '^### '`。

| 文件 | 条目 | self-written | reported speech | contemporary record | 备注 |
|---|---|---|---|---|---|
| da_vinci.md | 22 | 20 | 1 | 4 | Trattato 全 8 部逐字；wave14 追生平档案 6 条；Codex 未收（已声明） |
| michelangelo.md | 22 | 17 | 2 | 6 | Rime 6 首 + Varchi 信 + Condivi；wave14 追 7 条；「色彩与光」仅 3 条（材料本就稀少） |
| van_gogh.md | 36 | 38 | 1 | 1 | 原文书信（法/荷；含提奥 3 封）；全集 903 封未穷尽 |
| monet.md | 29 | 17 | 12 | 3 | Perry/Geffroy/Clemenceau 转录 + wave14 书信追加；页码 ±1 风险已标 |
| picasso.md | 24 | 2 | 23 | 1 | 多为转述（Brassaï/Gilot/Malraux，带页码）；亚型另计：[reported speech·memoir] 3 / ·press 2 |
| cezanne.md | 24 | 11 | 12 | 5 | Gasquet 对话为文学重建（已标注）；«cylindre» 信逐字核过；wave14 追左拉通信 7 条 |
| matisse.md | 24 | 16 | 7 | 4 | 法文原刊不可得处用英译并标注；wave14 追 11 条（生平/剪纸等） |
| hokusai.md | 19 | 8 | 3 | 11 | 1834 序等；wave14 追 7 条（出版广告/晚年记录）；「色彩与光」仅 1 条（彩色通跋文） |
| klimt.md | 11 | 7 | 3 | 5 | 致 Flöge 书信/明信片（馆方英译）；Belvedere/Leopold 档案转引；Loos 误挂已剔 |
| seurat.md | 19 | 14 | 4 | 4 | 法文仅收 Met 1991 目录已印段；英译逐条标注；OCR 校正已声明 |
| caravaggio.md | 22 | 3 | 4 | 20 | 自述类目为空（史实性空缺，非采集缺口）；档案证词/同代记述为主体；2007 受洗档案新见已收 |
| vermeer.md | 22 | 2 | 1 | 22 | 结构性无自述（0 条为事实）；Montias 文书 + 遗产清单；荷/法原文照录、英译逐条标注 |
| durer.md | 27 | 22 | 1 | 7 | Familienchronik / 威尼斯书信 / 尼德兰日记逐字（德英双轨）；Fraktur OCR 校正已声明 |
| turner.md | 19 | 5 | 12 | 6 | Thornbury / Hamerton / Ruskin 底本；OCR 规范化；「绑桅四小时」记录链双说并存 |
| rembrandt.md | 17 | 12 | 3 | 6 | Huygens 往来七封信（Worp 1913 排印）；荷语拼写原样；Worp/Strauss 差异逐条注 |
| goya.md | 22 | 19 | 4 | 3 | 书信/报告/公告/题刻；西语原信未全量回查（逐条标注）；「三导师」语已降级 [reported speech] |
| hopper.md | 25 | 9 | 9 | 3 | 含 [self-spoken] 12 条（口述史，另列）；AAA 转录 +《Notes on Painting》全文；书刊转引给页码 |
| bada_shanren.md | 22 | 9 | 3 | 10 | 题跋/尺牍/传记三源（逐字直读）；[later reception] 4 条另列；「墨点无多泪点多」已降级 |
| qi_baishi.md | 25 | 22 | 3 | 3 | 画语/题跋（汇编出处未直读，已标注）；异文记录；[later reception] 1 条另列 |
| ito_jakuchu.md | 24 | 7 | 1 | 11 | 款記/印文/寄進状；[research] 14 条另列（色彩科学调查）；纸书未直读（已声明） |
| mucha.md | 25 | 6 | 18 | 4 | Mucha Foundation / GAC / 传记载体转引；讲座遗稿《Lectures on Art》；捷克语 4 条原始出处未回查（单列标注） |
| munch.md | 29 | 27 | 1 | 4 | eMunch 数字档案（英译 Nichols）；挪威语原文逐字（保留原始拼写与编辑标记 `{}`/`‹›`）；只取创作/视觉语言相关 |
| kandinsky.md | 29 | 30 | 1 | 1 | 《论艺术中的精神》德/英双底本逐字（PG #46203/#5321）+《点线面》OCR；书信多经英译转引（逐条标）；[OCR] 已最小订正 |
| velazquez.md | 20 | 3 | 7 | 5 | 结构性无自述（0 条为事实；行内 token 为正文提及）；Palomino/Pacheco + 馆方文本；[later testimony] 5 / [contemporary poem] 2 另列 |
| bosch.md | 26 | 0 | 1 | 15 | 无存世文字；档案转写 + [early account] 14 条（16–17 世纪文献）另列；[research] 4 另列；charter 未逐件回查（已声明） |
| huang_gongwang.md | 24 | 15 | 1 | 6 | 《写山水诀》11 条（维基文库 raw 直读）+ 台北故宫题跋；[later reception] 6 条另列；校勘 [校] 标注不改原文 |
| kahlo.md | 24 | 20 | 1 | 1 | 日记/书信/写作 + 口述（[self-spoken] 6 条另列）；书刊转引给页码；西/英双版并存 |
| behzad.md | 21 | 1 | 0 | 5 | 无自述传世；[inscription] 8 + [later record] 11 另列；波斯/察合台原文未回查（已声明） |
| friedrich.md | 31 | 21 | 5 | 10 | Hinz/Zschoche 书信与遗稿（德文经转引，英译逐条注明）；未回查德文原刊者不伪造（已声明） |
| repin.md | 23 | 23 | 1 | 5 | ru.wikisource 书信/回忆录/文集；Переписка т.1–3 OCR 回查；两版本日期差异并列标注 |
| ravi_varma.md | 30 | 5 | 3 | 11 | 原典（日记/书信/专著）未直读（逐条标注）；[research] 18 条另列；GAC 基金会展 8 篇等载体 |
| degas.md | 36 | 5 | 26 | 7 | 无系统著作；转记载体逐条标注（Moore/Vollard 原书全文核过）；[research] 2 另列 |
| gauguin.md | 33 | 25 | 6 | 6 | Noa Noa 法文版 + Avant et Après + 书信集（法/英双底本）；保留时代语境条目（单列） |
| van_eyck.md | 20 | 0 | 4 | 6 | 题刻为「自述」核心（[inscription] 13 条另列）；Facio / 丢勒日记 / Vasari 记述；无书信/笔记存世 |
| kngwarreye.md | 18 | 0 | 4 | 0 | 口述艺术家：全为 Anmatyerre 语口述英译（[self-spoken] 11 条另列）；原住民伦理约束（仪式内容不收） |
| hiroshige.md | 24 | 4 | 0 | 5 | 旅日記/题记/辞世句逐字；早期研究（1900s–1930s）与接受史记录分层收录；馆方/学术转引逐条标注 |
| sargent.md | 30 | 10 | 14 | 7 | Charteris 1927 全文 OCR；书信/致辞/课堂记录分层；[research] 3 条另列 |
| piero_della_francesca.md | 24 | 11 | 7 | 3 | 《De prospectiva pingendi》中古意大利语原文逐字；[inscription] 4 条另列；Vasari 旧说 2 条已订正 |
| artemisia_gentileschi.md | 29 | 13 | 3 | 10 | 庭审证词/书信逐字（[self-spoken] 8 条另列）；1653 戏谑墓志铭误传源头已辨；[later reception] 10 条另列 |
| namatjira.md | 22 | 0 | 5 | 4 | 口述记录分层（转写者随条标注）；[self-spoken] 12 条另列；原住民伦理约束（限制性内容不收） |
| el_salahi.md | 44 | 0 | 1 | 0 | 访谈/笔记/回忆录（[self-spoken] 38 条另列）；全为已刊记录转引，逐条标注 |
| wu_guanzhong.md | 40 | 24 | 6 | 0 | 文论/自传/题句/书信 + 受访口述（[self-spoken] 6 条另列）；转引逐条标注 |
| fan_kuan.md | 26 | 0 | 0 | 15 | 无文字传世——「自述」经宋人转述；《宋朝名画评》四库本全文；[later reception] 8 条另列 |
| sesshu.md | 17 | 8 | 0 | 10 | 自序/款记/书状 + 同代题赞纪行；[later record] 3 条另列（江户期画史与传说） |
| constable.md | 36 | 24 | 5 | 4 | 书信/讲稿/展签 + 作品背面题记（[inscription] 9 条另列）；[later reception] 4 条另列 |
| poussin.md | 24 | 16 | 5 | 9 | 书信/笔记逐字（Jouanny 1911 页码级）；转记逐条标注 |
| bruegel.md | 28 | 2 | 1 | 5 | 同时代记录（1567–1598）+ van Mander 1604 早期传记 + 馆方文本；学术转引逐条标注 |
| el_greco.md | 30 | 10 | 3 | 14 | 批注/书信/题记/遗嘱 + 转记（经文学化者标注）；[later reception] 7 条另列 |
| holbein.md | 26 | 12 | 6 | 11 | 签名/题铭/遗嘱（画进作品的文字与法律文书）；van Mander 订正已入；引文 18/18 |
| aivazovsky.md | 34 | 19 | 6 | 17 | 书信/文书/题写 + 同时代记录（1836–1904）；[research] 3 条另列；2 条 OVERTURNED 版本修正 |
| okeeffe.md | 35 | 26 | 2 | 4 | 书信/自传/展览声明 + 口述（[self-spoken] 9 条另列）；[later reception] 7 条另列；引文 42/42 |
| rivera.md | 23 | 5 | 12 | 3 | 声明/书信/写作 + 受访（[self-spoken] 7 条另列）；镜像 vs 卡罗互查 |
| zhao_mengfu.md | 24 | 13 | 2 | 8 | 题跋/款识/书论/诗（含「用笔千古不易」第七跋自纠）；[later reception] 7 条另列 |
| ni_zan.md | 35 | 20 | 1 | 9 | 画论/题识/题跋/诗曲；[later reception] 9 条另列；bada 互查留档 |
| qiu_ying.md | 24 | 0 | 0 | 0 | 标注为中文类目（同代记述/史料/研究/转引）——三列英文口径计 0；转引件逐条标注 |
| ogata_korin.md | 24 | 6 | 2 | 4 | 款印/文书/遗言 + 家人/同代记录；[later reception] 16 条另列（含馆方研究） |
| blake.md | 28 | 30 | 7 | 4 | 书信/自印书籍诗文/笔记/版画铭文（Erdman 1988 逐字）；3 条 OVERTURNED 已订正 |
| chardin.md | 28 | 3 | 5 | 11 | 书信 + 转记（Cochin/Diderot 闭环）；[research] 12 条另列；引文 37/37 |
| manet.md | 26 | 11 | 11 | 7 | 书信/图录序/笔记 + 转记；[research] 1 条另列；vs 萨金特逐条对齐 |
| sorolla.md | 31 | 7 | 15 | 9 | 书信/笔记 + 转记（1909 两卷本 OCR 行号级）；[research] 6 条另列 |
| zorn.md | 33 | 9 | 5 | 10 | 自传笔记/书信/题记 + 转记（Jansson 2022 全文直读升级）；[research] 15 条另列 |
| sultan_mohammed.md | 24 | 1 | 0 | 4 | 题记/签名（[inscription] 3 条另列）+ 同时代/早期记录（[later record] 6 条另列）；归属分级纪律 |
| xu_beihong.md | 37 | 29 | 2 | 5 | 讲演辞（1926《申报》）/文论/题句/书信 + 年谱辑录；转引逐条标注（一手底本未逐件核） |
| li_keran.md | 46 | 15 | 11 | 0 | 李可染艺术基金会语录（官方发布）逐字 + 年表/藏品页；记录稿与转述稿分级标注 |
| sher_gil.md | 32 | 32 | 3 | 3 | 书信/短文——全部转引级（标准版书信集未直读，逐条注转引链）；拼写原样+[sic] 标注 |
| tarsila.md | 28 | 10 | 2 | 5 | 1923 信影印（拍卖图录）/专栏/受访 + 馆方页；书刊转引给页码；译文版本注明 |
| chen_hongshou.md | 26 | 15 | 2 | 7 | 《陈老莲别传》《陶庵梦忆》直读 + 画论/题识；[later reception] 7 条另列；校勘记已出 |
| xu_wei.md | 29 | 25 | 1 | 3 | 题画诗/题跋/表/铭（故宫/上博/台北故宫直读）；[later reception] 5 条另列 |
| hogarth.md | 29 | 26 | 3 | 4 | 《美的分析》（Gutenberg #51459）+ 自传笔记/Remarks（1833 排印）+ 广告公告；转记逐条标注 |
| mir_sayyid_ali.md | 28 | 0 | 0 | 9 | 无自述传世——题记/签名（[inscription] 7 条另列）+ 记录/研究；OCR 轻校已声明 |
| de_chirico.md | 32 | 19 | 0 | 0 | 基金会官网 Scritti/访谈全文 + Gartz 书信英译 + 自传/小说/诗；转引链逐条标注 |
| rockwell.md | 34 | 7 | 7 | 0 | 自传转录层 + New Yorker 1945 直读 + SEP/NRM 档案；原书页码未逐页回查（已声明） |

缺口与验证声明见各文件末节（「缺口与待验证」）。
**未纳入（在产）**：无（wave21 十位已随 IndexMerge4 并入，2026-10-16）。
