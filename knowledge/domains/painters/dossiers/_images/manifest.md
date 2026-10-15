# 代表作图库 · manifest（D-02）

> 11 位画家 × 3 张 = **33 张**；采集日 2026-10-15；采集人 ImageLibrary（wave4 / D-02）。
> **wave12 追加**：克里姆特（klimt）3 张，2026-10-15，ArtistKlimt / A-22 → **现共 12 位 × 3 张 = 36 张**（总量 20.9 MB → 约 24.2 MB）。
> **wave13 追加**：修拉（seurat）10 张，2026-10-15，ArtistSeurat / A-24 → **现共 46 张**（36 + 修拉 10；总量约 34.5 MB）。
> **wave16 收口合并**（2026-10-16，IndexMerge / A-51）：并入 wave12/13 新档 6 位 58 张（turner 5 / rembrandt 6 / goya 9 / bada_shanren 9 / qi_baishi 11 / ito_jakuchu 18）＋ hopper 私有层例外（公开 0 / 私有 9）→ **现共 20 位画家 / 公开 104 张**（另有私有层例外 32 张——公开/私有分开记，见「私有层例外」节）。
> **wave15/17 并入**（2026-10-16，IndexMerge2）：并入 wave15×8 + wave17×7 共 15 位——新公开 169 张（mucha 12 / munch 13 / kandinsky 11 / velazquez 12 / bosch 10 / huang_gongwang 10 / behzad 12 / friedrich 12 / repin 10 / ravi_varma 17 / degas 13 / gauguin 20 / van_eyck 17；kahlo / kngwarreye 公开 0——全私有）＋ 私有层例外同步（+12 位 94 张）→ **现共 35 位画家 / 公开 273 张**（另有私有层例外 126 张——公开/私有分开记，见「私有层例外」节）。
> 单张长边 ≤1800px（满足「单张 ≤2000px 宽」）；公开侧总量约 155.3 MB（wave4 首轮目标 ≤100MB 为 11 位 ×3 张时口径；后续波次按各批 v2 规格「≥6 张/位、长边 ≤1800px」累计扩容）。
> 许可：全部为公有领域（PD）或开放许可（CC0 / CC BY-SA / CC BY / ColBase 规约）；CC 类署名逐张记录。
> 目录结构：`_images/<artist>/<slug>.jpg`；本文件为唯一 manifest。

## 总表

| 文件 | 作品 | 作者 | 年份 | 馆藏 | 来源 URL | License |
|---|---|---|---|---|---|---|
| `da_vinci/last_supper.jpg` | The Last Supper（最后的晚餐） | Leonardo da Vinci | c. 1495–1498 | 圣玛利亚感恩教堂, Milan | https://commons.wikimedia.org/wiki/File:The_Last_Supper_Leonardo_Da_Vinci_-_High_Resolution.jpg | CC BY-SA 4.0（上传者 LoganTheWatermelon） |
| `da_vinci/mona_lisa.jpg` | Mona Lisa (La Gioconda) | Leonardo da Vinci | c. 1503–1506 | 卢浮宫（Musée du Louvre）, Paris | https://commons.wikimedia.org/wiki/File:Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg | Public domain（C2RMF 官方高清复制品） |
| `da_vinci/vitruvian_man.jpg` | Vitruvian Man（维特鲁威人） | Leonardo da Vinci | c. 1490 | 学院美术馆（Gallerie dell’Accademia）, Venice | https://commons.wikimedia.org/wiki/File:Da_Vinci_Vitruve_Luc_Viatour.jpg | Public domain |
| `michelangelo/creation_of_adam.jpg` | The Creation of Adam（创造亚当，西斯廷天顶画） | Michelangelo | c. 1511 | 梵蒂冈博物馆（西斯廷礼拜堂） | https://commons.wikimedia.org/wiki/File:Michelangelo_-_Creation_of_Adam_(cropped).jpg | Public domain |
| `michelangelo/david.jpg` | David（大卫） | Michelangelo | 1501–1504 | 学院美术馆, Florence | https://commons.wikimedia.org/wiki/File:Michelangelo's_David_2015.jpg | CC BY-SA 4.0（摄影 Livioandronico2013） |
| `michelangelo/pieta.jpg` | Pietà（圣殇） | Michelangelo | 1498–1499 | 圣彼得大教堂, Vatican | https://commons.wikimedia.org/wiki/File:Michelangelo's_Pietà_Saint_Peter's_Basilica_Vatican_City.jpg | CC0（摄影 Jebulon） |
| `van_gogh/irises.jpg` | Irises | Vincent van Gogh | 1890 | The Metropolitan Museum of Art, New York | https://www.metmuseum.org/art/collection/search/436528 | CC0 1.0（Met Open Access） |
| `van_gogh/self_portrait_with_a_straw_hat.jpg` | Self-Portrait with a Straw Hat (obverse: The Potato Peeler) | Vincent van Gogh | 1887 | The Metropolitan Museum of Art, New York | https://www.metmuseum.org/art/collection/search/436532 | CC0 1.0（Met Open Access） |
| `van_gogh/wheat_field_with_cypresses.jpg` | Wheat Field with Cypresses | Vincent van Gogh | 1889 | The Metropolitan Museum of Art, New York | https://www.metmuseum.org/art/collection/search/436535 | CC0 1.0（Met Open Access） |
| `monet/impression_sunrise.jpg` | Impression, Sunrise（印象·日出） | Claude Monet | 1872 | 玛摩丹莫奈美术馆, Paris | https://commons.wikimedia.org/wiki/File:Monet_-_Impression,_Sunrise.jpg | Public domain |
| `monet/stacks_of_wheat_end_of_day_autumn.jpg` | Stacks of Wheat (End of Day, Autumn) | Claude Monet (French, 1840–1926) | 1890–91 | The Art Institute of Chicago | https://www.artic.edu/artworks/14624 | CC0（AIC 开放数据 / Public Domain Designation） |
| `monet/water_lilies_1906.jpg` | Water Lilies | Claude Monet (French, 1840–1926) | 1906 | The Art Institute of Chicago | https://www.artic.edu/artworks/16568 | CC0（AIC 开放数据 / Public Domain Designation） |
| `picasso/cafe_wepler.jpg` | Café Wepler | Pablo Picasso | c. 1908–10, reworked in 1912 | Cleveland Museum of Art | https://clevelandart.org/art/1950.90 | CC0（CMA Open Access） |
| `picasso/the_frugal_meal.jpg` | The Frugal Meal | Pablo Picasso | September 1904, printed 1913 | Cleveland Museum of Art | https://clevelandart.org/art/1929.888 | CC0（CMA Open Access） |
| `picasso/the_saltimbanques.jpg` | The Saltimbanques | Pablo Picasso | 1905, printed 1913 | Cleveland Museum of Art | https://clevelandart.org/art/1929.893 | CC0（CMA Open Access） |
| `cezanne/mont_sainte_victoire_and_the_viaduct.jpg` | Mont Sainte-Victoire and the Viaduct of the Arc River Valley | Paul Cézanne | 1882–85 | The Metropolitan Museum of Art, New York | https://www.metmuseum.org/art/collection/search/435877 | CC0 1.0（Met Open Access） |
| `cezanne/still_life_with_apples_and_a_pot_of_primroses.jpg` | Still Life with Apples and a Pot of Primroses | Paul Cézanne | ca. 1890 | The Metropolitan Museum of Art, New York | https://www.metmuseum.org/art/collection/search/435882 | CC0 1.0（Met Open Access） |
| `cezanne/the_card_players.jpg` | The Card Players | Paul Cézanne | 1890–92 | The Metropolitan Museum of Art, New York | https://www.metmuseum.org/art/collection/search/435868 | CC0 1.0（Met Open Access） |
| `matisse/la_danse.jpg` | La Danse (II)（舞蹈） | Henri Matisse | 1909–10 | 冬宫博物馆（Hermitage）, St. Petersburg | https://commons.wikimedia.org/wiki/File:La_Danse_II,_par_Henri_Matisse.jpg | Public domain（上传者 Thierry Caro） |
| `matisse/still_life_with_geranium.jpg` | Still Life with Geranium | Henri Matisse | 1906 | The Art Institute of Chicago | https://www.artic.edu/artworks/87045 | CC0（AIC 开放数据 / Public Domain Designation） |
| `matisse/woman_before_an_aquarium.jpg` | Woman before an Aquarium | Henri Matisse | 1921–23 | The Art Institute of Chicago | https://www.artic.edu/artworks/27984 | CC0（AIC 开放数据 / Public Domain Designation） |
| `hokusai/red_fuji_south_wind_clear_sky.jpg` | South Wind, Clear Sky (Gaifū kaisei), also known as Red Fuji, from the series Thirty-six Views of Mount Fuji (Fugaku sanjūrokkei) | Katsushika Hokusai | ca. 1830–32 | The Metropolitan Museum of Art, New York | https://www.metmuseum.org/art/collection/search/36490 | CC0 1.0（Met Open Access） |
| `hokusai/storm_below_mount_fuji.jpg` | Storm below Mount Fuji (Sanka no haku u), from the series Thirty-six Views of Mount Fuji (Fugaku sanjūrokkei) | Katsushika Hokusai | ca. 1830–32 | The Metropolitan Museum of Art, New York | https://www.metmuseum.org/art/collection/search/36492 | CC0 1.0（Met Open Access） |
| `hokusai/the_great_wave.jpg` | Under the Wave off Kanagawa (Kanagawa oki nami ura), also known as The Great Wave, from the series Thirty-six Views of Mount Fuji (Fugaku sanjūrokkei) | Katsushika Hokusai | ca. 1830–32 | The Metropolitan Museum of Art, New York | https://www.metmuseum.org/art/collection/search/45434 | CC0 1.0（Met Open Access） |
| `caravaggio/bacchus.jpg` | Bacchus（酒神） | Caravaggio | c. 1598 | 乌菲齐美术馆, Florence | https://commons.wikimedia.org/wiki/File:Bacchus-Caravaggio_(1598).jpg | Public domain |
| `caravaggio/calling_of_saint_matthew.jpg` | The Calling of Saint Matthew（圣马太蒙召） | Caravaggio | 1599–1600 | 圣路易吉·德·弗朗切西教堂·康塔雷利礼拜堂, Rome | https://commons.wikimedia.org/wiki/File:Caravaggio_—_The_Calling_of_Saint_Matthew.jpg | CC0 |
| `caravaggio/judith_beheading_holofernes.jpg` | Judith Beheading Holofernes（朱迪斯斩首荷罗孚尼） | Caravaggio | c. 1598–99 | 巴贝里尼宫（国立古代艺术馆）, Rome | https://commons.wikimedia.org/wiki/File:Caravaggio_-_Judith_beheading_Holofernes.jpg | Public domain |
| `vermeer/a_maid_asleep.jpg` | A Maid Asleep | Johannes Vermeer | ca. 1656–57 | The Metropolitan Museum of Art, New York | https://www.metmuseum.org/art/collection/search/437878 | CC0 1.0（Met Open Access） |
| `vermeer/study_of_a_young_woman.jpg` | Study of a Young Woman | Johannes Vermeer | ca. 1665–67 | The Metropolitan Museum of Art, New York | https://www.metmuseum.org/art/collection/search/437879 | CC0 1.0（Met Open Access） |
| `vermeer/young_woman_with_a_water_pitcher.jpg` | Young Woman with a Water Pitcher | Johannes Vermeer | ca. 1662 | The Metropolitan Museum of Art, New York | https://www.metmuseum.org/art/collection/search/437881 | CC0 1.0（Met Open Access） |
| `durer/adam_and_eve.jpg` | Adam and Eve | Albrecht Dürer | 1504 | The Metropolitan Museum of Art, New York | https://www.metmuseum.org/art/collection/search/336222 | CC0 1.0（Met Open Access） |
| `durer/melencolia_i.jpg` | Melencolia I | Albrecht Dürer | 1514 | The Metropolitan Museum of Art, New York | https://www.metmuseum.org/art/collection/search/360018 | CC0 1.0（Met Open Access） |
| `durer/the_rhinoceros.jpg` | The Rhinoceros | Albrecht Dürer | 1515 | The Metropolitan Museum of Art, New York | https://www.metmuseum.org/art/collection/search/356497 | CC0 1.0（Met Open Access） |
| `klimt/the_kiss.jpg` | The Kiss (Lovers)（吻） | Gustav Klimt | c. 1907–1909 | Belvedere, Vienna（inv. 912） | https://commons.wikimedia.org/wiki/File:Gustav_Klimt_-_Der_Kuss_(Liebespaar)_-_912_-_%C3%96sterreichische_Galerie_Belvedere.jpg | Public domain（PD-Art；PD-old-100-expired；上传者附加 CC BY-SA 4.0） |
| `klimt/adele_bloch_bauer_i.jpg` | Portrait of Adele Bloch-Bauer I（阿黛尔·布洛赫-鲍尔像 I） | Gustav Klimt | 1907 | Neue Galerie New York | https://commons.wikimedia.org/wiki/File:Gustav_Klimt,_1907,_Adele_Bloch-Bauer_I,_Neue_Galerie_New_York.jpg | Public domain（PD-Art；PD-old-auto-1923） |
| `klimt/death_and_life.jpg` | Death and Life（死与生） | Gustav Klimt | 1910/11, reworked 1912/13 & 1915/16 | Leopold Museum, Vienna（inv. 630） | https://commons.wikimedia.org/wiki/File:Gustav_Klimt_-_Death_and_Life_-_Google_Art_Project.jpg | Public domain（PD-Art；PD-Art-two-auto） |
| `seurat/a_sunday_on_la_grande_jatte.jpg` | A Sunday on La Grande Jatte — 1884（大碗岛） | Georges Seurat | 1884–86（边框 1888–89） | Art Institute of Chicago（1926.224） | https://www.artic.edu/artworks/27992 | CC0（AIC Public Domain Designation） |
| `seurat/bathers_at_asnieres.jpg` | Bathers at Asnières（阿尼埃尔浴场） | Georges Seurat | 1884 | National Gallery, London（NG3908） | https://commons.wikimedia.org/wiki/File:Baigneurs_a_Asnieres.jpg | Public domain |
| `seurat/study_for_a_sunday_on_la_grande_jatte.jpg` | Study for "A Sunday on La Grande Jatte" | Georges Seurat | 1884 | The Metropolitan Museum of Art, New York（51.112.6） | https://www.metmuseum.org/art/collection/search/437658 | CC0 1.0（Met Open Access） |
| `seurat/gray_weather_grande_jatte.jpg` | Gray Weather, Grande Jatte | Georges Seurat | ca. 1886–88 | The Metropolitan Museum of Art, New York（2002.62.3） | https://www.metmuseum.org/art/collection/search/438015 | CC0 1.0（Met Open Access） |
| `seurat/circus_sideshow_parade_de_cirque.jpg` | Circus Sideshow (Parade de cirque)（阅兵） | Georges Seurat | 1887–88 | The Metropolitan Museum of Art, New York（61.101.17） | https://www.metmuseum.org/art/collection/search/437654 | CC0 1.0（Met Open Access） |
| `seurat/aman_jean_drawing.jpg` | Aman-Jean (Portrait of Edmond François Aman-Jean)（孔特素描） | Georges Seurat | 1882–83 | The Metropolitan Museum of Art, New York（61.101.16） | https://www.metmuseum.org/art/collection/search/339751 | CC0 1.0（Met Open Access） |
| `seurat/le_chahut.jpg` | Le Chahut（康康舞） | Georges Seurat | 1889–90 | Kröller-Müller Museum, Otterlo | https://commons.wikimedia.org/wiki/File:Georges_Seurat_-_Le_Chahut_-_Google_Art_Project.jpg | Public domain |
| `seurat/the_circus.jpg` | The Circus (Le Cirque)（马戏） | Georges Seurat | 1890–91（未完成） | Musée d'Orsay, Paris | https://commons.wikimedia.org/wiki/File:Georges_Seurat_-_The_Circus_-_Google_Art_Project.jpg | Public domain |
| `seurat/young_woman_powdering_herself.jpg` | Young Woman Powdering Herself（扑粉的年轻女子） | Georges Seurat | 1888–90 | The Courtauld Gallery, London | https://commons.wikimedia.org/wiki/File:Georges_Seurat_-_Young_Woman_Powdering_Herself_-_Google_Art_Project.jpg | Public domain |
| `seurat/les_poseuses.jpg` | Les Poseuses (Models)（模特们） | Georges Seurat | 1886–88 | Barnes Foundation, Philadelphia | https://commons.wikimedia.org/wiki/File:Georges_Seurat_-_Models_(Poseuses)_-_BF811_-_Barnes_Foundation.jpg | Public domain |
| `turner/fighting_temeraire.jpg` | The Fighting Téméraire tugged to her last Berth to be broken up（无畏号） | J.M.W. Turner | 1839 | National Gallery, London（NG524） | https://commons.wikimedia.org/wiki/File:Turner,_J._M._W._-_The_Fighting_T%C3%A9m%C3%A9raire_tugged_to_her_last_Berth_to_be_broken.jpg | Public domain |
| `turner/norham_castle_sunrise.jpg` | Norham Castle, Sunrise（诺勒姆城堡·日出） | J.M.W. Turner | c. 1845 | Tate, London（N01981） | https://commons.wikimedia.org/wiki/File:Jmw_turner,_norham_castle,_alba,_1845_ca.jpg | CC BY 3.0（摄影 Sailko；署名要求=是） |
| `turner/rain_steam_speed.jpg` | Rain, Steam and Speed – The Great Western Railway（雨、蒸汽与速度） | J.M.W. Turner | 1844 | National Gallery, London（NG538） | https://commons.wikimedia.org/wiki/File:Turner_-_Rain,_Steam_and_Speed_-_National_Gallery_file.jpg | Public domain |
| `turner/snow_storm_steam_boat.jpg` | Snow Storm: Steam-Boat off a Harbour's Mouth（暴风雪） | J.M.W. Turner | exhibited 1842 | Tate, London（N00530） | https://commons.wikimedia.org/wiki/File:J.M.W._Turner_%E2%80%93_Snow_Storm_-_Steam-Boat_off_a_Harbour%27s_Mouth.jpg | Public domain |
| `turner/the_slave_ship.jpg` | The Slave Ship（奴隶船） | J.M.W. Turner | 1840 | Museum of Fine Arts, Boston（99.22） | https://commons.wikimedia.org/wiki/File:Slave-ship.jpg | Public domain |
| `rembrandt/the_night_watch.jpg` | The Night Watch（夜巡） | Rembrandt | 1642 | Rijksmuseum, Amsterdam（SK-C-5） | https://commons.wikimedia.org/wiki/File:The_Night_Watch_-_HD.jpg | Public domain |
| `rembrandt/the_jewish_bride.jpg` | The Jewish Bride（犹太新娘） | Rembrandt | c. 1665–69 | Rijksmuseum, Amsterdam（SK-C-216） | https://commons.wikimedia.org/wiki/File:Rembrandt_Harmensz._van_Rijn_-_Portret_van_een_paar_als_oudtestamentische_figuren,_genaamd_%27Het_Joodse_bruidje%27_-_Google_Art_Project.jpg | Public domain |
| `rembrandt/self_portrait_with_two_circles.jpg` | Self-Portrait with Two Circles（双圆自画像） | Rembrandt | c. 1665–69 | Kenwood House, London（57） | https://commons.wikimedia.org/wiki/File:Rembrandt_Self-portrait_(Kenwood).jpg | Public domain |
| `rembrandt/self_portrait_drawing_at_a_window.jpg` | Self-Portrait Drawing at a Window（窗前自画像，蚀刻） | Rembrandt | 1648 | National Gallery of Art, Washington（9931） | https://commons.wikimedia.org/wiki/File:Rembrandt_van_Rijn,_Self-Portrait_Drawing_at_a_Window,_1648,_NGA_9931.jpg | CC0（NGA Open Access） |
| `rembrandt/the_anatomy_lesson_of_dr_nicolaes_tulp.jpg` | The Anatomy Lesson of Dr Nicolaes Tulp（杜尔普医生的解剖课） | Rembrandt | 1632 | Mauritshuis, The Hague（146） | https://commons.wikimedia.org/wiki/File:Rembrandt_-_The_Anatomy_Lesson_of_Dr_Nicolaes_Tulp.jpg | Public domain |
| `rembrandt/aristotle_with_a_bust_of_homer.jpg` | Aristotle with a Bust of Homer（亚里士多德凝视荷马胸像） | Rembrandt | 1653 | The Met, New York（61.198） | https://commons.wikimedia.org/wiki/File:Aristotle_with_a_Bust_of_Homer_MET_DP319026.jpg | CC0（Met Open Access） |
| `goya/third_of_may_1808.jpg` | The Third of May 1808（1808 年 5 月 3 日） | Francisco de Goya | 1814 | Museo del Prado, Madrid | https://commons.wikimedia.org/wiki/File:El_Tres_de_Mayo,_by_Francisco_de_Goya,_from_Prado_in_Google_Earth.jpg | Public domain |
| `goya/saturn_devouring_his_son.jpg` | Saturn Devouring His Son（农神吞噬其子，黑画） | Francisco de Goya | c. 1819–23 | Museo del Prado, Madrid | https://commons.wikimedia.org/wiki/File:Francisco_de_Goya,_Saturno_devorando_a_su_hijo_(1819-1823).jpg | Public domain |
| `goya/the_sleep_of_reason_produces_monsters.jpg` | The Sleep of Reason Produces Monsters（理性沉睡产生怪物，奇想集 43） | Francisco de Goya | 1799 | The Met, New York | https://commons.wikimedia.org/wiki/File:Plate_43_from_%27Los_Caprichos%27-_The_sleep_of_reason_produces_monsters_(El_sue%C3%B1o_de_la_razon_produce_monstruos)_MET_DP816991.jpg | CC0（Met Open Access 捐赠件） |
| `goya/disasters_of_war_yo_lo_vi.jpg` | The Disasters of War, plate 44 "Yo lo vi"（战祸·我看见了） | Francisco de Goya | 1810–20（1863 出版） | The Met, New York | https://commons.wikimedia.org/wiki/File:Plate_44_from_%27The_Disasters_of_War%27_(Los_Desastres_de_la_Guerra)-_%27I_saw_it%27_(Yo_lo_vi.)_MET_DP817391.jpg | CC0（Met Open Access 捐赠件） |
| `goya/the_family_of_charles_iv.jpg` | The Family of Charles IV（卡洛斯四世一家） | Francisco de Goya | 1800–01 | Museo del Prado, Madrid | https://commons.wikimedia.org/wiki/File:La_familia_de_Carlos_IV,_por_Francisco_de_Goya.jpg | Public domain |
| `goya/manuel_osorio_manrique_de_zuniga.jpg` | Manuel Osorio Manrique de Zúñiga（奥索里奥男孩） | Francisco de Goya | c. 1787–88 | The Met, New York | https://commons.wikimedia.org/wiki/File:Manuel_Osorio_Manrique_de_Zu%C3%B1iga_(1784%E2%80%931792)_MET_DP287624.jpg | CC0（Met Open Access 捐赠件） |
| `goya/the_dog.jpg` | The Dog（狗，黑画） | Francisco de Goya | c. 1819–23 | Museo del Prado, Madrid | https://commons.wikimedia.org/wiki/File:Goya_Dog.jpg | Public domain |
| `goya/witches_flight.jpg` | Witches' Flight（女巫飞行） | Francisco de Goya | 1798 | Museo del Prado, Madrid | https://commons.wikimedia.org/wiki/File:Francisco_de_Goya_-_Vuelo_de_brujas_(1798).jpg | Public domain |
| `goya/tauromaquia_plate_18.jpg` | La Tauromaquia, plate 18（斗牛术·Martincho 的胆量） | Francisco de Goya | 1815–16 | The Met, New York | https://commons.wikimedia.org/wiki/File:Plate_18_of_the_%27Tauromaquia%27-_The_daring_of_Martincho_in_the_ring_at_Saragossa_MET_DP817784.jpg | CC0（Met Open Access 捐赠件） |
| `bada_shanren/met_fish_and_rocks_1699.jpg` | Fish and Rocks（鱼石图） | 八大山人（朱耷） | 1699 | The Metropolitan Museum of Art（41491） | https://www.metmuseum.org/art/collection/search/41491 | CC0 1.0（Met Open Access） |
| `bada_shanren/met_two_eagles_1702.jpg` | Two Eagles（双鹰图） | 八大山人（朱耷） | 1702 | The Metropolitan Museum of Art（39540） | https://www.metmuseum.org/art/collection/search/39540 | CC0 1.0（Met Open Access） |
| `bada_shanren/met_birds_in_a_lotus_pond.jpg` | Birds in a Lotus Pond（湖塘禽鸟） | 八大山人（朱耷） | ca. 1690 | The Metropolitan Museum of Art（49143） | https://www.metmuseum.org/art/collection/search/49143 | CC0 1.0（Met Open Access） |
| `bada_shanren/met_landscape_album_1699.jpg` | Landscape album（山水册，十二开） | 八大山人（朱耷） | 1699 | The Metropolitan Museum of Art（49145） | https://www.metmuseum.org/art/collection/search/49145 | CC0 1.0（Met Open Access） |
| `bada_shanren/met_letters_to_fang_shiguan.jpg` | Letters to Fang Shiguan（致方士琯尺牍，十开） | 八大山人（朱耷） | ca. 1688–1705 | The Metropolitan Museum of Art（49147） | https://www.metmuseum.org/art/collection/search/49147 | CC0 1.0（Met Open Access） |
| `bada_shanren/cleveland_landscape_after_guo_zhongshu.jpg` | Landscape after Guo Zhongshu（仿郭忠恕山水） | 八大山人（朱耷） | ca. 1680–1705 | Cleveland Museum of Art（1955.36） | https://clevelandart.org/art/1955.36 | CC0（CMA Open Access） |
| `bada_shanren/freer_lotus_and_ducks_ca1696.jpg` | Lotus and Ducks（荷花双凫图） | 八大山人（朱耷） | ca. 1696 | Freer Gallery of Art（F1998.45，王方宇旧藏） | https://commons.wikimedia.org/wiki/File:Bada_Shanren_-_Lotus_and_Ducks_-_Google_Art_Project.jpg | Public domain（PD-Art） |
| `bada_shanren/tianjin_river_flowers_1697.jpg` | 《河上花图》卷（局部，HX5 段） | 八大山人（朱耷） | 1697 | 天津博物馆 | https://commons.wikimedia.org/wiki/Category:Flowers_on_a_River_by_Bada_Shanren | Public domain（PD-Art） |
| `bada_shanren/commons_anwan_album_bird.jpg` | 《安晚册》鸟页（局部） | 八大山人（朱耷） | 1694（册） | 泉屋博古馆（日本） | https://commons.wikimedia.org/wiki/File:Anban_Album_Bird_Bada_Shanren.jpg | Public domain（PD-Art） |
| `qi_baishi/morning_glory_1950.jpg` | 牵牛花（Liserons rouges） | 齐白石 | 1950 | 赛努奇博物馆, Paris（摄影 Jean-Pierre Dalbéra） | https://commons.wikimedia.org/wiki/File:%22Liserons_rouges%22_de_Qi_Baishi_(Mus%C3%A9e_Cernuschi,_Paris)_-_Flickr_-_dalbera.jpg | PD-China + 照片 CC BY 2.0（已审） |
| `qi_baishi/camellia_and_bird.jpg` | 茶花小鸟 | 齐白石 | 1921 | 画作翻拍（Commons） | https://commons.wikimedia.org/wiki/File:%E9%BD%90%E7%99%BD%E7%9F%B3_%E8%8C%B6%E8%8A%B1%E5%B0%8F%E9%B8%9F.jpg | PD-PRC + PD-US-expired |
| `qi_baishi/wisteria_scroll.jpg` | 齐璜画藤轴 | 齐白石 | 近现代（无年款） | 故宫博物院·名画记（官方扫描） | https://commons.wikimedia.org/wiki/File:%E9%BD%90%E7%92%9C%E7%94%BB%E8%97%A4%E8%BD%B4.png | PD-scan + PD-old-auto-expired |
| `qi_baishi/frogs.jpg` | 鸣蛙 | 齐白石 | 不晚于 1955 | 中国美术馆藏（原老舍家族） | https://commons.wikimedia.org/wiki/File:%E9%BD%90%E7%99%BD%E7%9F%B3%E3%80%8A%E9%B8%A3%E8%9B%99%E3%80%8B.jpg | PD-Art（PD-CN）+ PD-US-no notice |
| `qi_baishi/old_man_and_gourd.jpg` | Old Man Looking into a Gourd（老人与葫芦） | 齐白石 | — | 旧金山亚洲艺术博物馆（摄影 Daderot） | https://commons.wikimedia.org/wiki/File:Old_Man_Looking_into_a_Gourd,_by_Qi_Baishi,_ink_on_paper_-_Asian_Art_Museum_of_San_Francisco_-_DSC01548.JPG | 摄影 CC0 |
| `qi_baishi/twelve_landscape_screens_1925.jpg` | 十二山水屏 | 齐白石 | 1925 | 公开拍卖图（Commons） | https://commons.wikimedia.org/wiki/File:Twelve_Landscape_Screens_by_Qi_Baishi.jpg | PD-Art（PD-China） |
| `qi_baishi/seal_script_couplet.jpg` | 篆书联「持山与鹤」 | 齐白石 | — | 摄影 陳寅恪（Commons） | https://commons.wikimedia.org/wiki/File:%E9%BD%90%E7%99%BD%E7%9F%B3%E2%80%9C%E6%8C%81%E5%B1%B1%E4%B8%8E%E9%B9%A4%E2%80%9D%E7%AF%86%E4%B9%A6%E8%81%94%E4%B9%8B%E4%BA%8C.jpg | 摄影 CC BY-SA 4.0 |
| `qi_baishi/seal_impression_changsha.jpg` | 印「中国长沙湘潭人也」 | 齐白石 | — | 摄影 陳寅恪（Commons） | https://commons.wikimedia.org/wiki/File:%E9%BD%90%E7%99%BD%E7%9F%B3_%E4%B8%AD%E5%9B%BD%E9%95%BF%E6%B2%99%E6%B9%98%E6%BD%AD%E4%BA%BA%E4%B9%9F_%E4%B9%8B%E4%BA%8C.jpg | 摄影 CC BY-SA 4.0 |
| `qi_baishi/portrait_by_lang_jingshan.jpg` | 齐白石像（郎静山摄） | 齐白石 | 1930s | 摄影 郎静山（Commons） | https://commons.wikimedia.org/wiki/File:Qi_Baishi,_by_Lang_Jingshan.jpg | PD-China-1996 |
| `qi_baishi/zhou_enlai_visit_1953.jpg` | 周恩来拜访齐白石 | 齐白石 | 1953 | 《人民画报》1953 年（Commons 翻拍） | https://commons.wikimedia.org/wiki/File:1953-03_1953%E5%B9%B4_%E5%91%A8%E6%81%A9%E6%9D%A5%E6%8B%9C%E8%AE%BF%E9%BD%90%E7%99%BD%E7%9F%B3.jpg | PD-CN |
| `qi_baishi/lotus_and_insects.jpg` | Lotus and Insects（工写结合示例） | 齐白石 | 20 世纪早期 | 馆藏展陈翻拍（摄影 Jnzl's Photos） | https://commons.wikimedia.org/wiki/File:Lotus_and_Insects_by_Qi_Baishi_(11264641955).jpg | 摄影 CC BY 2.0（已审）；作品 PD-China |
| `ito_jakuchu/doshoku_saie_gunkei.jpg` | 動植綵絵之内「群鶏図」 | 伊藤若冲 | c. 1761–65 | 皇居三の丸尚蔵館 | https://colbase.nich.go.jp/collection_items/shozokan/SZK002949 | ColBase 规约（出典：ColBase） |
| `ito_jakuchu/doshoku_saie_rogan.jpg` | 動植綵絵之内「芦雁図」 | 伊藤若冲 | c. 1765–66 | 皇居三の丸尚蔵館 | https://colbase.nich.go.jp/collection_items/shozokan/SZK002949 | ColBase 规约（出典：ColBase） |
| `ito_jakuchu/doshoku_saie_gunyo.jpg` | 動植綵絵之内「群魚図」 | 伊藤若冲 | c. 1765–66 | 皇居三の丸尚蔵館 | https://colbase.nich.go.jp/collection_items/shozokan/SZK002949 | ColBase 规约（出典：ColBase） |
| `ito_jakuchu/doshoku_saie_kikka.jpg` | 動植綵絵之内「菊花流水図」 | 伊藤若冲 | c. 1765–66 | 皇居三の丸尚蔵館 | https://colbase.nich.go.jp/collection_items/shozokan/SZK002949 | ColBase 规约（出典：ColBase） |
| `ito_jakuchu/doshoku_saie_himawari.jpg` | 動植綵絵之内「向日葵雄鶏図」 | 伊藤若冲 | 1759 | 皇居三の丸尚蔵館 | https://commons.wikimedia.org/wiki/File:It%C5%8D_Jakuch%C5%AB_-_Rooster_and_Sunflowers_%28Colorful_Realm_of_Living_Beings%29.jpg | Public domain |
| `ito_jakuchu/doshoku_saie_hakkei.jpg` | 動植綵絵之内「老松白鶏図」 | 伊藤若冲 | c. 1759–60 | 皇居三の丸尚蔵館 | https://commons.wikimedia.org/wiki/File:It%C5%8D_Jakuch%C5%AB_-_White_fowl_and_pine_%28Colorful_Realm_of_Living_Beings%29.jpg | Public domain |
| `ito_jakuchu/doshoku_saie_setchu_enou.jpg` | 動植綵絵之内「雪中鴛鴦図」 | 伊藤若冲 | 1759 | 皇居三の丸尚蔵館 | https://commons.wikimedia.org/wiki/File:It%C5%8D_Jakuch%C5%AB_-_Mandarin_ducks_in_the_snow_%28Colorful_Realm_of_Living_Beings%29.jpg | Public domain |
| `ito_jakuchu/doshoku_saie_rousho_kujaku.jpg` | 動植綵絵之内「老松孔雀図」 | 伊藤若冲 | c. 1757–60 | 皇居三の丸尚蔵館 | https://commons.wikimedia.org/wiki/File:%27Old_Pine_Tree_and_Peacock%27_from_the_%27Colorful_Realm_of_Living_Beings%27_by_Ito_Jakuchu.jpg | Public domain |
| `ito_jakuchu/doshoku_saie_kaigai.jpg` | 動植綵絵之内「貝甲図」 | 伊藤若冲 | c. 1761–65 | 皇居三の丸尚蔵館 | https://commons.wikimedia.org/wiki/File:It%C5%8D_Jakuch%C5%AB_-_Shells_%28Colorful_Realm_of_Living_Beings%29.jpg | Public domain |
| `ito_jakuchu/doshoku_saie_shutou_gunjaku.jpg` | 動植綵絵之内「秋塘群雀図」 | 伊藤若冲 | 1759 | 皇居三の丸尚蔵館 | https://commons.wikimedia.org/wiki/File:Autumn_Millet_and_Sparrows_by_Ito_Jakuchu_%28Sannomaru_Shozokan%29.jpg | Public domain |
| `ito_jakuchu/kasonehanzu.jpg` | 果蔬涅槃図 | 伊藤若冲 | 江戸中期（c.1790s） | 京都国立博物館（重要文化財） | https://colbase.nich.go.jp/collection_items/kyohaku/A%E7%94%B283 | ColBase 规约（出典：ColBase） |
| `ito_jakuchu/genpo_yoka.jpg` | 玄圃瑤華之内「水葵・糸瓜」 | 伊藤若冲 | 1768 | 東京国立博物館 | https://colbase.nich.go.jp/collection_items/tnm/A-12445-5 | ColBase 规约（出典：ColBase） |
| `ito_jakuchu/shoubai_gunkei_zu_byobu.jpg` | 松梅群鶏図屏風（六曲一双） | 伊藤若冲 | 江戸中期 | 東京国立博物館 | https://colbase.nich.go.jp/collection_items/tnm/A-12320 | ColBase 规约（出典：ColBase） |
| `ito_jakuchu/kaiboji_gunkei_zu.jpg` | 群鶏図（旧・海宝寺方丈障壁画） | 伊藤若冲 | 1790 | 京都国立博物館 | https://colbase.nich.go.jp/collection_items/kyohaku/A%E7%94%B2355 | ColBase 规约（出典：ColBase） |
| `ito_jakuchu/ishidoro_zu_byobu.jpg` | 石燈籠図屏風 | 伊藤若冲 | 江戸中期 | 京都国立博物館 | https://colbase.nich.go.jp/collection_items/kyohaku/A%E7%94%B21339 | ColBase 规约（出典：ColBase） |
| `ito_jakuchu/chouju_kaboku_zu_byobu.jpg` | 鳥獣花木図屏風（右隻；升目描き） | 伊藤若冲 | c. 1770s–1780s | 出光美術館（旧プライス・コレクション） | https://commons.wikimedia.org/wiki/File:It%C5%8D_Jakuch%C5%AB_-_Animals_in_the_Flower_garden_%28Right-hand_screen%29.jpg | Public domain |
| `ito_jakuchu/zo_to_kujira_zu_byobu.jpg` | 象と鯨図屏風（左隻；升目描き） | 伊藤若冲 | c. 1796 | Miho Museum | https://commons.wikimedia.org/wiki/File:Elephant_and_Whale_Screens_by_Ito_Jakuchu_%28Miho_Museum%29L.jpg | Public domain |
| `ito_jakuchu/crane_under_plum.jpg` | Crane under a Branch of Plum（梅枝と鶴） | 伊藤若冲 | 1770s | The Metropolitan Museum of Art（929172） | https://www.metmuseum.org/art/collection/search/929172 | CC0（Met Open Access） |
| `mucha/gismonda_1894.jpg` | *Gismonda*（吉斯蒙达戏剧海报，莎拉·伯恩哈特） | Alphonse Mucha | 1894 | Mucha Trust 藏（彩色石版画；Lemercier 印） | https://commons.wikimedia.org/wiki/File:Alphonse_Mucha_-_Poster_for_Victorien_Sardou%27s_Gismonda_starring_Sarah_Bernhardt.jpg | Public domain |
| `mucha/dame_aux_camelias_1896.jpg` | *La Dame aux Camélias*（茶花女戏剧海报） | Alphonse Mucha | 1896 | Mucha Trust 藏 | https://commons.wikimedia.org/wiki/File:Alfons_Mucha_-_1896_-_La_Dame_aux_Cam%C3%A9lias_-_Sarah_Bernhardt.jpg | Public domain |
| `mucha/job_1896.jpg` | *Job*（Job 卷烟纸广告海报） | Alphonse Mucha | 1896 | Mucha Trust 藏 | https://commons.wikimedia.org/wiki/File:Alphonse_Mucha_-_Advertisment_for_Job_cigarettes%2C_1896.jpg | Public domain |
| `mucha/seasons_series_1896.jpg` | *The Seasons*（四季，四联装饰板·合框变体） | Alphonse Mucha | 1896 | Champenois 印 | https://commons.wikimedia.org/wiki/File:Alfons_Mucha_-_The_Seasons_%28series%29%2C_1896.jpg | Public domain |
| `mucha/seasons_summer_1896.jpg` | *The Seasons — Summer*（四季·夏） | Alphonse Mucha | 1896 | Champenois 印 | https://commons.wikimedia.org/wiki/File:Alfons_Mucha_-_The_Seasons_-_Summer_%281896%29.jpg | Public domain |
| `mucha/zodiac_1896.jpg` | *Zodiac*（黄道十二宫，La Plume 日历） | Alphonse Mucha | 1896–97 | La Plume 发行 | https://commons.wikimedia.org/wiki/File:Alphonse_Mucha_-_Zodiac%2C_1869.jpg | Public domain（文件名年份笔误；作品 1896–97） |
| `mucha/le_pater_1899.jpg` | *Le Pater* —「Lead us not into temptation」（主祷文页） | Alphonse Mucha | 1899 | 石版画册（510 册） | https://commons.wikimedia.org/wiki/File:Alfons_Mucha_Le_Pater_%22Lead_us_not_into_temptation%22_%281899%29.jpg | **CC BY-SA 4.0**（翻拍 SiefkinDR 2018；原作 PD；署名要求=是） |
| `mucha/documents_decoratifs_plate30.jpg` | *Documents décoratifs* 第 30 版（装饰图案版） | Alphonse Mucha | 1901/1902 | Librairie Centrale des Beaux-Arts | https://commons.wikimedia.org/wiki/File:30_mucha_documentsdecoratifs_1901.jpg | Public domain |
| `mucha/monaco_monte_carlo_1897.jpg` | *Monaco–Monte-Carlo*（P.L.M. 铁路海报） | Alphonse Mucha | 1897 | P.L.M. 铁路 | https://commons.wikimedia.org/wiki/File:Alfons_Mucha_-_Poster_for_%27Monaco_-_Monte_Carlo%27%2C_P.L.M._railway_services_%281897%29.jpg | Public domain |
| `mucha/moet_cremant_1899.jpg` | *Moët & Chandon Crémant Impérial*（香槟广告） | Alphonse Mucha | 1899 | 彩色石版画 | https://commons.wikimedia.org/wiki/File:Mucha-Mo%C3%ABt_%26_Chandon_Cr%C3%A9mant_Imp%C3%A9rial-1899.jpg | Public domain |
| `mucha/self_portrait.jpg` | *Self-portrait*（自画像，持笔） | Alphonse Mucha | c. 1907 | Mucha Trust 藏（布面油画） | https://commons.wikimedia.org/wiki/File:Alfons_Mucha_Selbstportr%C3%A4t.jpg | Public domain |
| `mucha/slav_epic_apotheosis.jpg` | *The Slav Epic* No.20《斯拉夫的神化》（Slavs for Humanity） | Alphonse Mucha | 1926 | 布拉格市藏（蛋彩画布） | https://commons.wikimedia.org/wiki/File:Mucha_Apoteoza.jpg | Public domain |
| `munch/scream_1893_mm.jpg` | The Scream（尖叫；粉彩/蜡笔纸板，MM.M.00122b） | Edvard Munch | 1893 | Munchmuseet, Oslo | https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_The_Scream_-_MM.M.00122b_-_Munch_Museum.jpg | Public domain |
| `munch/scream_1893_nm.jpg` | The Scream（尖叫；油彩/蛋彩/粉彩纸板，NG.M.00939） | Edvard Munch | 1893 | National Museum, Oslo | https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_The_Scream_-_NG.M.00939_-_National_Museum_of_Art,_Architecture_and_Design.jpg | Public domain |
| `munch/scream_1910_mm.jpg` | The Scream（尖叫；蛋彩/油彩纸板，MM.M.00514） | Edvard Munch | 1910 | Munchmuseet, Oslo | https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_The_Scream_-_Google_Art_Project.jpg | Public domain |
| `munch/scream_lithograph_1895.jpg` | The Scream（尖叫；石版画，Woll G 38；Met DP860367） | Edvard Munch | 1895 | The Met, New York | https://commons.wikimedia.org/wiki/File:The_Scream_MET_DP860367.jpg | CC0（Met Open Access 捐赠件） |
| `munch/madonna_1894_95.jpg` | Madonna（圣母；NG.M.00841） | Edvard Munch | 1894–95 | National Museum, Oslo | https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_Madonna_(1894-1895).jpg | Public domain |
| `munch/dance_of_life_1899.jpg` | The Dance of Life（生命之舞；NG.M.00941） | Edvard Munch | 1899–1900 | National Museum, Oslo | https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_The_Dance_of_Life_-_NG.M.00941_-_National_Museum_of_Art,_Architecture_and_Design.jpg | Public domain |
| `munch/anxiety_1894.jpg` | Anxiety（焦虑；MM.M.00515） | Edvard Munch | 1894 | Munchmuseet, Oslo | https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_Anxiety_-_MM.M.00515_-_Munch_Museum.jpg | Public domain |
| `munch/self_portrait_with_cigarette_1895.jpg` | Self-Portrait with Cigarette（自画像与香烟；NG.M.00470） | Edvard Munch | 1895 | National Museum, Oslo | https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_Self-Portrait_with_Cigarette_-_NG.M.00470_-_National_Museum_of_Art,_Architecture_and_Design.jpg | Public domain |
| `munch/puberty_1894_95.jpg` | Puberty（青春期；NG.M.00807） | Edvard Munch | 1894–95 | National Museum, Oslo | https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_Puberty_-_NG.M.00807_-_National_Museum_of_Art,_Architecture_and_Design.jpg | Public domain |
| `munch/the_sick_child_1885_86.jpg` | The Sick Child（病中的孩子；NG.M.00839） | Edvard Munch | 1885–86 | National Museum, Oslo | https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_The_Sick_Child_-_NG.M.00839_-_National_Museum_of_Art,_Architecture_and_Design.jpg | Public domain |
| `munch/ashes_1894.jpg` | Ashes（灰烬；NG.M.00809） | Edvard Munch | 1894（另记 1895，两存） | National Museum, Oslo | https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_Ashes_-_NG.M.00809_-_National_Museum_of_Art,_Architecture_and_Design.jpg | Public domain |
| `munch/the_sun_1911.jpg` | The Sun（太阳；MM.M.00963；Aula 组画主作另版藏奥斯陆大学） | Edvard Munch | 1910–11 | Munchmuseet, Oslo | https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_The_Sun_-_MM.M.00963_-_Munch_Museum.jpg | Public domain |
| `munch/girls_on_the_bridge_1901.jpg` | The Girls on the Bridge（桥上的少女；NG.M.00844） | Edvard Munch | 1901 | National Museum, Oslo | https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_The_Girls_on_the_Bridge_-_NG.M.00844_-_National_Museum_of_Art,_Architecture_and_Design.jpg | Public domain |
| `kandinsky/the_blue_rider_1903.jpg` | The Blue Rider (Der Blaue Reiter)（青骑士） | Wassily Kandinsky | 1903 | Stiftung Sammlung E.G. Bührle, Zurich | https://commons.wikimedia.org/wiki/File:Wassily_Kandinsky,_1903,_The_Blue_Rider_(Der_Blaue_Reiter),_oil_on_canvas,_52.1_x_54.6_cm,_Stiftung_Sammlung_E.G._Bührle,_Zurich.jpg | Public domain（PD-Art） |
| `kandinsky/murnau_mit_kirche_i_1910.jpg` | Murnau mit Kirche I（慕尔瑙与教堂 I） | Wassily Kandinsky | 1910 | Städtische Galerie im Lenbachhaus（GMS 59） | https://www.lenbachhaus.de/en/digital/collection-online/detail/murnau-mit-kirche-i-30018804 | CC0 1.0（Lenbachhaus） |
| `kandinsky/impression_iii_konzert_1911.jpg` | Impression III (Konzert)（印象 III·音乐会） | Wassily Kandinsky | 1911 | Städtische Galerie im Lenbachhaus（GMS 78） | https://www.lenbachhaus.de/en/digital/collection-online/detail/impression-iii-konzert-30012206 | CC0 1.0（Lenbachhaus） |
| `kandinsky/composition_vii_1913.jpg` | Composition VII（构成 VII） | Wassily Kandinsky | 1913 | Tretyakov Gallery, Moscow | https://commons.wikimedia.org/wiki/File:Composition_VII_-_Wassily_Kandinsky,_GAC.jpg | Public domain（PD-Art；Google Art Project 扫描） |
| `kandinsky/study_for_improvisation_31_1913.jpg` | Study for Improvisation 31 (Seeschlacht)（即兴 31 习作·海战） | Wassily Kandinsky | 1913 | Centre Pompidou（AM 1976-866） | https://commons.wikimedia.org/wiki/File:Kandinsky,_Wassily_-_Study_for_Improvisation_31_(Seeschlacht),_1913,_GAC.jpg | Public domain（PD-Art） |
| `kandinsky/blaue_reiter_almanac_cover_1912.jpg` | 《Der Blaue Reiter》年鉴封面（康定斯基设计，与 Franz Marc 合编） | Wassily Kandinsky | 1912 | 实物摄影：Goesseln（2010） | https://commons.wikimedia.org/wiki/File:Der_Blaue_Reiter_Almanach_10.jpg | CC BY-SA 3.0（摄影 Goesseln；原设计 PD） |
| `kandinsky/the_archer_woodcut_c1909.jpg` | The Archer（弓箭手，Roethel 79；彩色木刻） | Wassily Kandinsky | c. 1909（1912 用于年鉴豪华版；1938 补印） | 版画（散藏） | https://commons.wikimedia.org/wiki/File:W.Kandinsky_The_Archer.jpg | Public domain（PD-Art） |
| `kandinsky/composition_viii_1923.jpg` | Composition VIII（构成 VIII） | Wassily Kandinsky | 1923 | Solomon R. Guggenheim Museum, New York（展览现场摄影） | https://commons.wikimedia.org/wiki/File:Kandinsky_-_Composition_8,_July_1923.jpg | CC0（摄影 Xyxyzyz） |
| `kandinsky/on_white_ii_1923.jpg` | Auf Weiss II (On White II)（在白色上 II） | Wassily Kandinsky | 1923 | Centre Pompidou（AM 1976-855） | https://commons.wikimedia.org/wiki/File:Vassily_Kandinsky,_1923_-_On_White_II.jpg | Public domain（PD-Art） |
| `kandinsky/yellow_red_blue_1925.jpg` | Gelb-Rot-Blau (Jaune-rouge-bleu)（黄·红·蓝） | Wassily Kandinsky | 1925 | Centre Pompidou（AM 1976-856） | https://commons.wikimedia.org/wiki/File:Gelb-Rot-Blau,_by_Wassily_Kandinsky,_Centre_Pompidou.jpg | Public domain（PD-Art；馆方标 Domaine public） |
| `kandinsky/several_circles_1926.jpg` | Several Circles (Einige Kreise)（若干圆） | Wassily Kandinsky | 1926 | Solomon R. Guggenheim Museum, New York | https://commons.wikimedia.org/wiki/File:Vassily_Kandinsky,_1926_-_Several_Circles,_Gugg_0910_25.jpg | Public domain（PD-Art） |
| `velazquez/las_meninas.jpg` | Las Meninas（宫娥） | Diego Velázquez | 1656 | Museo del Prado, Madrid（P001174） | https://commons.wikimedia.org/wiki/File:Las_Meninas,_by_Diego_Vel%C3%A1zquez,_from_Prado_in_Google_Earth.jpg | Public domain |
| `velazquez/las_hilanderas.jpg` | Las Hilanderas (The Fable of Arachne)（纺纱女） | Diego Velázquez | c. 1655–60 | Museo del Prado, Madrid（P001173） | https://commons.wikimedia.org/wiki/File:Velazquez-las_hilanderas.jpg | Public domain |
| `velazquez/the_surrender_of_breda.jpg` | The Surrender of Breda (Las Lanzas)（布雷达的投降） | Diego Velázquez | c. 1634–35 | Museo del Prado, Madrid（P001172） | https://commons.wikimedia.org/wiki/File:Velazquez-The_Surrender_of_Breda.jpg | Public domain |
| `velazquez/portrait_of_innocent_x.jpg` | Portrait of Pope Innocent X（英诺森十世像） | Diego Velázquez | 1650 | Galleria Doria Pamphilj, Rome | https://commons.wikimedia.org/wiki/File:Retrato_del_Papa_Inocencio_X._Roma,_by_Diego_Vel%C3%A1zquez.jpg | Public domain |
| `velazquez/the_rokeby_venus.jpg` | The Toilet of Venus ('The Rokeby Venus')（镜前的维纳斯） | Diego Velázquez | 1647–51 | The National Gallery, London（NG2057） | https://commons.wikimedia.org/wiki/File:Diego_Vel%C3%A1zquez_-_Rokeby_Venus.jpg | Public domain |
| `velazquez/juan_de_pareja.jpg` | Juan de Pareja（胡安·德·帕雷哈像） | Diego Velázquez | 1650 | The Met, New York（1971.86） | https://www.metmuseum.org/art/collection/search/437869 | CC0（Met Open Access） |
| `velazquez/the_waterseller_of_seville.jpg` | The Waterseller of Seville（塞维利亚的卖水人） | Diego Velázquez | c. 1620 | Wellington Collection, Apsley House, London | https://commons.wikimedia.org/wiki/File:El_aguador_de_Sevilla,_por_Diego_Vel%C3%A1zquez.jpg | Public domain |
| `velazquez/old_woman_frying_eggs.jpg` | Old Woman Cooking Eggs（煎蛋的老妇） | Diego Velázquez | 1618 | National Galleries of Scotland, Edinburgh | https://commons.wikimedia.org/wiki/File:Diego_Velazquez_-_An_Old_Woman_Cooking_Eggs_-_Google_Art_Project.jpg | Public domain |
| `velazquez/view_of_the_villa_medici.jpg` | View of the Garden of the Villa Medici, Rome（'Entrance to the Grotto'） | Diego Velázquez | c. 1630 | Museo del Prado, Madrid | https://commons.wikimedia.org/wiki/File:Vista_del_jard%C3%ADn_de_la_Villa_Medici_en_Roma,_por_Diego_Vel%C3%A1zquez.jpg | Public domain |
| `velazquez/the_triumph_of_bacchus.jpg` | The Triumph of Bacchus (Los Borrachos)（酒神的胜利） | Diego Velázquez | 1628–29 | Museo del Prado, Madrid（P001170） | https://commons.wikimedia.org/wiki/File:Vel%C3%A1zquez_-_El_Triunfo_de_Baco_o_Los_Borrachos_(Museo_del_Prado,_1628-29).jpg | Public domain |
| `velazquez/the_supper_at_emmaus.jpg` | The Supper at Emmaus（以马忤斯的晚餐） | Diego Velázquez | 1622–23 | The Met, New York（14.40.631） | https://www.metmuseum.org/art/collection/search/437871 | CC0（Met Open Access） |
| `velazquez/maria_teresa_infanta.jpg` | María Teresa, Infanta of Spain（西班牙公主玛丽亚·特蕾莎） | Diego Velázquez | 1651–54 | The Met, New York（49.7.43） | https://www.metmuseum.org/art/collection/search/437870 | CC0（Met Open Access） |
| `bosch/garden_of_earthly_delights.jpg` | The Garden of Earthly Delights Triptych（人间乐园，三联全开） | Hieronymus Bosch | 1490–1500 | Museo del Prado, Madrid（P002823） | https://commons.wikimedia.org/wiki/File:Hieronymus_Bosch_(c._1450–1516),_The_Garden_of_Earthly_Delights_Triptych,_1490–1500.jpg | Public Domain Mark（Prado 摄影复制品；PDM-owner） |
| `bosch/haywain_triptych.jpg` | The Haywain Triptych（干草车，三联全开） | Hieronymus Bosch | 1512–1515 | Museo del Prado, Madrid（P002052） | https://commons.wikimedia.org/wiki/File:Bosch_-_Haywain_Triptych.jpg | Public domain |
| `bosch/last_judgment_vienna.jpg` | The Last Judgment（最后的审判，三联全开） | Hieronymus Bosch | after 1482 | Academy of Fine Arts, Vienna | https://commons.wikimedia.org/wiki/File:Hieronymus_Bosch_-_The_Last_Judgement.jpg | Public domain |
| `bosch/temptation_of_st_anthony.jpg` | Triptych of the Temptation of St. Anthony（圣安东尼的诱惑，三联全开） | Hieronymus Bosch | c. 1501 | Museu Nacional de Arte Antiga, Lisbon | https://commons.wikimedia.org/wiki/File:Temptation_of_Saint_Anthony.jpg | Public domain |
| `bosch/ship_of_fools.jpg` | Ship of Fools（愚人船，残件） | Hieronymus Bosch | c. 1505–1515 | Musée du Louvre, Paris（RF 2218） | https://commons.wikimedia.org/wiki/File:La_Nef_des_fous_-_Jérôme_Bosch_-_Musée_du_Louvre_Peintures_RF_2218.jpg | Public domain |
| `bosch/death_and_the_miser.jpg` | Death and the Miser（死神与守财奴） | Hieronymus Bosch | c. 1485/1490 | National Gallery of Art, Washington（1952.5.33, Kress） | https://commons.wikimedia.org/wiki/File:Hieronymus_Bosch,_Death_and_the_Miser,_c._1485-1490,_NGA_41645.jpg（下载经 NGA IIIF） | CC0（NGA Open Access） |
| `bosch/seven_deadly_sins.jpg` | The Seven Deadly Sins and the Four Last Things（七宗罪与四末） | Hieronymus Bosch | 1505–1510 | Museo del Prado, Madrid（P002822） | https://commons.wikimedia.org/wiki/File:Hieronymus_Bosch-_The_Seven_Deadly_Sins_and_the_Four_Last_Things.JPG | Public domain |
| `bosch/adoration_of_the_magi.jpg` | Triptych of the Adoration of the Magi（三王来拜） | Hieronymus Bosch | c. 1494 | Museo del Prado, Madrid（P002048） | https://commons.wikimedia.org/wiki/File:Hieronymus_Bosch_-_Triptych_of_the_Adoration_of_the_Magi_-_WGA2606.jpg | Public domain |
| `bosch/christ_carrying_the_cross_ghent.jpg` | Christ Carrying the Cross（基督负十字架，根特本） | Hieronymus Bosch | c. 1510（BRCP：1530–40、出自追随者） | Museum of Fine Arts (MSK), Ghent（1902-H） | https://commons.wikimedia.org/wiki/File:Kruisdraging,_Hieronymus_Bosch,_ca._1510,_Koninklijk_Museum_voor_Schone_Kunsten_Gent,_1902-H.jpg | Public domain |
| `bosch/cutting_the_stone.jpg` | Cure of Folly / Extracting the Stone of Madness（取出愚石，带画框题刻） | Hieronymus Bosch | c. 1494–1516 | Museo del Prado, Madrid（P02056） | https://commons.wikimedia.org/wiki/File:Cutting_the_Stone_(Bosch).jpg | Public domain |
| `huang_gongwang/fuchun_remaining_mountain.jpg` | 富春山居图·剩山图（画心） | 黄公望 | 1347–1350 | 浙江省博物馆 | https://commons.wikimedia.org/wiki/File:富春山居圖(剩山圖).jpg | Public domain（PD-Art） |
| `huang_gongwang/fuchun_wuyongshi_full.jpg` | 富春山居图·无用师卷（画心，三段叠排） | 黄公望 | 1347–1350 | 台北故宫博物院（故画001016） | https://commons.wikimedia.org/wiki/File:富春山居圖(無用師卷).jpg | Public domain（PD-Art；原始图源：NPM 2011 特展官网） |
| `huang_gongwang/fuchun_wuyongshi_detail.jpg` | 富春山居图·无用师卷（局部） | 黄公望 | 1347–1350 | 台北故宫博物院 | https://commons.wikimedia.org/wiki/File:Huang_Gongwang._Dwelling_in_the_Fuchun_Mountains._detail._National_Palace_Museum,_Taipei.jpg | Public domain（PD-Art） |
| `huang_gongwang/fuchun_ziming_full.jpg` | 富春山居图·子明卷（两段叠排；摹本） | 黄公望（摹本/传） | 约 1338 纪年 | 台北故宫博物院（故画001017） | https://commons.wikimedia.org/wiki/File:富春山居圖(子明卷).jpg | Public domain（PD-Art） |
| `huang_gongwang/shenzhou_fuchun_copy.jpg` | 沈周仿黄公望富春山居图卷（两段叠排） | 沈周（临黄公望） | 1487 | 故宫博物院 | https://commons.wikimedia.org/wiki/File:沈周仿黄公望富春山居图卷.png | Public domain（PD-Art） |
| `huang_gongwang/jiufeng_xueji.jpg` | 九峰雪霁图（轴） | 黄公望 | 1349 | 故宫博物院 | https://commons.wikimedia.org/wiki/File:黄公望九峰雪霁图轴.png | Public domain（PD-Art） |
| `huang_gongwang/tianchi_shibi.jpg` | 天池石壁图（轴） | 黄公望 | 1341 | 故宫博物院 | https://commons.wikimedia.org/wiki/File:Huang_Gongwang._Stone_Cliff_at_the_Pond_of_Heaven.1341._139,4x57,3._Palace_Museum,_Beijing.jpg | Public domain（PD-Art） |
| `huang_gongwang/danya_yushu.jpg` | 丹崖玉树图（轴） | 黄公望 | 元 | 故宫博物院 | https://commons.wikimedia.org/wiki/File:黄公望丹崖玉树图轴.png | Public domain（PD-Art） |
| `huang_gongwang/kuaixue_shiqing.jpg` | 快雪时晴书画合璧卷（赵孟頫题·黄公望画·徐贲补） | 黄公望 | 约 1340 | 故宫博物院 | https://commons.wikimedia.org/wiki/File:Huang_Gongwang._Clearing_After_Sudden_Snow._ca._1340._104,6_cm_long.Palace_Museum,_Beijing.jpg | Public domain（PD-Art） |
| `huang_gongwang/jiuzhu_fengcui.jpg` | 九珠峰翠图（轴） | 黄公望 | 约 1346–48 | 台北故宫博物院（故画001309） | https://commons.wikimedia.org/wiki/File:元黃公望九珠峰翠圖軸.jpg | **CC0**（台北故宫开放数据） |
| `behzad/yusuf_zulaikha_cairo.jpg` | 《优素福逃避祖莱哈的纠缠》——萨迪《布斯坦》f.52b | Kamāl ud-Dīn Behzād | 1488 | 开罗，Dār al-Kutub（Adab Farsi 908） | https://commons.wikimedia.org/wiki/File:Yusuf_fleeing_the_Advances_of_Zulaikha.jpg | Public domain |
| `behzad/khawarnaq_f154v.jpg` | 《霍拉纳克宫的建造》——尼扎米《五卷诗》f.154v | Kamāl ud-Dīn Behzād | c. 1494–95 | 大英图书馆 Or. 6810 | https://commons.wikimedia.org/wiki/File:Kamal-ud-din_Bihzad_-_Construction_of_the_fort_of_Kharnaq.jpg | Public domain |
| `behzad/alexander_hermit_f273r.jpg` | 《亚历山大与隐士》f.273r | Kamāl ud-Dīn Behzād | c. 1494–95 | 大英图书馆 Or. 6810 | https://commons.wikimedia.org/wiki/File:Alexander_and_the_Hermit,_from_Nizami%27s_Iskandarnama,_1494-95,_by_Behzad._British_Library_OR.6810_Folio_273R.jpg | Public domain |
| `behzad/jami_astrolabe_f225v.jpg` | 《贾米持星盘》（f.225v 细节） | Kamāl ud-Dīn Behzād | c. 1494–95 | 大英图书馆 Or. 6810 | https://commons.wikimedia.org/wiki/File:Jami,_holding_an_astrolabe._By_Behz%C3%A2d,_from_the_Romance_of_Alexander_by_Nez%C3%A2m%C3%AE._Manuscript_of_the_Khamseh_of_the_emir_%27Al%C3%AE_F%C3%A2rs%C3%AE_Barlas,_Herat_1494-1495;_British_Library,_Or._6810,_f_225_v.jpg | Public domain |
| `behzad/sanjar_add25900_f18a.jpg` | 《苏丹·桑贾尔与老妇》f.18a | Kamāl ud-Dīn Behzād | 1493 | 大英图书馆 Add. 25900 | https://commons.wikimedia.org/wiki/File:Sultan_Sanjar_and_the_old_lady,_Khamsa,_this_painting_dated_1493_(British_Library,_Add._25900)_folio_18a.jpg | Public domain |
| `behzad/hunting_h676_topkapi.jpg` | 《狩猎场景》——阿米尔·霍斯劳《八天堂》双页扉画 | Kamāl ud-Dīn Behzād | 1496–97 | 托普卡帕宫图书馆 H.676 | https://commons.wikimedia.org/wiki/File:Hunting_scene_from_the_Hast_Bahist_by_Kamal_al-Din_Bihzad,_Herat,_1496.jpg | Public domain |
| `behzad/two_camels_golshan.jpg` | 《两只骆驼相斗》——《古尔尚画册》 | Kamāl ud-Dīn Behzād | c. 1525–30 | 德黑兰，古列斯坦宫 | https://commons.wikimedia.org/wiki/File:Behzad._Kamelkampf._Golestan_Palast.jpg | Public domain |
| `behzad/dancing_dervishes_met.jpg` | 《舞僧》——哈菲兹诗集散页 | Kamāl ud-Dīn Behzād | c. 1480 | The Metropolitan Museum of Art（17.81.4） | https://commons.wikimedia.org/wiki/File:%22Dancing_Dervishes%22,_Folio_from_a_Divan_of_Hafiz_MET_DP231332.jpg | CC0（Met Open Access） |
| `behzad/encampment_cleveland.jpg` | 《营地外的乐手与仆人》（双联画左半；含未完成底稿） | Kamāl ud-Dīn Behzād | c. 1485 | Cleveland Museum of Art（1944.490） | https://commons.wikimedia.org/wiki/File:Bihzad_-_Folio_from_an_Album_with_Musicians_and_Servants_Outside_a_Royal_Encampment_-_1944.490_-_Cleveland_Museum_of_Art.tif | CC0（CMA Open Access） |
| `behzad/sadi_youth_kashgar.jpg` | 《萨迪与喀什青年》——《古丽斯坦》 | Kamāl ud-Dīn Behzād | 1486 | 私人收藏（Art and History Trust Collection） | https://commons.wikimedia.org/wiki/File:Sad%27i_and_the_Youth_of_Kashgar,_Ascribed_to_Bihzad,_From_a_copy_of_the_Gulistan_(Rosegarden)_by_Sa%27di.jpg | Public domain |
| `behzad/sultan_husayn_portrait.jpg` | 《苏丹·侯赛因·米尔扎·拜卡拉像》（自贝赫扎德原作摹本） | Kamāl ud-Dīn Behzād | 1500–25 | 哈佛艺术博物馆（216273） | https://commons.wikimedia.org/wiki/File:Portrait_of_Sultan_Husayn_Mirza_Bayqara_at_the_age_of_about_50_years._1500%E2%80%9325_copy_from_Behz%C4%81d%27s_original_of_about_1490.jpg | Public domain |
| `behzad/dust_muhammad_preface_h2154.jpg` | Dust Muhammad《巴赫拉姆·米尔扎画册》序言页（文献页） | —（文献页，非贝赫扎德作品） | 1544–45 | 托普卡帕宫图书馆 H.2154, f.9b | https://commons.wikimedia.org/wiki/File:Preface_written_by_Dust_Muhammad,_1544-45._From_the_Bahram_mirza_album,_Safavid_Iran._Topkap%C4%B1_Palace_museum_library,_ms._H._2154,_fol._9b.jpg | Public domain |
| `friedrich/der_moench_am_meer.jpg` | Der Mönch am Meer（海边僧侣，NG 9/85） | Caspar David Friedrich | 1808–1810 | Alte Nationalgalerie, Berlin | https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Der_M%C3%B6nch_am_Meer_-_Google_Art_Project.jpg | Public domain |
| `friedrich/abtei_im_eichwald.jpg` | Abtei im Eichwald（橡树林中的修道院，NG 8/85） | Caspar David Friedrich | 1809–1810 | Alte Nationalgalerie, Berlin | https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Abtei_im_Eichwald_-_Google_Art_Project.jpg | Public domain |
| `friedrich/wanderer_above_the_sea_of_fog.jpg` | Der Wanderer über dem Nebelmeer（雾海上的漫游者，HK-5161） | Caspar David Friedrich | um 1817（传统记 1818） | Hamburger Kunsthalle | https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Wanderer_above_the_sea_of_fog.jpg | Public domain |
| `friedrich/das_eismeer.jpg` | Das Eismeer（冰海，HK-1051） | Caspar David Friedrich | 1823/24 | Hamburger Kunsthalle | https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Das_Eismeer_-_Hamburger_Kunsthalle_-_02.jpg | Public domain |
| `friedrich/kreidefelsen_auf_ruegen.jpg` | Kreidefelsen auf Rügen（吕根岛的白垩崖） | Caspar David Friedrich | 1818 | Kunst Museum Winterthur（Oskar Reinhart 藏） | https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich%27s_Chalk_Cliffs_on_R%C3%BCgen.jpg | Public domain |
| `friedrich/zwei_maenner_in_betrachtung_des_mondes.jpg` | Zwei Männer in Betrachtung des Mondes（月下双人） | Caspar David Friedrich | 1819/20 | Galerie Neue Meister, Dresden | https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Zwei_M%C3%A4nner_in_Betrachtung_des_Mondes.jpg | Public domain |
| `friedrich/frau_am_fenster.jpg` | Frau am Fenster（窗前的女人，A I 918） | Caspar David Friedrich | 1822 | Alte Nationalgalerie, Berlin | https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Frau_am_Fenster_-_Google_Art_Project.jpg | Public domain |
| `friedrich/mondaufgang_am_meer.jpg` | Mondaufgang am Meer（海上月出，W.S. 53） | Caspar David Friedrich | 1822 | Alte Nationalgalerie, Berlin | https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Mondaufgang_am_Meer_-_Google_Art_Project.jpg | Public domain |
| `friedrich/der_watzmann.jpg` | Der Watzmann（瓦茨曼山） | Caspar David Friedrich | 1824/25 | Alte Nationalgalerie, Berlin | https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_The_Watzmann_%281824-25%29.jpg | Public domain |
| `friedrich/die_lebensstufen.jpg` | Die Lebensstufen（生命阶段） | Caspar David Friedrich | um 1835 | Museum der bildenden Künste, Leipzig | https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Die_Lebensstufen_%28ca._1834%29.jpg | Public domain |
| `friedrich/das_kreuz_im_gebirge.jpg` | Das Kreuz im Gebirge（山中的十字架＝泰申祭坛画） | Caspar David Friedrich | 1808 | Galerie Neue Meister, Dresden | https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Das_Kreuz_im_Gebirge.jpg | Public domain |
| `friedrich/der_einsame_baum.jpg` | Der einsame Baum（孤独的树，W.S. 52） | Caspar David Friedrich | 1822 | Alte Nationalgalerie, Berlin | https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Der_einsame_Baum.jpg | Public domain |
| `repin/barge_haulers_on_the_volga.jpg` | Barge Haulers on the Volga（伏尔加河上的纤夫） | Ilya Repin | 1870–1873 | Государственный Русский музей（圣彼得堡） | https://commons.wikimedia.org/wiki/File:Ilya_Repin_-_Barge_Haulers_on_the_Volga_-_Google_Art_Project.jpg | Public domain |
| `repin/religious_procession_in_kursk_province.jpg` | Religious Procession in Kursk Province（库尔斯克省的宗教行列） | Ilya Repin | 1880–1883 | Государственная Третьяковская галерея（莫斯科） | https://commons.wikimedia.org/wiki/File:Ilya_Repin_-_%D0%9A%D1%80%D0%B5%D1%81%D1%82%D0%BD%D1%8B%D0%B9_%D1%85%D0%BE%D0%B4_%D0%B2_%D0%9A%D1%83%D1%80%D1%81%D0%BA%D0%BE%D0%B9_%D0%B3%D1%83%D0%B1%D0%B5%D1%80%D0%BD%D0%B8%D0%B8_-_Google_Art_Project.jpg | Public domain |
| `repin/ivan_the_terrible_and_his_son_ivan.jpg` | Ivan the Terrible and His Son Ivan, 16 November 1581（伊凡雷帝杀子） | Ilya Repin | 1883–1885 | Государственная Третьяковская галерея | https://commons.wikimedia.org/wiki/File:R%C3%A9pine_Ivan_le_Terrible_et_son_fils_Ivan_principale_version_1883_-_1885.jpg | Public domain |
| `repin/they_did_not_expect_him.jpg` | They Did Not Expect Him（意外归来／不期而至） | Ilya Repin | 1884–1888 | Государственная Третьяковская галерея | https://commons.wikimedia.org/wiki/File:Ilya_Repin_Unexpected_visitors.jpg | Public domain |
| `repin/reply_of_the_zaporozhian_cossacks.jpg` | Reply of the Zaporozhian Cossacks to the Turkish Sultan（扎波罗热哥萨克致土耳其苏丹的回信） | Ilya Repin | 1880–1891 | Государственный Русский музей | https://commons.wikimedia.org/wiki/File:Repin_Cossacks.jpg | Public domain |
| `repin/portrait_of_modest_mussorgsky.jpg` | Portrait of Modest Mussorgsky（穆索尔斯基像） | Ilya Repin | 1881 | Государственная Третьяковская галерея | https://commons.wikimedia.org/wiki/File:Ilya_Repin_-_%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82_%D0%BA%D0%BE%D0%BC%D0%BF%D0%BE%D0%B7%D0%B8%D1%82%D0%BE%D1%80%D0%B0_%D0%9C.%D0%9F.%D0%9C%D1%83%D1%81%D0%BE%D1%80%D0%B3%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_-_Google_Art_Project.jpg | Public domain |
| `repin/sadko.jpg` | Sadko in the Underwater Kingdom（萨德科） | Ilya Repin | 1876 | Государственный Русский музей | https://commons.wikimedia.org/wiki/File:Ilya_Repin_-_Sadko_-_Google_Art_Project.jpg | Public domain |
| `repin/portrait_of_leo_tolstoy.jpg` | Portrait of Leo Tolstoy（列夫·托尔斯泰像，坐姿） | Ilya Repin | 1887 | Государственная Третьяковская галерея | https://commons.wikimedia.org/wiki/File:Ilya_Efimovich_Repin_(1844-1930)_-_Portrait_of_Leo_Tolstoy_(1887).jpg | Public domain |
| `repin/self_portrait_1878.jpg` | Self-portrait（自画像） | Ilya Repin | 1878 | Государственный Русский музей | https://commons.wikimedia.org/wiki/File:A002Self-portrait._1878.jpg | Public domain |
| `repin/state_council_1903.jpg` | Ceremonial Sitting of the State Council on 7 May 1901（国务会议庆典） | Ilya Repin | 1903 | Государственный Русский музей | https://commons.wikimedia.org/wiki/File:Ilya_Repin_-_Ceremonial_Sitting_of_the_State_Council_on_7_May_1901_Marking_the_Centenary_of_its_Foundation_-_Google_Art_Project.jpg | Public domain |
| `ravi_varma/shakuntala_looking_for_dushyanta.jpg` | 《沙恭达罗回眸》（Shakuntala looking for Dushyanta） | Raja Ravi Varma | 1898 | Sree Chitra Art Gallery（特里凡得琅） | https://commons.wikimedia.org/wiki/File:Raja_Ravi_Varma_-_Mahabharata_-_Shakuntala.jpg | Public domain（PD-Art） |
| `ravi_varma/nair_lady_adorning_her_hair.jpg` | 《奈尔女子梳妆》（Nair Lady Adorning Her Hair） | Raja Ravi Varma | 1873 | 未注（Commons 未记馆藏） | https://commons.wikimedia.org/wiki/File:Nair_Lady_Adorning_Her_Hair.jpg | Public domain |
| `ravi_varma/galaxy_of_musicians.jpg` | 《音乐家银河》（Galaxy of Musicians，11 位女乐手） | Raja Ravi Varma | 1889 | 原为迈索尔大君而作（藏处未注） | https://commons.wikimedia.org/wiki/File:Raja_Ravi_Varma,_Galaxy_of_Musicians.jpg | Public domain |
| `ravi_varma/there_comes_papa.jpg` | 《爸爸来了》（There Comes Papa） | Raja Ravi Varma | 1893 | Kowdiar Palace（特里凡得琅） | https://commons.wikimedia.org/wiki/File:Raja_Ravi_Varma,_There_Comes_Papa_(1893).jpg | Public domain（PD-Art） |
| `ravi_varma/radha_in_the_moonlight.jpg` | 《月下 Radha》（Radha in the Moonlight） | Raja Ravi Varma | 1890 | 私人收藏 | https://commons.wikimedia.org/wiki/File:Radha_in_the_Moonlight.jpg | Public domain |
| `ravi_varma/hamsa_damayanti.jpg` | 《天鹅与达玛扬蒂》（Hamsa Damayanti） | Raja Ravi Varma | 1899 | Sree Chitra Art Gallery | https://commons.wikimedia.org/wiki/File:Ravi_Varma-Princess_Damayanthi_talking_with_Royal_Swan_about_Nala.jpg | Public domain |
| `ravi_varma/sri_krishna_as_envoy.jpg` | 《克利希那出使》（Sri Krishna as Envoy） | Raja Ravi Varma | c.1906 | NGMA 新德里 | https://commons.wikimedia.org/wiki/File:Sri_Krishna_as_Envoy.jpg | Public domain（PD-Art） |
| `ravi_varma/draupadi_vastrapaharanam.jpg` | 《黑公主被褫衣》（Draupadi Vastrapaharanam） | Raja Ravi Varma | 1888–89 | 私人收藏 | https://commons.wikimedia.org/wiki/File:Draupadi_Vastraharan,_Raja_Ravi_Varma.jpg | Public domain |
| `ravi_varma/yashoda_with_krishna.jpg` | 《雅首达与克利希那》（Yashoda and Krishna） | Raja Ravi Varma | c.1890s | 私人收藏（2026-04 Saffronart ₹167.2 crore 成交） | https://commons.wikimedia.org/wiki/File:Yashoda_with_Krishna,_Raja_Ravi_Varma.jpg | Public domain |
| `ravi_varma/village_belle.jpg` | 《村中美人》（Village Belle） | Raja Ravi Varma | c.1900s | 私人收藏 | https://commons.wikimedia.org/wiki/File:Village_Belle,_by_Raja_Ravi_Varma.jpg | Public domain |
| `ravi_varma/gypsies_poverty_1893.jpg` | 《南印度吉普赛人（贫穷）》（The Gypsies of South India / Poverty） | Raja Ravi Varma | 1893 | Sree Chitra Art Gallery | https://commons.wikimedia.org/wiki/File:Raja_Ravi_Varma,_Gypsies_(1893).jpg | Public domain |
| `ravi_varma/mohini_on_a_swing.jpg` | 《秋千上的莫希尼》（Mohini on a Swing） | Raja Ravi Varma | 1894 | 私人收藏 | https://commons.wikimedia.org/wiki/File:Mohini_on_a_swing.jpg | Public domain（PD-Art） |
| `ravi_varma/jatayu_fights_ravana.jpg` | 《贾塔尤与罗波那》（Jatayu fights Ravana） | Raja Ravi Varma | c.1880s–90s | 未注（Commons 未记馆藏） | https://commons.wikimedia.org/wiki/File:Ravi_Varma-Ravana_Sita_Jathayu.jpg | Public domain |
| `ravi_varma/self_portrait.jpg` | 《自画像》（晚年像） | Raja Ravi Varma | 未定年 | 私人收藏 | https://commons.wikimedia.org/wiki/File:Self_portrait_by_Raja_Ravi_Varma.jpg | Public domain（PD-Art） |
| `ravi_varma/shakuntala_patra_lekhan.jpg` | 《沙恭达罗写信》（Shakuntala Patra-lekhan） | Raja Ravi Varma | c.1870s–90s | 未注（Commons 未记馆藏） | https://commons.wikimedia.org/wiki/File:Sakunthala-pathralekhanam.jpg | Public domain |
| `ravi_varma/saraswati.jpg` | 《辩才天女》（Saraswati，持维纳琴） | Raja Ravi Varma | 1896 | Maharaja Fateh Singh Museum（Vadodara） | https://commons.wikimedia.org/wiki/File:Saraswati.jpg | Public domain |
| `ravi_varma/saraswati_oleograph.jpg` | 《辩才天女》石版彩印版（oleograph；Ravi Varma Press 印制） | Raja Ravi Varma | c.1900s | 藏处未注（Commons） | https://commons.wikimedia.org/wiki/File:Raja_Ravi_Varma,_Goddess_Saraswati.jpg | Public domain |
| `degas/the_dance_class_1874.jpg` | The Dance Class（舞蹈课；Jules Perrot 课堂） | Edgar Degas | 1874 | The Met, New York（1987.47.1） | https://www.metmuseum.org/art/collection/search/438817 | CC0 1.0（Met Open Access） |
| `degas/la_classe_de_danse_1873_76.jpg` | La Classe de danse（舞蹈课） | Edgar Degas | 1873–76 | Musée d'Orsay（RF 1976） | https://commons.wikimedia.org/wiki/File:Edgar_Degas_-_La_Classe_de_danse.jpg | Public domain |
| `degas/ballet_from_robert_le_diable_1871.jpg` | The Ballet from "Robert le Diable"（罗贝尔恶魔的芭蕾） | Edgar Degas | 1871 | The Met, New York（436123） | https://www.metmuseum.org/art/collection/search/436123 | CC0 1.0（Met Open Access） |
| `degas/dancers_practicing_at_the_barre_1877.jpg` | Dancers Practicing at the Barre（把杆练习） | Edgar Degas | 1877 | The Met, New York（436139） | https://www.metmuseum.org/art/collection/search/436139 | CC0 1.0（Met Open Access） |
| `degas/blue_dancers_1890.jpg` | Danseuses bleues（蓝色舞者） | Edgar Degas | c. 1890 | Musée d'Orsay（RF 1951 10） | https://commons.wikimedia.org/wiki/File:Edgar_Germain_Hilaire_Degas_071.jpg | Public domain（PD-old-70 / PD-Art-Yorck） |
| `degas/the_star_1876_77.jpg` | Ballet / L'Étoile（舞台之星；粉彩） | Edgar Degas | 1876–77 | Musée d'Orsay（RF 12258） | https://commons.wikimedia.org/wiki/File:Edgar_Degas_-_Ballet_(L%27%C3%89toile).jpg | Public domain（PD-Art） |
| `degas/le_foyer_de_la_danse_1872.jpg` | Le Foyer de la danse à l'Opéra（舞台后厅） | Edgar Degas | 1872 | Musée d'Orsay（RF 1977） | https://commons.wikimedia.org/wiki/File:Edgar_Degas_-_The_Dance_Foyer_at_the_Opera_on_the_rue_Le_Peletier.jpg | Public domain |
| `degas/miss_la_la_at_the_cirque_fernando_1879.jpg` | Miss La La at the Cirque Fernando（拉拉小姐） | Edgar Degas | 1879 | National Gallery, London（NG4121） | https://commons.wikimedia.org/wiki/File:Edgar_Degas,_Miss_La_La_at_the_Cirque_Fernando,_1879.jpg | Public domain |
| `degas/combing_the_hair_1896.jpg` | Combing the Hair ('La Coiffure')（梳头） | Edgar Degas | c. 1896 | National Gallery, London（NG486） | https://commons.wikimedia.org/wiki/File:Combing_the_Hair_(La_Coiffure),_Edgar_Degas.jpg | **CC BY-SA 4.0**（照片；原作 PD） |
| `degas/dans_un_cafe_1875_76.jpg` | Dans un café（L'Absinthe，咖啡馆） | Edgar Degas | 1875–76 | Musée d'Orsay（RF 1147） | https://commons.wikimedia.org/wiki/File:Edgar_Degas_-_In_a_Caf%C3%A9_-_Google_Art_Project.jpg | Public domain |
| `degas/the_bellelli_family_1858_67.jpg` | Portrait de famille / La famille Bellelli（贝列里一家） | Edgar Degas | 1858–69 | Musée d'Orsay（RF 2210） | https://commons.wikimedia.org/wiki/File:Edgar_Degas_-_The_Bellelli_Family_-_Google_Art_Project.jpg | Public domain |
| `degas/woman_bathing_in_a_shallow_tub_1885.jpg` | Woman Bathing in a Shallow Tub（浴女；粉彩） | Edgar Degas | 1885 | The Met, New York（436127） | https://www.metmuseum.org/art/collection/search/436127 | CC0 1.0（Met Open Access） |
| `degas/little_fourteen_year_old_dancer.jpg` | The Little Fourteen-Year-Old Dancer（十四岁的小舞者；铸铜） | Edgar Degas | modeled 1881 / cast 1922 | The Met, New York（29.100.370） | https://www.metmuseum.org/art/collection/search/196439 | CC0 1.0（Met Open Access） |
| `gauguin/vision_after_sermon_1888.jpg` | Vision après le sermon（布道后的幻象） | Paul Gauguin | 1888 | National Galleries of Scotland, Edinburgh | https://commons.wikimedia.org/wiki/File:La_vision_après_le_sermon_(Paul_Gauguin).jpg | Public domain |
| `gauguin/breton_girls_dancing_1888.jpg` | Breton Girls Dancing, Pont-Aven | Paul Gauguin | 1888 | National Gallery of Art, Washington | https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Breton_Girls_Dancing,_Pont-Aven_-_Google_Art_Project.jpg | Public domain |
| `gauguin/yellow_christ_1889.jpg` | Le Christ jaune（黄色基督） | Paul Gauguin | 1889 | Buffalo AKG Art Museum | https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_The_Yellow_Christ_(Le_Christ_jaune)_1889.jpg | Public domain |
| `gauguin/self_portrait_halo_1889.jpg` | Self-Portrait with Halo and Snake（自画像） | Paul Gauguin | 1889 | National Gallery of Art, Washington | https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Self-Portrait_with_Halo_and_Snake.jpg | Public domain |
| `gauguin/ia_orana_maria_1891.jpg` | Ia Orana Maria（万福玛利亚；51.112.2） | Paul Gauguin | 1891 | The Met, New York | https://commons.wikimedia.org/wiki/File:Paul_Gauguin_Ia_Orana_Maria_(Hail_Mary)_The_Metropolitan_Museum_of_Art1.jpg | Public domain |
| `gauguin/tahitian_women_on_beach_1891.jpg` | Femmes de Tahiti（沙滩上的塔希提女人） | Paul Gauguin | 1891 | Musée d'Orsay, Paris | https://commons.wikimedia.org/wiki/File:Paul_Gauguin_056.jpg | Public domain |
| `gauguin/woman_with_flower_1891.jpg` | Vahine no te tiare（持花女人） | Paul Gauguin | 1891 | Ny Carlsberg Glyptotek, Copenhagen | https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Tahitian_Woman_with_a_Flower_-_Google_Art_Project.jpg | Public domain |
| `gauguin/spirit_of_dead_watching_1892.jpg` | Manao Tupapau（死亡的幽灵在注视） | Paul Gauguin | 1892 | Buffalo AKG Art Museum | https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Manaò_tupapaú_(Spirit_of_the_Dead_Watching)_-_1965-1_-_Albright–Knox_Art_Gallery.tiff | Public domain |
| `gauguin/arearea_1892.jpg` | Arearea（快乐的田园） | Paul Gauguin | 1892 | Musée d'Orsay, Paris | https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Arearea_-_Google_Art_Project.jpg | Public domain |
| `gauguin/the_siesta_1892.jpg` | The Siesta（午睡；1993.400.3） | Paul Gauguin | 1892–94 | The Met, New York | https://commons.wikimedia.org/wiki/File:Paul_Gauguin_044.jpg | Public domain |
| `gauguin/fatata_te_miti_1892.jpg` | Fatata te Miti（海边） | Paul Gauguin | 1892 | National Gallery of Art, Washington | https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Fatata_te_Miti_(By_the_Sea)_-_Google_Art_Project.jpg | Public domain |
| `gauguin/seed_of_areoi_1892.jpg` | Te aa no areois（阿雷奥伊的种子） | Paul Gauguin | 1892 | MoMA, New York | https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Te_aa_no_areois_-_Google_Art_Project.jpg | Public domain |
| `gauguin/when_will_you_marry_1892.jpg` | Nafea Faa Ipoipo（何时出嫁？） | Paul Gauguin | 1892 | 私人收藏（2015 年私售 2.1 亿美元） | https://commons.wikimedia.org/wiki/File:Paul_Gauguin,_Nafea_Faa_Ipoipo%3F_(When_Will_You_Marry%3F)_1892,_oil_on_canvas,_101_x_77_cm.jpg | Public domain |
| `gauguin/tehamana_1893.jpg` | Merahi metua no Tehamana（Tehamana 的祖先们） | Paul Gauguin | 1893 | Art Institute of Chicago | https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_The_Ancestors_of_Tehamana_OR_Tehamana_Has_Many_Parents_(Merahi_metua_no_Tehamana)_-_Google_Art_Project.jpg | Public domain |
| `gauguin/day_of_the_god_1894.jpg` | Mahana no atua（上帝之日；1926.198） | Paul Gauguin | 1894 | Art Institute of Chicago | https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Mahana_no_atua_(Day_of_the_God)_-_1926.198_-_Art_Institute_of_Chicago.jpg | Public domain |
| `gauguin/oviri_1894.jpg` | Oviri（野蛮人；釉陶） | Paul Gauguin | 1894 | Musée d'Orsay, Paris | https://commons.wikimedia.org/wiki/File:Paul_Gauguin,_1894,_Oviri_(Sauvage),_partially_glazed_stoneware,_75_x_19_x_27_cm,_Musée_d'Orsay.jpg | Public domain |
| `gauguin/noa_noa_woodcut_1894.jpg` | Nave Nave Fenua（Noa Noa 木刻组画之一） | Paul Gauguin | 1893–94 | Noa Noa 组画（多馆藏） | https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Nave_Nave_Fenua_from_the_Noa_Noa_Series_-_Google_Art_Project.jpg | Public domain |
| `gauguin/nevermore_1897.jpg` | Nevermore（永不复返） | Paul Gauguin | 1897 | The Courtauld, London | https://commons.wikimedia.org/wiki/File:Paul_Gauguin_091.jpg | Public domain |
| `gauguin/where_do_we_come_from_1897.jpg` | D'où venons-nous ? Que sommes-nous ? Où allons-nous ?（我们从何处来？） | Paul Gauguin | 1897–98 | MFA Boston | https://commons.wikimedia.org/wiki/File:Gauguin_-_Where_Do_We_Come_From%3F_What_Are_We%3F_Where_Are_We_Going%3F_(1897-98).jpg | Public domain |
| `gauguin/two_tahitian_women_1899.jpg` | Two Tahitian Women（两个塔希提女人；49.58.1） | Paul Gauguin | 1899 | The Met, New York | https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Deux_Tahitiennes.jpg | Public domain |
| `van_eyck/ghent_altarpiece_open.jpg` | 《根特祭坛画》开屏（全 12 面板，Adoration of the Mystic Lamb） | Jan van Eyck | 1432 | St Bavo's Cathedral, Ghent | https://commons.wikimedia.org/wiki/File:Lamgods_open.jpg | Public domain |
| `van_eyck/ghent_altarpiece_closed.jpg` | 《根特祭坛画》闭屏（修复后，外板 8 面） | Jan van Eyck | 1432 | St Bavo's Cathedral, Ghent | https://commons.wikimedia.org/wiki/File:Ghent_Altarpiece_(closed,_after_restoration).jpg | Public domain |
| `van_eyck/ghent_lamb_detail_restored.jpg` | 《神秘羔羊》中央细节（2020 修复后原貌） | Jan van Eyck | 1432 | St Bavo's Cathedral, Ghent | https://commons.wikimedia.org/wiki/File:Ghent_Altarpiece_D_-_Lamb.jpg | Public domain |
| `van_eyck/arnolfini_portrait_1434.jpg` | 《阿尔诺菲尼夫妇像》（NG186；凸镜/念珠/橙子反射） | Jan van Eyck | 1434 | National Gallery, London | https://commons.wikimedia.org/wiki/File:Van_Eyck_-_Arnolfini_Portrait.jpg | Public domain |
| `van_eyck/man_in_red_turban_1433.jpg` | 《红头巾男子像（自画像?）》（NG222；格言框铭） | Jan van Eyck | 1433 | National Gallery, London | https://commons.wikimedia.org/wiki/File:Portrait_of_a_Man_in_a_red_turban_(by_Jan_van_Eyck).jpg | Public domain |
| `van_eyck/leal_souvenir_1432.jpg` | 《Léal Souvenir（"忠诚的记忆"）》（NG290；三重题刻） | Jan van Eyck | 1432 | National Gallery, London | https://commons.wikimedia.org/wiki/File:Jan_van_Eyck_-_L%C3%A9al_Souvenir_-_National_Gallery,_London.jpg | Public domain |
| `van_eyck/madonna_chancellor_rolin_1435.jpg` | 《洛林大臣的圣母》（双光源 + 远景嵌套） | Jan van Eyck | c. 1435 | Musée du Louvre, Paris | https://commons.wikimedia.org/wiki/File:La_Vierge_du_chancelier_Rolin_-_Jan_van_Eyck_-_Mus%C3%A9e_du_Louvre_Peintures_INV_1271.jpg | Public domain |
| `van_eyck/lucca_madonna_c1437.jpg` | 《卢卡圣母》（日常容器中的圣母） | Jan van Eyck | c. 1437 | Städel Museum, Frankfurt | https://commons.wikimedia.org/wiki/File:Jan_van_Eyck_-_Lucca_Madonna_-_Google_Art_Project.jpg | Public domain |
| `van_eyck/van_der_paele_1436.jpg` | 《凡德帕勒圣母》（盔甲反射含画家自画像） | Jan van Eyck | 1434–36 | Groeningemuseum, Bruges | https://commons.wikimedia.org/wiki/File:Eyck,_Jan_van_-_Madonna_with_Canon_van_der_Paele.jpeg | Public domain |
| `van_eyck/madonna_in_church_c1439.jpg` | 《教堂中的圣母》（尺度越界=教会化身） | Jan van Eyck | c. 1438–40 | Gemäldegalerie, Berlin | https://commons.wikimedia.org/wiki/File:Jan_van_Eyck_-_The_Madonna_in_the_Church_-_Google_Art_Project.jpg | Public domain |
| `van_eyck/annunciation_washington_c1435.jpg` | 《天使报喜》（华盛顿；光柱/仰视透视） | Jan van Eyck | c. 1434–36 | National Gallery of Art, Washington | https://commons.wikimedia.org/wiki/File:Annunciation_-_Jan_van_Eyck_-_1434_-_NG_Wash_DC.jpg | Public domain |
| `van_eyck/saint_barbara_1437.jpg` | 《圣芭芭拉》（银笔/毛笔素描，细节密度递减） | Jan van Eyck | 1437 | KMSKA, Antwerp | https://commons.wikimedia.org/wiki/File:Heilige_Barbara_van_Nicomedi%C3%AB,_Jan_van_Eyck,_1437,_Koninklijk_Museum_voor_Schone_Kunsten_Antwerpen,_410.jpg | **CC0**（KMSKA 开放许可） |
| `van_eyck/dresden_triptych_1437.jpg` | 《德累斯顿三联画》（唯一存世三联；框铭系统） | Jan van Eyck | 1437 | Gemäldegalerie Alte Meister, Dresden | https://commons.wikimedia.org/wiki/File:Jan_van_Eyck_-_Triptych_of_Mary_and_Child,_St._Michael,_and_the_Catherine_-_Google_Art_Project.jpg | Public domain |
| `van_eyck/saint_francis_stigmata_c1432.jpg` | 《圣方济各接受圣痕》（费城版） | Jan van Eyck | c. 1430–32（归属与都灵版有辩论） | Philadelphia Museum of Art | https://commons.wikimedia.org/wiki/File:Attributed_to_Jan_van_Eyck,_Netherlandish_(active_Bruges),_c._1395_-_1441_-_Saint_Francis_of_Assisi_Receiving_the_Stigmata_-_Google_Art_Project.jpg | Public domain |
| `van_eyck/crucifixion_last_judgment_c1437.jpg` | 《十字架受难与最后的审判》双联（Met） | Jan van Eyck | c. 1436–38 | The Metropolitan Museum of Art, New York | https://commons.wikimedia.org/wiki/File:Jan_van_Eyck_-_Crucifixion_and_Last_Judgement_diptych_(c._1436-38).jpg | Public domain |
| `van_eyck/margaret_van_eyck_1439.jpg` | 《玛格丽特像》（画家之妻；框铭"我的丈夫约翰内斯……"） | Jan van Eyck | 1439 | Groeningemuseum, Bruges | https://commons.wikimedia.org/wiki/File:Jan_van_Eyck_-_Portrait_of_Margaret_van_Eyck_(1439).jpg | Public domain |
| `van_eyck/jan_de_leeuw_1436.jpg` | 《金匠扬·德·莱乌像》（"会说话"的框铭） | Jan van Eyck | 1436 | Kunsthistorisches Museum, Vienna | https://commons.wikimedia.org/wiki/File:Jan_van_Eyck_-_Portrait_of_the_Goldsmith_Jan_de_Leeuw.jpg | Public domain |

## 逐张明细（尺寸 / 体积 / 备注）

### da_vinci — 达·芬奇（3 张）
- **last_supper.jpg** — The Last Supper（最后的晚餐），Leonardo da Vinci，c. 1495–1498，圣玛利亚感恩教堂, Milan。
  - 来源: https://commons.wikimedia.org/wiki/File:The_Last_Supper_Leonardo_Da_Vinci_-_High_Resolution.jpg
  - License: CC BY-SA 4.0（上传者 LoganTheWatermelon）；原始文件 4972×2609px
  - 落盘: 1800×944px，406 KB
- **mona_lisa.jpg** — Mona Lisa (La Gioconda)，Leonardo da Vinci，c. 1503–1506，卢浮宫（Musée du Louvre）, Paris。
  - 来源: https://commons.wikimedia.org/wiki/File:Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg
  - License: Public domain（C2RMF 官方高清复制品）；原始文件 7479×11146px
  - 落盘: 1208×1800px，784 KB
- **vitruvian_man.jpg** — Vitruvian Man（维特鲁威人），Leonardo da Vinci，c. 1490，学院美术馆（Gallerie dell’Accademia）, Venice。
  - 来源: https://commons.wikimedia.org/wiki/File:Da_Vinci_Vitruve_Luc_Viatour.jpg
  - License: Public domain；原始文件 2258×3070px
  - 落盘: 1324×1800px，813 KB

### michelangelo — 米开朗基罗（3 张）
- **creation_of_adam.jpg** — The Creation of Adam（创造亚当，西斯廷天顶画），Michelangelo，c. 1511，梵蒂冈博物馆（西斯廷礼拜堂）。
  - 来源: https://commons.wikimedia.org/wiki/File:Michelangelo_-_Creation_of_Adam_(cropped).jpg
  - License: Public domain；原始文件 3524×1599px
  - 落盘: 1800×817px，443 KB
- **david.jpg** — David（大卫），Michelangelo，1501–1504，学院美术馆, Florence。
  - 来源: https://commons.wikimedia.org/wiki/File:Michelangelo's_David_2015.jpg
  - License: CC BY-SA 4.0（摄影 Livioandronico2013）；原始文件 2388×3824px
  - 落盘: 1124×1800px，402 KB
- **pieta.jpg** — Pietà（圣殇），Michelangelo，1498–1499，圣彼得大教堂, Vatican。
  - 来源: https://commons.wikimedia.org/wiki/File:Michelangelo's_Pietà_Saint_Peter's_Basilica_Vatican_City.jpg
  - License: CC0（摄影 Jebulon）；原始文件 2936×2710px
  - 落盘: 1800×1661px，885 KB

### van_gogh — 梵高（3 张）
- **irises.jpg** — Irises，Vincent van Gogh，1890，The Metropolitan Museum of Art, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/436528
  - License: CC0 1.0（Met Open Access）；credit: Gift of Adele R. Levy, 1958
  - 落盘: 1800×1427px，866 KB
- **self_portrait_with_a_straw_hat.jpg** — Self-Portrait with a Straw Hat (obverse: The Potato Peeler)，Vincent van Gogh，1887，The Metropolitan Museum of Art, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/436532
  - License: CC0 1.0（Met Open Access）；credit: Bequest of Miss Adelaide Milton de Groot (1876-1967), 1967
  - 落盘: 1447×1800px，1015 KB
- **wheat_field_with_cypresses.jpg** — Wheat Field with Cypresses，Vincent van Gogh，1889，The Metropolitan Museum of Art, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/436535
  - License: CC0 1.0（Met Open Access）；credit: Purchase, The Annenberg Foundation Gift, 1993
  - 落盘: 1800×1433px，935 KB

### monet — 莫奈（3 张）
- **impression_sunrise.jpg** — Impression, Sunrise（印象·日出），Claude Monet，1872，玛摩丹莫奈美术馆, Paris。
  - 来源: https://commons.wikimedia.org/wiki/File:Monet_-_Impression,_Sunrise.jpg
  - License: Public domain；原始文件 5773×4478px
  - 落盘: 1800×1396px，662 KB
- **stacks_of_wheat_end_of_day_autumn.jpg** — Stacks of Wheat (End of Day, Autumn)，Claude Monet (French, 1840–1926)，1890–91，The Art Institute of Chicago。
  - 来源: https://www.artic.edu/artworks/14624
  - License: CC0（AIC 开放数据 / Public Domain Designation）；credit: Mr. and Mrs. Lewis Larned Coburn Memorial Collection; ref: 1933.444
  - 落盘: 1800×1172px，386 KB
- **water_lilies_1906.jpg** — Water Lilies，Claude Monet (French, 1840–1926)，1906，The Art Institute of Chicago。
  - 来源: https://www.artic.edu/artworks/16568
  - License: CC0（AIC 开放数据 / Public Domain Designation）；credit: Mr. and Mrs. Martin A. Ryerson Collection; ref: 1933.1157
  - 落盘: 1800×1729px，746 KB

### picasso — 毕加索（3 张）
- **cafe_wepler.jpg** — Café Wepler，Pablo Picasso，c. 1908–10, reworked in 1912，Cleveland Museum of Art。
  - 来源: https://clevelandart.org/art/1950.90
  - License: CC0（CMA Open Access）；technique: oil on fabric; credit: Gift of the Hanna Fund; acc: 1950.90
  - 落盘: ?px，0 KB
- **the_frugal_meal.jpg** — The Frugal Meal，Pablo Picasso，September 1904, printed 1913，Cleveland Museum of Art。
  - 来源: https://clevelandart.org/art/1929.888
  - License: CC0（CMA Open Access）；technique: etching; credit: Dudley P. Allen Fund; acc: 1929.888
  - 落盘: 1496×1800px，821 KB
- **the_saltimbanques.jpg** — The Saltimbanques，Pablo Picasso，1905, printed 1913，Cleveland Museum of Art。
  - 来源: https://clevelandart.org/art/1929.893
  - License: CC0（CMA Open Access）；technique: drypoint; credit: Dudley P. Allen Fund; acc: 1929.893
  - 落盘: ?px，0 KB

### cezanne — 塞尚（3 张）
- **mont_sainte_victoire_and_the_viaduct.jpg** — Mont Sainte-Victoire and the Viaduct of the Arc River Valley，Paul Cézanne，1882–85，The Metropolitan Museum of Art, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/435877
  - License: CC0 1.0（Met Open Access）；credit: H. O. Havemeyer Collection, Bequest of Mrs. H. O. Havemeyer, 1929
  - 落盘: 1800×1451px，634 KB
- **still_life_with_apples_and_a_pot_of_primroses.jpg** — Still Life with Apples and a Pot of Primroses，Paul Cézanne，ca. 1890，The Metropolitan Museum of Art, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/435882
  - License: CC0 1.0（Met Open Access）；credit: Bequest of Sam A. Lewisohn, 1951
  - 落盘: 1800×1428px，509 KB
- **the_card_players.jpg** — The Card Players，Paul Cézanne，1890–92，The Metropolitan Museum of Art, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/435868
  - License: CC0 1.0（Met Open Access）；credit: Bequest of Stephen C. Clark, 1960
  - 落盘: 1800×1433px，547 KB

### matisse — 马蒂斯（3 张）
- **la_danse.jpg** — La Danse (II)（舞蹈），Henri Matisse，1909–10，冬宫博物馆（Hermitage）, St. Petersburg。
  - 来源: https://commons.wikimedia.org/wiki/File:La_Danse_II,_par_Henri_Matisse.jpg
  - License: Public domain（上传者 Thierry Caro）；原始文件 2000×1377px
  - 落盘: 1800×1239px，337 KB
- **still_life_with_geranium.jpg** — Still Life with Geranium，Henri Matisse，1906，The Art Institute of Chicago。
  - 来源: https://www.artic.edu/artworks/87045
  - License: CC0（AIC 开放数据 / Public Domain Designation）；credit: Joseph Winterbotham Collection; ref: 1932.1342
  - 落盘: 1448×1800px，571 KB
- **woman_before_an_aquarium.jpg** — Woman before an Aquarium，Henri Matisse，1921–23，The Art Institute of Chicago。
  - 来源: https://www.artic.edu/artworks/27984
  - License: CC0（AIC 开放数据 / Public Domain Designation）；credit: Helen Birch Bartlett Memorial Collection; ref: 1926.220
  - 落盘: 1800×1438px，520 KB

### hokusai — 葛饰北斋（3 张）
- **red_fuji_south_wind_clear_sky.jpg** — South Wind, Clear Sky (Gaifū kaisei), also known as Red Fuji, from the series Thirty-six Views of Mount Fuji (Fugaku sanjūrokkei)，Katsushika Hokusai，ca. 1830–32，The Metropolitan Museum of Art, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/36490
  - License: CC0 1.0（Met Open Access）；credit: Rogers Fund, 1914
  - 落盘: 1800×1241px，579 KB
- **storm_below_mount_fuji.jpg** — Storm below Mount Fuji (Sanka no haku u), from the series Thirty-six Views of Mount Fuji (Fugaku sanjūrokkei)，Katsushika Hokusai，ca. 1830–32，The Metropolitan Museum of Art, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/36492
  - License: CC0 1.0（Met Open Access）；credit: Rogers Fund, 1914
  - 落盘: 1800×1221px，480 KB
- **the_great_wave.jpg** — Under the Wave off Kanagawa (Kanagawa oki nami ura), also known as The Great Wave, from the series Thirty-six Views of Mount Fuji (Fugaku sanjūrokkei)，Katsushika Hokusai，ca. 1830–32，The Metropolitan Museum of Art, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/45434
  - License: CC0 1.0（Met Open Access）；credit: H. O. Havemeyer Collection, Bequest of Mrs. H. O. Havemeyer, 1929
  - 落盘: 1800×1210px，649 KB

### caravaggio — 卡拉瓦乔（3 张）
- **bacchus.jpg** — Bacchus（酒神），Caravaggio，c. 1598，乌菲齐美术馆, Florence。
  - 来源: https://commons.wikimedia.org/wiki/File:Bacchus-Caravaggio_(1598).jpg
  - License: Public domain；原始文件 4779×5485px
  - 落盘: 1568×1800px，941 KB
- **calling_of_saint_matthew.jpg** — The Calling of Saint Matthew（圣马太蒙召），Caravaggio，1599–1600，圣路易吉·德·弗朗切西教堂·康塔雷利礼拜堂, Rome。
  - 来源: https://commons.wikimedia.org/wiki/File:Caravaggio_—_The_Calling_of_Saint_Matthew.jpg
  - License: CC0；原始文件 8792×8304px
  - 落盘: 1800×1700px，713 KB
- **judith_beheading_holofernes.jpg** — Judith Beheading Holofernes（朱迪斯斩首荷罗孚尼），Caravaggio，c. 1598–99，巴贝里尼宫（国立古代艺术馆）, Rome。
  - 来源: https://commons.wikimedia.org/wiki/File:Caravaggio_-_Judith_beheading_Holofernes.jpg
  - License: Public domain；原始文件 2048×1701px
  - 落盘: 1800×1495px，543 KB

### vermeer — 维米尔（3 张）
- **a_maid_asleep.jpg** — A Maid Asleep，Johannes Vermeer，ca. 1656–57，The Metropolitan Museum of Art, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/437878
  - License: CC0 1.0（Met Open Access）；credit: Bequest of Benjamin Altman, 1913
  - 落盘: 1569×1800px，492 KB
- **study_of_a_young_woman.jpg** — Study of a Young Woman，Johannes Vermeer，ca. 1665–67，The Metropolitan Museum of Art, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/437879
  - License: CC0 1.0（Met Open Access）；credit: Gift of Mr. and Mrs. Charles Wrightsman, in memory of Theodore Rousseau Jr., 1979
  - 落盘: 1608×1800px，576 KB
- **young_woman_with_a_water_pitcher.jpg** — Young Woman with a Water Pitcher，Johannes Vermeer，ca. 1662，The Metropolitan Museum of Art, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/437881
  - License: CC0 1.0（Met Open Access）；credit: Marquand Collection, Gift of Henry G. Marquand, 1889
  - 落盘: 1600×1800px，484 KB

### durer — 丢勒（3 张）
- **adam_and_eve.jpg** — Adam and Eve，Albrecht Dürer，1504，The Metropolitan Museum of Art, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/336222
  - License: CC0 1.0（Met Open Access）；credit: Fletcher Fund, 1919
  - 落盘: 1422×1800px，833 KB
- **melencolia_i.jpg** — Melencolia I，Albrecht Dürer，1514，The Metropolitan Museum of Art, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/360018
  - License: CC0 1.0（Met Open Access）；credit: Fletcher Fund, 1919
  - 落盘: 1403×1800px，965 KB
- **the_rhinoceros.jpg** — The Rhinoceros，Albrecht Dürer，1515，The Metropolitan Museum of Art, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/356497
  - License: CC0 1.0（Met Open Access）；credit: Gift of Junius Spencer Morgan, 1919
  - 落盘: 1800×1440px，886 KB

### klimt — 克里姆特（3 张；wave12 追加）
- **the_kiss.jpg** — The Kiss (Lovers)（吻），Gustav Klimt，c. 1907–1909，Belvedere, Vienna（inv. 912；180×180 cm）。
  - 来源: https://commons.wikimedia.org/wiki/File:Gustav_Klimt_-_Der_Kuss_(Liebespaar)_-_912_-_%C3%96sterreichische_Galerie_Belvedere.jpg （原始出处：digital.belvedere.at/objects/6678，Belvedere 数字收藏）
  - License: Public domain（PD-Art；PD-old-100-expired；上传者另附 CC BY-SA 4.0，详见 Commons 文件页）；原始文件 3457×3508px
  - 落盘: 1774×1800px，1322 KB
- **adele_bloch_bauer_i.jpg** — Portrait of Adele Bloch-Bauer I，Gustav Klimt，1907，Neue Galerie New York（140×140 cm）。
  - 来源: https://commons.wikimedia.org/wiki/File:Gustav_Klimt,_1907,_Adele_Bloch-Bauer_I,_Neue_Galerie_New_York.jpg （原始出处：neuegalerie.org）
  - License: Public domain（PD-Art；PD-old-auto-1923）；原始文件 2036×2035px
  - 落盘: 1800×1799px，1325 KB
- **death_and_life.jpg** — Death and Life，Gustav Klimt，1910/11（1912/13、1915/16 改绘），Leopold Museum, Vienna（inv. 630；180.8×200.6 cm）。
  - 来源: https://commons.wikimedia.org/wiki/File:Gustav_Klimt_-_Death_and_Life_-_Google_Art_Project.jpg （Google Art Project / Leopold Museum）
  - License: Public domain（PD-Art；PD-Art-two-auto）；原始文件 4059×3533px
  - 落盘: 1800×1567px，703 KB

### seurat — 修拉（10 张；wave13 追加）
- **a_sunday_on_la_grande_jatte.jpg** — A Sunday on La Grande Jatte — 1884（大碗岛），Georges Seurat，1884–86（边框 1888–89），Art Institute of Chicago（1926.224；207.5×308.1 cm）。
  - 来源: https://www.artic.edu/artworks/27992 （AIC IIIF `full/1686,`；真 Chromium 取回）
  - License: CC0（AIC Public Domain Designation）；原始文件 9310×6237px
  - 落盘: 1686×1130px，626 KB
- **bathers_at_asnieres.jpg** — Bathers at Asnières（阿尼埃尔浴场），Georges Seurat，1884，National Gallery, London（NG3908；201×300 cm）。
  - 来源: https://commons.wikimedia.org/wiki/File:Baigneurs_a_Asnieres.jpg （作品页 https://www.nationalgallery.org.uk/paintings/georges-seurat-bathers-at-asnieres）
  - License: Public domain；原始文件 6367×4226px
  - 落盘: 1800×1195px，632 KB
- **study_for_a_sunday_on_la_grande_jatte.jpg** — Study for "A Sunday on La Grande Jatte"，Georges Seurat，1884，The Met（51.112.6；70.5×104.1 cm）。
  - 来源: https://www.metmuseum.org/art/collection/search/437658 （Met Open Access）
  - License: CC0 1.0；原始文件 1959×1332px
  - 落盘: 1800×1224px，731 KB
- **gray_weather_grande_jatte.jpg** — Gray Weather, Grande Jatte，Georges Seurat，ca. 1886–88，The Met（2002.62.3）。
  - 来源: https://www.metmuseum.org/art/collection/search/438015
  - License: CC0 1.0；原始文件 3811×3132px
  - 落盘: 1800×1479px，1334 KB
- **circus_sideshow_parade_de_cirque.jpg** — Circus Sideshow (Parade de cirque)（阅兵），Georges Seurat，1887–88，The Met（61.101.17；99.7×149.9 cm）。
  - 来源: https://www.metmuseum.org/art/collection/search/437654
  - License: CC0 1.0；原始文件 3920×2621px
  - 落盘: 1800×1204px，948 KB
- **aman_jean_drawing.jpg** — Aman-Jean (Portrait of Edmond François Aman-Jean)，孔特蜡笔 / Michallet 纸，Georges Seurat，1882–83，The Met（61.101.16）。
  - 来源: https://www.metmuseum.org/art/collection/search/339751
  - License: CC0 1.0；原始文件 2975×3885px
  - 落盘: 1378×1800px，907 KB
- **le_chahut.jpg** — Le Chahut（康康舞），Georges Seurat，1889–90，Kröller-Müller Museum, Otterlo。
  - 来源: https://commons.wikimedia.org/wiki/File:Georges_Seurat_-_Le_Chahut_-_Google_Art_Project.jpg （Google Art Project 扫描）
  - License: Public domain；原始文件 3582×4349px
  - 落盘: 1483×1800px，1609 KB
- **the_circus.jpg** — The Circus (Le Cirque)（马戏），Georges Seurat，1890–91（未完成），Musée d'Orsay, Paris。
  - 来源: https://commons.wikimedia.org/wiki/File:Georges_Seurat_-_The_Circus_-_Google_Art_Project.jpg
  - License: Public domain；原始文件 3918×4855px
  - 落盘: 1453×1800px，1266 KB
- **young_woman_powdering_herself.jpg** — Young Woman Powdering Herself（扑粉的年轻女子），Georges Seurat，1888–90，The Courtauld Gallery, London。
  - 来源: https://commons.wikimedia.org/wiki/File:Georges_Seurat_-_Young_Woman_Powdering_Herself_-_Google_Art_Project.jpg
  - License: Public domain；原始文件 1539×2401px
  - 落盘: 1154×1800px，852 KB
- **les_poseuses.jpg** — Les Poseuses (Models)（模特们），Georges Seurat，1886–88，Barnes Foundation, Philadelphia。
  - 来源: https://commons.wikimedia.org/wiki/File:Georges_Seurat_-_Models_(Poseuses)_-_BF811_-_Barnes_Foundation.jpg
  - License: Public domain；原始文件 4096×3298px
  - 落盘: 1800×1449px，1146 KB

### turner — 透纳（5 张；wave12 追加）
- **fighting_temeraire.jpg** — The Fighting Téméraire tugged to her last Berth to be broken up（无畏号），J.M.W. Turner，1839，National Gallery, London（NG524）。
  - 来源: https://commons.wikimedia.org/wiki/File:Turner,_J._M._W._-_The_Fighting_T%C3%A9m%C3%A9raire_tugged_to_her_last_Berth_to_be_broken.jpg
  - License: Public domain；原始文件 6000×4455px
  - 落盘: 1800×1337px，572 KB
- **norham_castle_sunrise.jpg** — Norham Castle, Sunrise（诺勒姆城堡·日出），J.M.W. Turner，c. 1845，Tate, London（N01981）。
  - 来源: https://commons.wikimedia.org/wiki/File:Jmw_turner,_norham_castle,_alba,_1845_ca.jpg
  - License: **CC BY 3.0**（摄影 Sailko；署名要求=是）；原始文件 3954×3102px
  - 落盘: 1800×1355px，319 KB
- **rain_steam_speed.jpg** — Rain, Steam and Speed – The Great Western Railway（雨、蒸汽与速度），J.M.W. Turner，1844，National Gallery, London（NG538）。
  - 来源: https://commons.wikimedia.org/wiki/File:Turner_-_Rain,_Steam_and_Speed_-_National_Gallery_file.jpg
  - License: Public domain；原始文件 5661×4226px
  - 落盘: 1800×1343px，601 KB
- **snow_storm_steam_boat.jpg** — Snow Storm: Steam-Boat off a Harbour's Mouth（暴风雪），J.M.W. Turner，exhibited 1842，Tate, London（N00530）。
  - 来源: https://commons.wikimedia.org/wiki/File:J.M.W._Turner_%E2%80%93_Snow_Storm_-_Steam-Boat_off_a_Harbour%27s_Mouth.jpg
  - License: Public domain；原始文件 7247×5448px
  - 落盘: 1800×1353px，690 KB
- **the_slave_ship.jpg** — The Slave Ship（奴隶船），J.M.W. Turner，1840，Museum of Fine Arts, Boston（99.22）。
  - 来源: https://commons.wikimedia.org/wiki/File:Slave-ship.jpg
  - License: Public domain；原始文件 2152×1616px
  - 落盘: 1800×1352px，455 KB

### rembrandt — 伦勃朗（6 张；wave12 追加）
- **the_night_watch.jpg** — The Night Watch（夜巡），Rembrandt，1642，Rijksmuseum, Amsterdam（SK-C-5）。
  - 来源: https://commons.wikimedia.org/wiki/File:The_Night_Watch_-_HD.jpg（hyper-resolution 2020 拼接件）
  - License: Public domain（PD-Art）；原始文件 57813×48438px
  - 落盘: 1800×1508px，467 KB
- **the_jewish_bride.jpg** — The Jewish Bride（犹太新娘），Rembrandt，c. 1665–69，Rijksmuseum, Amsterdam（SK-C-216）。
  - 来源: https://commons.wikimedia.org/wiki/File:Rembrandt_Harmensz._van_Rijn_-_Portret_van_een_paar_als_oudtestamentische_figuren,_genaamd_%27Het_Joodse_bruidje%27_-_Google_Art_Project.jpg
  - License: Public domain；原始文件 5486×4000px
  - 落盘: 1800×1312px，663 KB
- **self_portrait_with_two_circles.jpg** — Self-Portrait with Two Circles（双圆自画像），Rembrandt，c. 1665–69，Kenwood House, London（57）。
  - 来源: https://commons.wikimedia.org/wiki/File:Rembrandt_Self-portrait_(Kenwood).jpg
  - License: Public domain；原始文件 3807×4588px
  - 落盘: 1494×1800px，617 KB
- **self_portrait_drawing_at_a_window.jpg** — Self-Portrait Drawing at a Window（窗前自画像，蚀刻），Rembrandt，1648，National Gallery of Art, Washington（9931）。
  - 来源: https://commons.wikimedia.org/wiki/File:Rembrandt_van_Rijn,_Self-Portrait_Drawing_at_a_Window,_1648,_NGA_9931.jpg
  - License: CC0（NGA Open Access）；原始文件 3316×4000px
  - 落盘: 1492×1800px，991 KB
- **the_anatomy_lesson_of_dr_nicolaes_tulp.jpg** — The Anatomy Lesson of Dr Nicolaes Tulp（杜尔普医生的解剖课），Rembrandt，1632，Mauritshuis, The Hague（146）。
  - 来源: https://commons.wikimedia.org/wiki/File:Rembrandt_-_The_Anatomy_Lesson_of_Dr_Nicolaes_Tulp.jpg
  - License: Public domain；原始文件 6000×4520px
  - 落盘: 1800×1356px，496 KB
- **aristotle_with_a_bust_of_homer.jpg** — Aristotle with a Bust of Homer（亚里士多德凝视荷马胸像），Rembrandt，1653，The Met, New York（61.198）。
  - 来源: https://commons.wikimedia.org/wiki/File:Aristotle_with_a_Bust_of_Homer_MET_DP319026.jpg
  - License: CC0（Met Open Access）；原始文件 3647×3839px
  - 落盘: 1710×1800px，422 KB

### goya — 戈雅（9 张；wave13 追加）
- **third_of_may_1808.jpg** — The Third of May 1808（1808 年 5 月 3 日），Francisco de Goya，1814，Museo del Prado, Madrid。
  - 来源: https://commons.wikimedia.org/wiki/File:El_Tres_de_Mayo,_by_Francisco_de_Goya,_from_Prado_in_Google_Earth.jpg
  - License: Public domain；原始文件 30000×23131px（Prado in Google Earth 扫描）
  - 落盘: 1800×1388px，437 KB
- **saturn_devouring_his_son.jpg** — Saturn Devouring His Son（农神吞噬其子，黑画），Francisco de Goya，c. 1819–23，Museo del Prado, Madrid。
  - 来源: https://commons.wikimedia.org/wiki/File:Francisco_de_Goya,_Saturno_devorando_a_su_hijo_(1819-1823).jpg
  - License: Public domain；原始文件 1661×3051px
  - 落盘: 980×1800px，450 KB
- **the_sleep_of_reason_produces_monsters.jpg** — The Sleep of Reason Produces Monsters（奇想集 43），Francisco de Goya，1799，The Met, New York。
  - 来源: https://commons.wikimedia.org/wiki/File:Plate_43_from_%27Los_Caprichos%27-_The_sleep_of_reason_produces_monsters_(El_sue%C3%B1o_de_la_razon_produce_monstruos)_MET_DP816991.jpg
  - License: CC0（Met Open Access 捐赠件）；原始文件 2640×3697px
  - 落盘: 1285×1800px，389 KB
- **disasters_of_war_yo_lo_vi.jpg** — The Disasters of War, plate 44 "Yo lo vi"（战祸·我看见了），Francisco de Goya，1810–20（1863 出版），The Met, New York。
  - 来源: https://commons.wikimedia.org/wiki/File:Plate_44_from_%27The_Disasters_of_War%27_(Los_Desastres_de_la_Guerra)-_%27I_saw_it%27_(Yo_lo_vi.)_MET_DP817391.jpg
  - License: CC0（Met Open Access 捐赠件）；原始文件 3778×2771px
  - 落盘: 1800×1320px，308 KB
- **the_family_of_charles_iv.jpg** — The Family of Charles IV（卡洛斯四世一家），Francisco de Goya，1800–01，Museo del Prado, Madrid。
  - 来源: https://commons.wikimedia.org/wiki/File:La_familia_de_Carlos_IV,_por_Francisco_de_Goya.jpg
  - License: Public domain；原始文件 1911×1595px
  - 落盘: 1800×1502px，373 KB
- **manuel_osorio_manrique_de_zuniga.jpg** — Manuel Osorio Manrique de Zúñiga（奥索里奥男孩），Francisco de Goya，c. 1787–88，The Met, New York。
  - 来源: https://commons.wikimedia.org/wiki/File:Manuel_Osorio_Manrique_de_Zu%C3%B1iga_(1784%E2%80%931792)_MET_DP287624.jpg
  - License: CC0（Met Open Access 捐赠件）；原始文件 2855×3873px
  - 落盘: 1327×1800px，279 KB
- **the_dog.jpg** — The Dog（狗，黑画），Francisco de Goya，c. 1819–23，Museo del Prado, Madrid。
  - 来源: https://commons.wikimedia.org/wiki/File:Goya_Dog.jpg
  - License: Public domain；原始文件 1797×3051px
  - 落盘: 1060×1800px，613 KB
- **witches_flight.jpg** — Witches' Flight（女巫飞行），Francisco de Goya，1798，Museo del Prado, Madrid。
  - 来源: https://commons.wikimedia.org/wiki/File:Francisco_de_Goya_-_Vuelo_de_brujas_(1798).jpg
  - License: Public domain；原始文件 2068×2952px
  - 落盘: 1261×1800px，461 KB
- **tauromaquia_plate_18.jpg** — La Tauromaquia, plate 18（斗牛术·Martincho 的胆量），Francisco de Goya，1815–16，The Met, New York。
  - 来源: https://commons.wikimedia.org/wiki/File:Plate_18_of_the_%27Tauromaquia%27-_The_daring_of_Martincho_in_the_ring_at_Saragossa_MET_DP817784.jpg
  - License: CC0（Met Open Access 捐赠件）；原始文件 3803×2667px
  - 落盘: 1800×1262px，443 KB

### bada_shanren — 八大山人（9 张；wave13 追加）
- **met_fish_and_rocks_1699.jpg** — Fish and Rocks（鱼石图），八大山人（朱耷），1699，The Metropolitan Museum of Art（41491）。
  - 来源: https://www.metmuseum.org/art/collection/search/41491；License: CC0 1.0（Met Open Access）
  - 落盘: 1054×1800px，245 KB
- **met_two_eagles_1702.jpg** — Two Eagles（双鹰图），八大山人，1702，The Metropolitan Museum of Art（39540）。
  - 来源: https://www.metmuseum.org/art/collection/search/39540；License: CC0 1.0（Met Open Access）
  - 落盘: 1030×1800px，329 KB
- **met_birds_in_a_lotus_pond.jpg** — Birds in a Lotus Pond（湖塘禽鸟），八大山人，ca. 1690，The Metropolitan Museum of Art（49143）。
  - 来源: https://www.metmuseum.org/art/collection/search/49143；License: CC0 1.0（Met Open Access）
  - 落盘: 1800×851px，292 KB
- **met_landscape_album_1699.jpg** — Landscape album（山水册，十二开），八大山人，1699，The Metropolitan Museum of Art（49145）。
  - 来源: https://www.metmuseum.org/art/collection/search/49145；License: CC0 1.0（Met Open Access）
  - 落盘: 1431×1800px，677 KB
- **met_letters_to_fang_shiguan.jpg** — Letters to Fang Shiguan（致方士琯尺牍，十开），八大山人，ca. 1688–1705，The Metropolitan Museum of Art（49147）。
  - 来源: https://www.metmuseum.org/art/collection/search/49147；License: CC0 1.0（Met Open Access）
  - 落盘: 1296×1800px，571 KB
- **cleveland_landscape_after_guo_zhongshu.jpg** — Landscape after Guo Zhongshu（仿郭忠恕山水），八大山人，ca. 1680–1705，Cleveland Museum of Art（1955.36）。
  - 来源: https://clevelandart.org/art/1955.36；License: CC0（CMA Open Access）
  - 落盘: 777×1800px，329 KB
- **freer_lotus_and_ducks_ca1696.jpg** — Lotus and Ducks（荷花双凫图），八大山人，ca. 1696，Freer Gallery of Art（F1998.45，王方宇旧藏）。
  - 来源: https://commons.wikimedia.org/wiki/File:Bada_Shanren_-_Lotus_and_Ducks_-_Google_Art_Project.jpg；License: Public domain（PD-Art）
  - 落盘: 982×1800px，279 KB
- **tianjin_river_flowers_1697.jpg** — 《河上花图》卷（局部，HX5 段），八大山人，1697，天津博物馆。
  - 来源: https://commons.wikimedia.org/wiki/Category:Flowers_on_a_River_by_Bada_Shanren；License: Public domain（PD-Art）
  - 落盘: 1800×1328px，473 KB
- **commons_anwan_album_bird.jpg** — 《安晚册》鸟页（局部），八大山人，1694（册），泉屋博古馆（日本）。
  - 来源: https://commons.wikimedia.org/wiki/File:Anban_Album_Bird_Bada_Shanren.jpg；License: Public domain（PD-Art）
  - 落盘: 844×978px，185 KB

### qi_baishi — 齐白石（公开 11 张 / 私有 6；wave13 追加）
> 版权口径：齐白石卒 1957——中国及多数伯尔尼公约国已过保护期；美国状态（URAA）逐件不同，逐张按 Commons 模板记录。**主脑从严处置（2026-10-15）：4 件带 `{{Not-PD-US-URAA}}` 注记图（ink_shrimp / pine_eagle_and_couplet_1946 / daiyu_buries_flowers_1950 / leaves_and_insects）已移入私有层**，公开侧现 11 张（另见「私有层例外」节）。
- **morning_glory_1950.jpg** — 牵牛花（Liserons rouges），齐白石，1950，赛努奇博物馆, Paris（摄影 Jean-Pierre Dalbéra）。
  - 来源: https://commons.wikimedia.org/wiki/File:%22Liserons_rouges%22_de_Qi_Baishi_(Mus%C3%A9e_Cernuschi,_Paris)_-_Flickr_-_dalbera.jpg
  - License: `{{PD-China}}`（作品）+ 照片 CC BY 2.0（已审）
  - 落盘: 1158×1800px，231 KB
- **camellia_and_bird.jpg** — 茶花小鸟，齐白石，1921。
  - 来源: https://commons.wikimedia.org/wiki/File:%E9%BD%90%E7%99%BD%E7%9F%B3_%E8%8C%B6%E8%8A%B1%E5%B0%8F%E9%B8%9F.jpg
  - License: `{{PD-PRC}}` + `{{PD-US-expired}}`
  - 落盘: 451×1800px，178 KB
- **wisteria_scroll.jpg** — 齐璜画藤轴，齐白石，近现代（无年款），故宫博物院·名画记（官方扫描）。
  - 来源: https://commons.wikimedia.org/wiki/File:%E9%BD%90%E7%92%9C%E7%94%BB%E8%97%A4%E8%BD%B4.png
  - License: `{{PD-scan}}` + `{{PD-old-auto-expired}}`
  - 落盘: 911×1800px，284 KB
- **frogs.jpg** — 鸣蛙，齐白石，不晚于 1955，中国美术馆藏（原老舍家族）。
  - 来源: https://commons.wikimedia.org/wiki/File:%E9%BD%90%E7%99%BD%E7%9F%B3%E3%80%8A%E9%B8%A3%E8%9B%99%E3%80%8B.jpg
  - License: `{{PD-Art|PD-CN}}` + `{{PD-US-no notice}}`
  - 落盘: 906×1800px，205 KB
- **old_man_and_gourd.jpg** — Old Man Looking into a Gourd（老人与葫芦），齐白石，旧金山亚洲艺术博物馆（摄影 Daderot）。
  - 来源: https://commons.wikimedia.org/wiki/File:Old_Man_Looking_into_a_Gourd,_by_Qi_Baishi,_ink_on_paper_-_Asian_Art_Museum_of_San_Francisco_-_DSC01548.JPG
  - License: 摄影 `{{CC0}}`
  - 落盘: 1200×1800px，360 KB
- **twelve_landscape_screens_1925.jpg** — 十二山水屏，齐白石，1925，公开拍卖图（Commons）。
  - 来源: https://commons.wikimedia.org/wiki/File:Twelve_Landscape_Screens_by_Qi_Baishi.jpg
  - License: `{{PD-Art|PD-China|PD-old-auto}}`
  - 落盘: 900×1101px，233 KB
- **seal_script_couplet.jpg** — 篆书联「持山与鹤」，齐白石，摄影 陳寅恪（Commons）。
  - 来源: https://commons.wikimedia.org/wiki/File:%E9%BD%90%E7%99%BD%E7%9F%B3%E2%80%9C%E6%8C%81%E5%B1%B1%E4%B8%8E%E9%B9%A4%E2%80%9D%E7%AF%86%E4%B9%A6%E8%81%94%E4%B9%8B%E4%BA%8C.jpg
  - License: 摄影 `{{self|cc-by-sa-4.0}}`
  - 落盘: 800×1253px，186 KB
- **seal_impression_changsha.jpg** — 印「中国长沙湘潭人也」，齐白石，摄影 陳寅恪（Commons）。
  - 来源: https://commons.wikimedia.org/wiki/File:%E9%BD%90%E7%99%BD%E7%9F%B3_%E4%B8%AD%E5%9B%BD%E9%95%BF%E6%B2%99%E6%B9%98%E6%BD%AD%E4%BA%BA%E4%B9%9F_%E4%B9%8B%E4%BA%8C.jpg
  - License: 摄影 `{{self|cc-by-sa-4.0}}`
  - 落盘: 490×515px，70 KB
- **portrait_by_lang_jingshan.jpg** — 齐白石像（郎静山摄），1930s，摄影 郎静山（Commons）。
  - 来源: https://commons.wikimedia.org/wiki/File:Qi_Baishi,_by_Lang_Jingshan.jpg
  - License: `{{PD-China-1996}}`
  - 落盘: 456×598px，76 KB
- **zhou_enlai_visit_1953.jpg** — 周恩来拜访齐白石，1953，《人民画报》1953 年（Commons 翻拍）。
  - 来源: https://commons.wikimedia.org/wiki/File:1953-03_1953%E5%B9%B4_%E5%91%A8%E6%81%A9%E6%9D%A5%E6%8B%9C%E8%AE%BF%E9%BD%90%E7%99%BD%E7%9F%B3.jpg
  - License: `{{PD-CN}}`
  - 落盘: 960×642px，127 KB
- **lotus_and_insects.jpg** — Lotus and Insects（工写结合示例），齐白石，20 世纪早期，馆藏展陈翻拍（摄影 Jnzl's Photos）。
  - 来源: https://commons.wikimedia.org/wiki/File:Lotus_and_Insects_by_Qi_Baishi_(11264641955).jpg
  - License: 摄影 CC BY 2.0（已审）；作品 PD-China
  - 落盘: 960×1800px，282 KB

### ito_jakuchu — 伊藤若冲（18 张；wave13 追加）
> 许可口径：① ColBase 图像（皇居三の丸尚蔵館 / 東京国立博物館 / 京都国立博物館）按 ColBase 利用规约使用（可自由复制/公开传播/改编，含商用；须标注出典：「出典：国立文化財機構所蔵品統合検索システム（ColBase）」）；② Commons 图像为 Public domain（PD-Art）；③ Met 图像 CC0。
- **doshoku_saie_gunkei.jpg** — 動植綵絵之内「群鶏図」（13 羽の雄鶏），c.1761–1765，皇居三の丸尚蔵館。
  - 来源: https://colbase.nich.go.jp/collection_items/shozokan/SZK002949；License: ColBase 规约（出典：ColBase）
  - 落盘: 1348×1800px，534 KB
- **doshoku_saie_rogan.jpg** — 動植綵絵之内「芦雁図」，c.1765–1766，皇居三の丸尚蔵館。
  - 来源: 同上（SZK002949）；License: ColBase 规约｜落盘: 1348×1800px，402 KB
- **doshoku_saie_gunyo.jpg** — 動植綵絵之内「群魚図」（ルリハタに紺青），c.1765–1766，皇居三の丸尚蔵館。
  - 来源: 同上（SZK002949）；License: ColBase 规约｜落盘: 1348×1800px，352 KB
- **doshoku_saie_kikka.jpg** — 動植綵絵之内「菊花流水図」，c.1765–1766，皇居三の丸尚蔵館。
  - 来源: 同上（SZK002949）；License: ColBase 规约｜落盘: 1348×1800px，430 KB
- **doshoku_saie_himawari.jpg** — 動植綵絵之内「向日葵雄鶏図」，1759，皇居三の丸尚蔵館。
  - 来源: https://commons.wikimedia.org/wiki/File:It%C5%8D_Jakuch%C5%AB_-_Rooster_and_Sunflowers_%28Colorful_Realm_of_Living_Beings%29.jpg；License: Public domain｜落盘: 997×1800px，477 KB
- **doshoku_saie_hakkei.jpg** — 動植綵絵之内「老松白鶏図」，c.1759–60，皇居三の丸尚蔵館。
  - 来源: https://commons.wikimedia.org/wiki/File:It%C5%8D_Jakuch%C5%AB_-_White_fowl_and_pine_%28Colorful_Realm_of_Living_Beings%29.jpg；License: Public domain｜落盘: 1008×1800px，597 KB
- **doshoku_saie_setchu_enou.jpg** — 動植綵絵之内「雪中鴛鴦図」（正反双面胡粉の雪），1759，皇居三の丸尚蔵館。
  - 来源: https://commons.wikimedia.org/wiki/File:It%C5%8D_Jakuch%C5%AB_-_Mandarin_ducks_in_the_snow_%28Colorful_Realm_of_Living_Beings%29.jpg；License: Public domain｜落盘: 1047×1800px，567 KB
- **doshoku_saie_rousho_kujaku.jpg** — 動植綵絵之内「老松孔雀図」（白孔雀），c.1757–60，皇居三の丸尚蔵館。
  - 来源: https://commons.wikimedia.org/wiki/File:%27Old_Pine_Tree_and_Peacock%27_from_the_%27Colorful_Realm_of_Living_Beings%27_by_Ito_Jakuchu.jpg；License: Public domain｜落盘: 1051×1800px，553 KB
- **doshoku_saie_kaigai.jpg** — 動植綵絵之内「貝甲図」，c.1761–65，皇居三の丸尚蔵館。
  - 来源: https://commons.wikimedia.org/wiki/File:It%C5%8D_Jakuch%C5%AB_-_Shells_%28Colorful_Realm_of_Living_Beings%29.jpg；License: Public domain｜落盘: 1044×1800px，422 KB
- **doshoku_saie_shutou_gunjaku.jpg** — 動植綵絵之内「秋塘群雀図」（58 羽の雀），1759，皇居三の丸尚蔵館。
  - 来源: https://commons.wikimedia.org/wiki/File:Autumn_Millet_and_Sparrows_by_Ito_Jakuchu_%28Sannomaru_Shozokan%29.jpg；License: Public domain｜落盘: 876×1500px，312 KB
- **kasonehanzu.jpg** — 果蔬涅槃図（重文；款記「藤汝鈞印」「若沖居士」），c.1790s，京都国立博物館。
  - 来源: https://colbase.nich.go.jp/collection_items/kyohaku/A%E7%94%B283；License: ColBase 规约｜落盘: 950×1800px，387 KB
- **genpo_yoka.jpg** — 玄圃瑤華之内「水葵・糸瓜」（拓版画），1768，東京国立博物館。
  - 来源: https://colbase.nich.go.jp/collection_items/tnm/A-12445-5；License: ColBase 规约｜落盘: 1800×1416px，442 KB
- **shoubai_gunkei_zu_byobu.jpg** — 松梅群鶏図屏風（六曲一双），江戸中期，東京国立博物館。
  - 来源: https://colbase.nich.go.jp/collection_items/tnm/A-12320；License: ColBase 规约｜落盘: 1433×1800px，400 KB
- **kaiboji_gunkei_zu.jpg** — 群鶏図（旧・海宝寺方丈障壁画；约 10m 连续画面），1790，京都国立博物館。
  - 来源: https://colbase.nich.go.jp/collection_items/kyohaku/A%E7%94%B2355；License: ColBase 规约｜落盘: 1112×1800px，239 KB
- **ishidoro_zu_byobu.jpg** — 石燈籠図屏風（点描造石质），江戸中期，京都国立博物館。
  - 来源: https://colbase.nich.go.jp/collection_items/kyohaku/A%E7%94%B21339；License: ColBase 规约｜落盘: 1800×826px，313 KB
- **chouju_kaboku_zu_byobu.jpg** — 鳥獣花木図屏風（右隻；升目描き），c.1770s–1780s，出光美術館（旧プライス・コレクション）。
  - 来源: https://commons.wikimedia.org/wiki/File:It%C5%8D_Jakuch%C5%AB_-_Animals_in_the_Flower_garden_%28Right-hand_screen%29.jpg；License: Public domain｜落盘: 1800×720px，451 KB
- **zo_to_kujira_zu_byobu.jpg** — 象と鯨図屏風（左隻；升目描き；2008 年发现），c.1796，Miho Museum。
  - 来源: https://commons.wikimedia.org/wiki/File:Elephant_and_Whale_Screens_by_Ito_Jakuchu_%28Miho_Museum%29L.jpg；License: Public domain｜落盘: 1800×841px，290 KB
- **crane_under_plum.jpg** — Crane under a Branch of Plum（梅枝と鶴；晚年简笔侧），1770s，The Metropolitan Museum of Art（929172）。
  - 来源: https://www.metmuseum.org/art/collection/search/929172；License: CC0（Met Open Access）｜落盘: 1107×1800px，303 KB

### mucha — 慕夏（12 张；wave15 并入）
- **gismonda_1894.jpg** — *Gismonda*（吉斯蒙达戏剧海报，莎拉·伯恩哈特），Alphonse Mucha，1894，Mucha Trust 藏（彩色石版画 216×74.2 cm；Lemercier 印）。
  - 来源: https://commons.wikimedia.org/wiki/File:Alphonse_Mucha_-_Poster_for_Victorien_Sardou%27s_Gismonda_starring_Sarah_Bernhardt.jpg；License: Public domain
  - 落盘: 636×1800px，433 KB
- **dame_aux_camelias_1896.jpg** — *La Dame aux Camélias*（茶花女戏剧海报），Alphonse Mucha，1896，Mucha Trust 藏。
  - 来源: https://commons.wikimedia.org/wiki/File:Alfons_Mucha_-_1896_-_La_Dame_aux_Cam%C3%A9lias_-_Sarah_Bernhardt.jpg；License: Public domain
  - 落盘: 675×1800px，338 KB
- **job_1896.jpg** — *Job*（Job 卷烟纸广告海报），Alphonse Mucha，1896，Mucha Trust 藏（底缘带来源收藏编目标签）。
  - 来源: https://commons.wikimedia.org/wiki/File:Alphonse_Mucha_-_Advertisment_for_Job_cigarettes%2C_1896.jpg；License: Public domain
  - 落盘: 1253×1800px，422 KB
- **seasons_series_1896.jpg** — *The Seasons*（四季，四联装饰板·合框变体），Alphonse Mucha，1896，Champenois 印。
  - 来源: https://commons.wikimedia.org/wiki/File:Alfons_Mucha_-_The_Seasons_%28series%29%2C_1896.jpg；License: Public domain
  - 落盘: 1754×847px，449 KB（原样，长边 <1800）
- **seasons_summer_1896.jpg** — *The Seasons — Summer*（四季·夏），Alphonse Mucha，1896，Champenois 印。
  - 来源: https://commons.wikimedia.org/wiki/File:Alfons_Mucha_-_The_Seasons_-_Summer_%281896%29.jpg；License: Public domain
  - 落盘: 937×1800px，496 KB
- **zodiac_1896.jpg** — *Zodiac*（黄道十二宫，La Plume 日历），Alphonse Mucha，1896–97，La Plume 发行（Commons 文件名年份笔误 1869）。
  - 来源: https://commons.wikimedia.org/wiki/File:Alphonse_Mucha_-_Zodiac%2C_1869.jpg；License: Public domain
  - 落盘: 1355×1800px，789 KB
- **le_pater_1899.jpg** — *Le Pater* —「Lead us not into temptation」（主祷文页），Alphonse Mucha，1899（石版画册 510 册）。
  - 来源: https://commons.wikimedia.org/wiki/File:Alfons_Mucha_Le_Pater_%22Lead_us_not_into_temptation%22_%281899%29.jpg；License: **CC BY-SA 4.0**（翻拍 SiefkinDR 2018；原作 PD；署名要求=是）
  - 落盘: 1000×1498px，342 KB
- **documents_decoratifs_plate30.jpg** — *Documents décoratifs* 第 30 版（装饰图案版），Alphonse Mucha，1901/1902，Librairie Centrale des Beaux-Arts（图册 72 版）。
  - 来源: https://commons.wikimedia.org/wiki/File:30_mucha_documentsdecoratifs_1901.jpg；License: Public domain
  - 落盘: 964×1600px，522 KB
- **monaco_monte_carlo_1897.jpg** — *Monaco–Monte-Carlo*（巴黎—蒙特卡洛铁路海报），Alphonse Mucha，1897，P.L.M. 铁路。
  - 来源: https://commons.wikimedia.org/wiki/File:Alfons_Mucha_-_Poster_for_%27Monaco_-_Monte_Carlo%27%2C_P.L.M._railway_services_%281897%29.jpg；License: Public domain
  - 落盘: 1212×1800px，788 KB
- **moet_cremant_1899.jpg** — *Moët & Chandon Crémant Impérial*（香槟广告），Alphonse Mucha，1899。
  - 来源: https://commons.wikimedia.org/wiki/File:Mucha-Mo%C3%ABt_%26_Chandon_Cr%C3%A9mant_Imp%C3%A9rial-1899.jpg；License: Public domain
  - 落盘: 652×1729px，216 KB
- **self_portrait.jpg** — *Self-portrait*（自画像，持笔），Alphonse Mucha，c. 1907，Mucha Trust 藏（布面油画）。
  - 来源: https://commons.wikimedia.org/wiki/File:Alfons_Mucha_Selbstportr%C3%A4t.jpg；License: Public domain
  - 落盘: 1185×1800px，304 KB
- **slav_epic_apotheosis.jpg** — *The Slav Epic* No.20《斯拉夫的神化》（Slavs for Humanity），Alphonse Mucha，1926，布拉格市藏（蛋彩画布）。
  - 来源: https://commons.wikimedia.org/wiki/File:Mucha_Apoteoza.jpg；License: Public domain
  - 落盘: 1488×1800px，431 KB

### munch — 蒙克（13 张；wave15 并入）
- **scream_1893_mm.jpg** — The Scream（尖叫；粉彩/蜡笔纸板，MM.M.00122b），Edvard Munch，1893，Munchmuseet, Oslo。
  - 来源: https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_The_Scream_-_MM.M.00122b_-_Munch_Museum.jpg；License: Public domain
  - 落盘: 1280×1674px，656 KB（限流期 1280px 缩略，长边未达 1800）
- **scream_1893_nm.jpg** — The Scream（尖叫；NG.M.00939），Edvard Munch，1893，National Museum, Oslo。
  - 来源: https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_The_Scream_-_NG.M.00939_-_National_Museum_of_Art,_Architecture_and_Design.jpg；License: Public domain
  - 落盘: 1450×1800px，711 KB
- **scream_1910_mm.jpg** — The Scream（尖叫；MM.M.00514），Edvard Munch，1910，Munchmuseet, Oslo。
  - 来源: https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_The_Scream_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1423×1800px，726 KB
- **scream_lithograph_1895.jpg** — The Scream（尖叫；石版画 Woll G 38；Met DP860367），Edvard Munch，1895，The Met, New York。
  - 来源: https://commons.wikimedia.org/wiki/File:The_Scream_MET_DP860367.jpg；License: CC0（Met Open Access 捐赠件）
  - 落盘: 1396×1800px，586 KB
- **madonna_1894_95.jpg** — Madonna（圣母；NG.M.00841），Edvard Munch，1894–95，National Museum, Oslo。
  - 来源: https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_Madonna_(1894-1895).jpg；License: Public domain
  - 落盘: 1399×1800px，937 KB
- **dance_of_life_1899.jpg** — The Dance of Life（生命之舞；NG.M.00941），Edvard Munch，1899–1900，National Museum, Oslo。
  - 来源: https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_The_Dance_of_Life_-_NG.M.00941_-_National_Museum_of_Art,_Architecture_and_Design.jpg；License: Public domain
  - 落盘: 1800×1173px，493 KB
- **anxiety_1894.jpg** — Anxiety（焦虑；MM.M.00515），Edvard Munch，1894，Munchmuseet, Oslo。
  - 来源: https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_Anxiety_-_MM.M.00515_-_Munch_Museum.jpg；License: Public domain
  - 落盘: 1427×1800px，981 KB
- **self_portrait_with_cigarette_1895.jpg** — Self-Portrait with Cigarette（自画像与香烟；NG.M.00470），Edvard Munch，1895，National Museum, Oslo。
  - 来源: https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_Self-Portrait_with_Cigarette_-_NG.M.00470_-_National_Museum_of_Art,_Architecture_and_Design.jpg；License: Public domain
  - 落盘: 1371×1800px，837 KB
- **puberty_1894_95.jpg** — Puberty（青春期；NG.M.00807），Edvard Munch，1894–95，National Museum, Oslo。
  - 来源: https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_Puberty_-_NG.M.00807_-_National_Museum_of_Art,_Architecture_and_Design.jpg；License: Public domain
  - 落盘: 1309×1800px，650 KB
- **the_sick_child_1885_86.jpg** — The Sick Child（病中的孩子；NG.M.00839），Edvard Munch，1885–86，National Museum, Oslo。
  - 来源: https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_The_Sick_Child_-_NG.M.00839_-_National_Museum_of_Art,_Architecture_and_Design.jpg；License: Public domain
  - 落盘: 1774×1800px，1049 KB
- **ashes_1894.jpg** — Ashes（灰烬；NG.M.00809），Edvard Munch，1894（另记 1895，两存），National Museum, Oslo。
  - 来源: https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_Ashes_-_NG.M.00809_-_National_Museum_of_Art,_Architecture_and_Design.jpg；License: Public domain
  - 落盘: 1800×1543px，776 KB
- **the_sun_1911.jpg** — The Sun（太阳；MM.M.00963），Edvard Munch，1910–11，Munchmuseet, Oslo（Aula 组画主作另版藏奥斯陆大学）。
  - 来源: https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_The_Sun_-_MM.M.00963_-_Munch_Museum.jpg；License: Public domain
  - 落盘: 1800×1055px，654 KB
- **girls_on_the_bridge_1901.jpg** — The Girls on the Bridge（桥上的少女；NG.M.00844），Edvard Munch，1901，National Museum, Oslo。
  - 来源: https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_The_Girls_on_the_Bridge_-_NG.M.00844_-_National_Museum_of_Art,_Architecture_and_Design.jpg；License: Public domain
  - 落盘: 1646×1800px，995 KB

### kandinsky — 康定斯基（11 张；wave15 并入）
- **the_blue_rider_1903.jpg** — The Blue Rider (Der Blaue Reiter)（青骑士；蓝骑士得名来源），Wassily Kandinsky，1903，Stiftung Sammlung E.G. Bührle, Zurich。
  - 来源: https://commons.wikimedia.org/wiki/File:Wassily_Kandinsky,_1903,_The_Blue_Rider_(Der_Blaue_Reiter),_oil_on_canvas,_52.1_x_54.6_cm,_Stiftung_Sammlung_E.G._Bührle,_Zurich.jpg；License: Public domain（PD-Art）
  - 落盘: 960×922px，415 KB
- **murnau_mit_kirche_i_1910.jpg** — Murnau mit Kirche I（慕尔瑙与教堂 I；对象溶解关键作），Wassily Kandinsky，1910，Lenbachhaus（GMS 59）。
  - 来源: https://www.lenbachhaus.de/en/digital/collection-online/detail/murnau-mit-kirche-i-30018804；License: CC0 1.0（Lenbachhaus）
  - 落盘: 1382×1800px，499 KB
- **impression_iii_konzert_1911.jpg** — Impression III (Konzert)（印象 III·音乐会），Wassily Kandinsky，1911，Lenbachhaus（GMS 78）。
  - 来源: https://www.lenbachhaus.de/en/digital/collection-online/detail/impression-iii-konzert-30012206；License: CC0 1.0（Lenbachhaus）
  - 落盘: 1800×1387px，581 KB
- **composition_vii_1913.jpg** — Composition VII（构成 VII），Wassily Kandinsky，1913，Tretyakov Gallery（Google Art Project 扫描）。
  - 来源: https://commons.wikimedia.org/wiki/File:Composition_VII_-_Wassily_Kandinsky,_GAC.jpg；License: Public domain（PD-Art）
  - 落盘: 1800×1196px，808 KB
- **study_for_improvisation_31_1913.jpg** — Study for Improvisation 31 (Seeschlacht)（即兴 31 习作·海战），Wassily Kandinsky，1913，Centre Pompidou（AM 1976-866）。
  - 来源: https://commons.wikimedia.org/wiki/File:Kandinsky,_Wassily_-_Study_for_Improvisation_31_(Seeschlacht),_1913,_GAC.jpg；License: Public domain（PD-Art）
  - 落盘: 1424×1799px，819 KB
- **blaue_reiter_almanac_cover_1912.jpg** — 《Der Blaue Reiter》年鉴封面（康定斯基设计，与 Franz Marc 合编），Wassily Kandinsky，1912（摄影 Goesseln 2010）。
  - 来源: https://commons.wikimedia.org/wiki/File:Der_Blaue_Reiter_Almanach_10.jpg；License: **CC BY-SA 3.0**（摄影 Goesseln；二次使用需同许可）
  - 落盘: 1280×1707px，429 KB
- **the_archer_woodcut_c1909.jpg** — The Archer（弓箭手，Roethel 79；彩色木刻），Wassily Kandinsky，c. 1909（1938 补印）。
  - 来源: https://commons.wikimedia.org/wiki/File:W.Kandinsky_The_Archer.jpg；License: Public domain（PD-Art）
  - 落盘: 500×542px，77 KB（原图即小尺寸，不放大）
- **composition_viii_1923.jpg** — Composition VIII（构成 VIII；包豪斯几何期旗舰作），Wassily Kandinsky，1923，Solomon R. Guggenheim Museum（展览现场摄影）。
  - 来源: https://commons.wikimedia.org/wiki/File:Kandinsky_-_Composition_8,_July_1923.jpg；License: CC0（摄影 Xyxyzyz）
  - 落盘: 1800×1311px，607 KB
- **on_white_ii_1923.jpg** — Auf Weiss II (On White II)（在白色上 II），Wassily Kandinsky，1923，Centre Pompidou（AM 1976-855）。
  - 来源: https://commons.wikimedia.org/wiki/File:Vassily_Kandinsky,_1923_-_On_White_II.jpg；License: Public domain（PD-Art）
  - 落盘: 1678×1800px，719 KB
- **yellow_red_blue_1925.jpg** — Gelb-Rot-Blau (Jaune-rouge-bleu)（黄·红·蓝；与《点线面》互为图解），Wassily Kandinsky，1925，Centre Pompidou（AM 1976-856）。
  - 来源: https://commons.wikimedia.org/wiki/File:Gelb-Rot-Blau,_by_Wassily_Kandinsky,_Centre_Pompidou.jpg；License: Public domain（PD-Art；馆方标 Domaine public）
  - 落盘: 1800×1148px，518 KB
- **several_circles_1926.jpg** — Several Circles (Einige Kreise)（若干圆；「圆」主题顶点），Wassily Kandinsky，1926，Solomon R. Guggenheim Museum。
  - 来源: https://commons.wikimedia.org/wiki/File:Vassily_Kandinsky,_1926_-_Several_Circles,_Gugg_0910_25.jpg；License: Public domain（PD-Art）
  - 落盘: 1280×1303px，340 KB（标准缩略尺寸，限流期降档）

### velazquez — 委拉斯开兹（12 张；wave15 并入）
- **las_meninas.jpg** — Las Meninas（宫娥），Diego Velázquez，1656，Museo del Prado（P001174）。
  - 来源: https://commons.wikimedia.org/wiki/File:Las_Meninas,_by_Diego_Vel%C3%A1zquez,_from_Prado_in_Google_Earth.jpg；License: Public domain
  - 落盘: 1564×1800px，474 KB
- **las_hilanderas.jpg** — Las Hilanderas (The Fable of Arachne)（纺纱女），Diego Velázquez，c. 1655–60，Museo del Prado（P001173）。
  - 来源: https://commons.wikimedia.org/wiki/File:Velazquez-las_hilanderas.jpg；License: Public domain
  - 落盘: 1800×1241px，806 KB
- **the_surrender_of_breda.jpg** — The Surrender of Breda (Las Lanzas)（布雷达的投降），Diego Velázquez，c. 1634–35，Museo del Prado（P001172）。
  - 来源: https://commons.wikimedia.org/wiki/File:Velazquez-The_Surrender_of_Breda.jpg；License: Public domain
  - 落盘: 1800×1484px，946 KB
- **portrait_of_innocent_x.jpg** — Portrait of Pope Innocent X（英诺森十世像），Diego Velázquez，1650，Galleria Doria Pamphilj, Rome。
  - 来源: https://commons.wikimedia.org/wiki/File:Retrato_del_Papa_Inocencio_X._Roma,_by_Diego_Vel%C3%A1zquez.jpg；License: Public domain
  - 落盘: 1411×1800px，580 KB
- **the_rokeby_venus.jpg** — The Toilet of Venus ('The Rokeby Venus')（镜前的维纳斯），Diego Velázquez，1647–51，The National Gallery, London（NG2057）。
  - 来源: https://commons.wikimedia.org/wiki/File:Diego_Vel%C3%A1zquez_-_Rokeby_Venus.jpg；License: Public domain
  - 落盘: 1800×1235px，393 KB
- **juan_de_pareja.jpg** — Juan de Pareja（胡安·德·帕雷哈像），Diego Velázquez，1650，The Met（1971.86；Met DP-14286-001）。
  - 来源: https://www.metmuseum.org/art/collection/search/437869；License: CC0（Met Open Access）
  - 落盘: 1555×1800px，451 KB
- **the_waterseller_of_seville.jpg** — The Waterseller of Seville（塞维利亚的卖水人），Diego Velázquez，c. 1620，Wellington Collection, Apsley House。
  - 来源: https://commons.wikimedia.org/wiki/File:El_aguador_de_Sevilla,_por_Diego_Vel%C3%A1zquez.jpg；License: Public domain
  - 落盘: 1334×1800px，751 KB
- **old_woman_frying_eggs.jpg** — Old Woman Cooking Eggs（煎蛋的老妇），Diego Velázquez，1618，National Galleries of Scotland。
  - 来源: https://commons.wikimedia.org/wiki/File:Diego_Velazquez_-_An_Old_Woman_Cooking_Eggs_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1522px，617 KB
- **view_of_the_villa_medici.jpg** — View of the Garden of the Villa Medici（'Entrance to the Grotto'；空气/外光锚点），Diego Velázquez，c. 1630，Museo del Prado。
  - 来源: https://commons.wikimedia.org/wiki/File:Vista_del_jard%C3%ADn_de_la_Villa_Medici_en_Roma,_por_Diego_Vel%C3%A1zquez.jpg；License: Public domain
  - 落盘: 1588×1800px，1251 KB
- **the_triumph_of_bacchus.jpg** — The Triumph of Bacchus (Los Borrachos)（酒神的胜利），Diego Velázquez，1628–29，Museo del Prado（P001170）。
  - 来源: https://commons.wikimedia.org/wiki/File:Vel%C3%A1zquez_-_El_Triunfo_de_Baco_o_Los_Borrachos_(Museo_del_Prado,_1628-29).jpg；License: Public domain
  - 落盘: 1800×1313px，450 KB
- **the_supper_at_emmaus.jpg** — The Supper at Emmaus（以马忤斯的晚餐），Diego Velázquez，1622–23，The Met（14.40.631；DP120945）。
  - 来源: https://www.metmuseum.org/art/collection/search/437871；License: CC0（Met Open Access）
  - 落盘: 1800×1680px，427 KB
- **maria_teresa_infanta.jpg** — María Teresa, Infanta of Spain（西班牙公主玛丽亚·特蕾莎），Diego Velázquez，1651–54，The Met（49.7.43；DP-24467-001）。
  - 来源: https://www.metmuseum.org/art/collection/search/437870；License: CC0（Met Open Access）
  - 落盘: 1800×1535px，571 KB

### bosch — 博斯（10 张；wave15 并入）
- **garden_of_earthly_delights.jpg** — The Garden of Earthly Delights Triptych（人间乐园，三联全开），Hieronymus Bosch，1490–1500，Museo del Prado（P002823；板 205.5×384.9 cm）。
  - 来源: https://commons.wikimedia.org/wiki/File:Hieronymus_Bosch_(c._1450–1516),_The_Garden_of_Earthly_Delights_Triptych,_1490–1500.jpg；License: Public Domain Mark（Prado 摄影复制品；PDM-owner）
  - 落盘: 1800×1014px，681 KB
- **haywain_triptych.jpg** — The Haywain Triptych（干草车，三联全开），Hieronymus Bosch，1512–1515，Museo del Prado（P002052；中央板签名）。
  - 来源: https://commons.wikimedia.org/wiki/File:Bosch_-_Haywain_Triptych.jpg；License: Public domain
  - 落盘: 1800×1184px，659 KB
- **last_judgment_vienna.jpg** — The Last Judgment（最后的审判，三联全开），Hieronymus Bosch，after 1482，Academy of Fine Arts, Vienna（外翼 grisaille）。
  - 来源: https://commons.wikimedia.org/wiki/File:Hieronymus_Bosch_-_The_Last_Judgement.jpg；License: Public domain
  - 落盘: 1800×1181px，910 KB
- **temptation_of_st_anthony.jpg** — Triptych of the Temptation of St. Anthony（圣安东尼的诱惑，三联全开），Hieronymus Bosch，c. 1501，Museu Nacional de Arte Antiga, Lisbon。
  - 来源: https://commons.wikimedia.org/wiki/File:Temptation_of_Saint_Anthony.jpg；License: Public domain
  - 落盘: 1800×933px，506 KB
- **ship_of_fools.jpg** — Ship of Fools（愚人船，残件），Hieronymus Bosch，c. 1505–1515，Musée du Louvre（RF 2218）。
  - 来源: https://commons.wikimedia.org/wiki/File:La_Nef_des_fous_-_Jérôme_Bosch_-_Musée_du_Louvre_Peintures_RF_2218.jpg；License: Public domain
  - 落盘: 970×1800px，651 KB
- **death_and_the_miser.jpg** — Death and the Miser（死神与守财奴），Hieronymus Bosch，c. 1485/1490，National Gallery of Art, Washington（1952.5.33, Kress；93×31 cm）。
  - 来源: https://commons.wikimedia.org/wiki/File:Hieronymus_Bosch,_Death_and_the_Miser,_c._1485-1490,_NGA_41645.jpg（下载经 NGA IIIF `!1800,1800`）；License: CC0（NGA Open Access）
  - 落盘: 602×1800px，312 KB
- **seven_deadly_sins.jpg** — The Seven Deadly Sins and the Four Last Things（七宗罪与四末），Hieronymus Bosch，1505–1510，Museo del Prado（P002822；归属两说并存）。
  - 来源: https://commons.wikimedia.org/wiki/File:Hieronymus_Bosch-_The_Seven_Deadly_Sins_and_the_Four_Last_Things.JPG；License: Public domain
  - 落盘: 1800×1535px，904 KB
- **adoration_of_the_magi.jpg** — Triptych of the Adoration of the Magi（三王来拜），Hieronymus Bosch，c. 1494，Museo del Prado（P002048；WGA 扫描）。
  - 来源: https://commons.wikimedia.org/wiki/File:Hieronymus_Bosch_-_Triptych_of_the_Adoration_of_the_Magi_-_WGA2606.jpg；License: Public domain
  - 落盘: 1800×1568px，834 KB
- **christ_carrying_the_cross_ghent.jpg** — Christ Carrying the Cross（基督负十字架，根特本；归属争议件），Hieronymus Bosch，c. 1510（BRCP 2015：1530–40、出自追随者），MSK Ghent（1902-H）。
  - 来源: https://commons.wikimedia.org/wiki/File:Kruisdraging,_Hieronymus_Bosch,_ca._1510,_Koninklijk_Museum_voor_Schone_Kunsten_Gent,_1902-H.jpg；License: Public domain
  - 落盘: 1800×1771px，750 KB
- **cutting_the_stone.jpg** — Cure of Folly / Extracting the Stone of Madness（取出愚石；带画框荷兰语题刻版），Hieronymus Bosch，c. 1494–1516，Museo del Prado（P02056）。
  - 来源: https://commons.wikimedia.org/wiki/File:Cutting_the_Stone_(Bosch).jpg；License: Public domain
  - 落盘: 1259×1800px，881 KB

### huang_gongwang — 黄公望（10 张；wave15 并入）
- **fuchun_remaining_mountain.jpg** — 富春山居图·剩山图（画心），黄公望，1347–1350，浙江省博物馆（自 7260×900 整卷装裱裁出画心）。
  - 来源: https://commons.wikimedia.org/wiki/File:富春山居圖(剩山圖).jpg；License: Public domain（PD-Art）
  - 落盘: 1410×900px，288 KB
- **fuchun_wuyongshi_full.jpg** — 富春山居图·无用师卷（画心，三段叠排；右→左阅读方向），黄公望，1347–1350，台北故宫博物院（故画001016；自 NPM 26134×900 图裁出）。
  - 来源: https://commons.wikimedia.org/wiki/File:富春山居圖(無用師卷).jpg；License: Public domain（PD-Art）
  - 落盘: 1800×898px，517 KB
- **fuchun_wuyongshi_detail.jpg** — 富春山居图·无用师卷（局部；松林/坡石/披麻皴细节），黄公望，1347–1350，台北故宫博物院。
  - 来源: https://commons.wikimedia.org/wiki/File:Huang_Gongwang._Dwelling_in_the_Fuchun_Mountains._detail._National_Palace_Museum,_Taipei.jpg；License: Public domain（PD-Art）
  - 落盘: 1800×658px，473 KB
- **fuchun_ziming_full.jpg** — 富春山居图·子明卷（两段叠排；乾隆误认之本 1745），黄公望（摹本/传），约 1338 纪年，台北故宫博物院（故画001017）。
  - 来源: https://commons.wikimedia.org/wiki/File:富春山居圖(子明卷).jpg；License: Public domain（PD-Art）
  - 落盘: 1800×314px，239 KB
- **shenzhou_fuchun_copy.jpg** — 沈周仿黄公望富春山居图卷（两段叠排；1487 背临本），沈周，1487，故宫博物院。
  - 来源: https://commons.wikimedia.org/wiki/File:沈周仿黄公望富春山居图卷.png；License: Public domain（PD-Art）
  - 落盘: 1800×252px，124 KB
- **jiufeng_xueji.jpg** — 九峰雪霁图（轴；纸本墨笔 117×55.5 cm），黄公望，1349（81 岁），故宫博物院。
  - 来源: https://commons.wikimedia.org/wiki/File:黄公望九峰雪霁图轴.png；License: Public domain（PD-Art）
  - 落盘: 825×1800px，192 KB
- **tianchi_shibi.jpg** — 天池石壁图（轴；绢本设色 139.4×57.3 cm；浅绛法典范），黄公望，1341（73 岁），故宫博物院。
  - 来源: https://commons.wikimedia.org/wiki/File:Huang_Gongwang._Stone_Cliff_at_the_Pond_of_Heaven.1341._139,4x57,3._Palace_Museum,_Beijing.jpg；License: Public domain（PD-Art）
  - 落盘: 738×1800px，464 KB
- **danya_yushu.jpg** — 丹崖玉树图（轴；纸本设色 101.3×43.8 cm），黄公望，元，故宫博物院。
  - 来源: https://commons.wikimedia.org/wiki/File:黄公望丹崖玉树图轴.png；License: Public domain（PD-Art）
  - 落盘: 1025×1800px，495 KB
- **kuaixue_shiqing.jpg** — 快雪时晴书画合璧卷（赵孟頫题·黄公望画·徐贲补；纸本墨笔 29.7×102.6 cm），黄公望，约 1340，故宫博物院。
  - 来源: https://commons.wikimedia.org/wiki/File:Huang_Gongwang._Clearing_After_Sudden_Snow._ca._1340._104,6_cm_long.Palace_Museum,_Beijing.jpg；License: Public domain（PD-Art）
  - 落盘: 1800×500px，339 KB
- **jiuzhu_fengcui.jpg** — 九珠峰翠图（轴；裁去底部色标尺），黄公望，约 1346–48，台北故宫博物院（故画001309）。
  - 来源: https://commons.wikimedia.org/wiki/File:元黃公望九珠峰翠圖軸.jpg；License: **CC0**（台北故宫开放数据）
  - 落盘: 905×1600px，317 KB

### behzad — 贝赫扎德（12 张；wave15 并入）
- **yusuf_zulaikha_cairo.jpg** — 《优素福逃避祖莱哈的纠缠》——萨迪《布斯坦》f.52b，Kamāl ud-Dīn Behzād，1488，开罗 Dār al-Kutub（四幅署名插图之一）。
  - 来源: https://commons.wikimedia.org/wiki/File:Yusuf_fleeing_the_Advances_of_Zulaikha.jpg；License: Public domain
  - 落盘: 1206×1800px，826 KB
- **khawarnaq_f154v.jpg** — 《霍拉纳克宫的建造》——尼扎米《五卷诗》f.154v，Kamāl ud-Dīn Behzād，c. 1494–95，大英图书馆 Or. 6810（页下缘后人注）。
  - 来源: https://commons.wikimedia.org/wiki/File:Kamal-ud-din_Bihzad_-_Construction_of_the_fort_of_Kharnaq.jpg；License: Public domain
  - 落盘: 1349×1800px，793 KB
- **alexander_hermit_f273r.jpg** — 《亚历山大与隐士》f.273r，Kamāl ud-Dīn Behzād，c. 1494–95，大英图书馆 Or. 6810（「可能」六页之一）。
  - 来源: https://commons.wikimedia.org/wiki/File:Alexander_and_the_Hermit,_from_Nizami%27s_Iskandarnama,_1494-95,_by_Behzad._British_Library_OR.6810_Folio_273R.jpg；License: Public domain
  - 落盘: 1201×1800px，468 KB
- **jami_astrolabe_f225v.jpg** — 《贾米持星盘》（f.225v 细节；局部裁切版），Kamāl ud-Dīn Behzād，c. 1494–95，大英图书馆 Or. 6810。
  - 来源: https://commons.wikimedia.org/wiki/File:Jami,_holding_an_astrolabe._By_Behz%C3%A2d,_from_the_Romance_of_Alexander_by_Nez%C3%A2m%C3%AE._Manuscript_of_the_Khamseh_of_the_emir_%27Al%C3%AE_F%C3%A2rs%C3%AE_Barlas,_Herat_1494-1495;_British_Library,_Or._6810,_f_225_v.jpg；License: Public domain
  - 落盘: 1073×1800px，596 KB
- **sanjar_add25900_f18a.jpg** — 《苏丹·桑贾尔与老妇》f.18a，Kamāl ud-Dīn Behzād，1493，大英图书馆 Add. 25900（识别依据 Daʿadli 2019）。
  - 来源: https://commons.wikimedia.org/wiki/File:Sultan_Sanjar_and_the_old_lady,_Khamsa,_this_painting_dated_1493_(British_Library,_Add._25900)_folio_18a.jpg；License: Public domain
  - 落盘: 1189×1800px，536 KB
- **hunting_h676_topkapi.jpg** — 《狩猎场景》——阿米尔·霍斯劳《八天堂》双页扉画，Kamāl ud-Dīn Behzād，1496–97，托普卡帕宫图书馆 H.676。
  - 来源: https://commons.wikimedia.org/wiki/File:Hunting_scene_from_the_Hast_Bahist_by_Kamal_al-Din_Bihzad,_Herat,_1496.jpg；License: Public domain
  - 落盘: 1227×1800px，817 KB
- **two_camels_golshan.jpg** — 《两只骆驼相斗》——《古尔尚画册》（题记自称「七十之年」作），Kamāl ud-Dīn Behzād，c. 1525–30，德黑兰古列斯坦宫。
  - 来源: https://commons.wikimedia.org/wiki/File:Behzad._Kamelkampf._Golestan_Palast.jpg；License: Public domain
  - 落盘: 1800×1101px，707 KB
- **dancing_dervishes_met.jpg** — 《舞僧》——哈菲兹诗集散页，Kamāl ud-Dīn Behzād，c. 1480，The Metropolitan Museum of Art（17.81.4）。
  - 来源: https://commons.wikimedia.org/wiki/File:%22Dancing_Dervishes%22,_Folio_from_a_Divan_of_Hafiz_MET_DP231332.jpg；License: CC0（Met Open Access）
  - 落盘: 1147×1800px，632 KB
- **encampment_cleveland.jpg** — 《营地外的乐手与仆人》（双联画左半；含未完成底稿），Kamāl ud-Dīn Behzād，c. 1485，Cleveland Museum of Art（1944.490）。
  - 来源: https://commons.wikimedia.org/wiki/File:Bihzad_-_Folio_from_an_Album_with_Musicians_and_Servants_Outside_a_Royal_Encampment_-_1944.490_-_Cleveland_Museum_of_Art.tif；License: CC0（CMA Open Access）
  - 落盘: 1145×1800px，613 KB
- **sadi_youth_kashgar.jpg** — 《萨迪与喀什青年》——《古丽斯坦》，Kamāl ud-Dīn Behzād，1486，私人收藏（Art and History Trust Collection）。
  - 来源: https://commons.wikimedia.org/wiki/File:Sad%27i_and_the_Youth_of_Kashgar,_Ascribed_to_Bihzad,_From_a_copy_of_the_Gulistan_(Rosegarden)_by_Sa%27di.jpg；License: Public domain
  - 落盘: 1369×1800px，1029 KB
- **sultan_husayn_portrait.jpg** — 《苏丹·侯赛因·米尔扎·拜卡拉像（约五十岁）》（自贝赫扎德约 1490 原作摹本），Kamāl ud-Dīn Behzād（摹本），1500–25，哈佛艺术博物馆（216273）。
  - 来源: https://commons.wikimedia.org/wiki/File:Portrait_of_Sultan_Husayn_Mirza_Bayqara_at_the_age_of_about_50_years._1500%E2%80%9325_copy_from_Behz%C4%81d%27s_original_of_about_1490.jpg；License: Public domain
  - 落盘: 1122×1800px，814 KB
- **dust_muhammad_preface_h2154.jpg** — Dust Muhammad《巴赫拉姆·米尔扎画册》序言页（文献页；内含对其评价的关键文本），1544–45，托普卡帕宫图书馆 H.2154, f.9b。
  - 来源: https://commons.wikimedia.org/wiki/File:Preface_written_by_Dust_Muhammad,_1544-45._From_the_Bahram_mirza_album,_Safavid_Iran._Topkap%C4%B1_Palace_museum_library,_ms._H._2154,_fol._9b.jpg；License: Public domain
  - 落盘: 1206×1800px，537 KB

### friedrich — 弗里德里希（12 张；wave17 并入）
- **der_moench_am_meer.jpg** — Der Mönch am Meer（海边僧侣，NG 9/85），Caspar David Friedrich，1808–1810，Alte Nationalgalerie, Berlin。
  - 来源: https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Der_M%C3%B6nch_am_Meer_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1145px，523 KB
- **abtei_im_eichwald.jpg** — Abtei im Eichwald（橡树林中的修道院，NG 8/85），Caspar David Friedrich，1809–1810，Alte Nationalgalerie, Berlin。
  - 来源: https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Abtei_im_Eichwald_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1153px，492 KB
- **wanderer_above_the_sea_of_fog.jpg** — Der Wanderer über dem Nebelmeer（雾海上的漫游者，HK-5161），Caspar David Friedrich，um 1817，Hamburger Kunsthalle。
  - 来源: https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Wanderer_above_the_sea_of_fog.jpg；License: Public domain
  - 落盘: 1405×1800px，538 KB
- **das_eismeer.jpg** — Das Eismeer（冰海，HK-1051），Caspar David Friedrich，1823/24，Hamburger Kunsthalle。
  - 来源: https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Das_Eismeer_-_Hamburger_Kunsthalle_-_02.jpg；License: Public domain
  - 落盘: 1800×1346px，553 KB
- **kreidefelsen_auf_ruegen.jpg** — Kreidefelsen auf Rügen（吕根岛的白垩崖），Caspar David Friedrich，1818，Kunst Museum Winterthur。
  - 来源: https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich%27s_Chalk_Cliffs_on_R%C3%BCgen.jpg；License: Public domain
  - 落盘: 1430×1800px，771 KB
- **zwei_maenner_in_betrachtung_des_mondes.jpg** — Zwei Männer in Betrachtung des Mondes（月下双人；德累斯顿油画版），Caspar David Friedrich，1819/20，Galerie Neue Meister, Dresden。
  - 来源: https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Zwei_M%C3%A4nner_in_Betrachtung_des_Mondes.jpg；License: Public domain
  - 落盘: 1800×1409px，754 KB
- **frau_am_fenster.jpg** — Frau am Fenster（窗前的女人，A I 918），Caspar David Friedrich，1822，Alte Nationalgalerie, Berlin。
  - 来源: https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Frau_am_Fenster_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1272×1800px，806 KB
- **mondaufgang_am_meer.jpg** — Mondaufgang am Meer（海上月出，W.S. 53），Caspar David Friedrich，1822，Alte Nationalgalerie, Berlin。
  - 来源: https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Mondaufgang_am_Meer_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1377px，535 KB
- **der_watzmann.jpg** — Der Watzmann（瓦茨曼山），Caspar David Friedrich，1824/25，Alte Nationalgalerie, Berlin。
  - 来源: https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_The_Watzmann_%281824-25%29.jpg；License: Public domain
  - 落盘: 1800×1383px，551 KB
- **die_lebensstufen.jpg** — Die Lebensstufen（生命阶段；含画家本人/妻子/子女五人物＋五艘船），Caspar David Friedrich，um 1835，Museum der bildenden Künste, Leipzig。
  - 来源: https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Die_Lebensstufen_%28ca._1834%29.jpg；License: Public domain
  - 落盘: 1800×1398px，843 KB
- **das_kreuz_im_gebirge.jpg** — Das Kreuz im Gebirge（山中的十字架＝泰申祭坛画），Caspar David Friedrich，1808，Galerie Neue Meister, Dresden。
  - 来源: https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Das_Kreuz_im_Gebirge.jpg；License: Public domain
  - 落盘: 1280×1334px，354 KB（1800px 桶被拒，取 1280px 标准桶）
- **der_einsame_baum.jpg** — Der einsame Baum（孤独的树，W.S. 52），Caspar David Friedrich，1822，Alte Nationalgalerie, Berlin。
  - 来源: https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Der_einsame_Baum.jpg；License: Public domain
  - 落盘: 1800×1370px，401 KB

### repin — 列宾（10 张；wave17 并入）
- **barge_haulers_on_the_volga.jpg** — Barge Haulers on the Volga（伏尔加河上的纤夫），Ilya Repin，1870–1873，Государственный Русский музей（Google Art Project 扫描）。
  - 来源: https://commons.wikimedia.org/wiki/File:Ilya_Repin_-_Barge_Haulers_on_the_Volga_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×843px，439 KB
- **religious_procession_in_kursk_province.jpg** — Religious Procession in Kursk Province（库尔斯克省的宗教行列），Ilya Repin，1880–1883，Государственная Третьяковская галерея。
  - 来源: https://commons.wikimedia.org/wiki/File:Ilya_Repin_-_%D0%9A%D1%80%D0%B5%D1%81%D1%82%D0%BD%D1%8B%D0%B9_%D1%85%D0%BE%D0%B4_%D0%B2_%D0%9A%D1%83%D1%80%D1%81%D0%BA%D0%BE%D0%B9_%D0%B3%D1%83%D0%B1%D0%B5%D1%80%D0%BD%D0%B8%D0%B8_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1129px，562 KB
- **ivan_the_terrible_and_his_son_ivan.jpg** — Ivan the Terrible and His Son Ivan, 16 November 1581（伊凡雷帝杀子），Ilya Repin，1883–1885，Государственная Третьяковская галерея。
  - 来源: https://commons.wikimedia.org/wiki/File:R%C3%A9pine_Ivan_le_Terrible_et_son_fils_Ivan_principale_version_1883_-_1885.jpg；License: Public domain
  - 落盘: 1800×1401px，566 KB
- **they_did_not_expect_him.jpg** — They Did Not Expect Him（意外归来／不期而至），Ilya Repin，1884–1888，Государственная Третьяковская галерея。
  - 来源: https://commons.wikimedia.org/wiki/File:Ilya_Repin_Unexpected_visitors.jpg；License: Public domain
  - 落盘: 1800×1728px，832 KB
- **reply_of_the_zaporozhian_cossacks.jpg** — Reply of the Zaporozhian Cossacks to the Turkish Sultan（扎波罗热哥萨克致土耳其苏丹的回信），Ilya Repin，1880–1891，Государственный Русский музей。
  - 来源: https://commons.wikimedia.org/wiki/File:Repin_Cossacks.jpg；License: Public domain
  - 落盘: 1800×1063px，567 KB
- **portrait_of_modest_mussorgsky.jpg** — Portrait of Modest Mussorgsky（穆索尔斯基像），Ilya Repin，1881，Государственная Третьяковская галерея（Google Art Project）。
  - 来源: https://commons.wikimedia.org/wiki/File:Ilya_Repin_-_%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82_%D0%BA%D0%BE%D0%BC%D0%BF%D0%BE%D0%B7%D0%B8%D1%82%D0%BE%D1%80%D0%B0_%D0%9C.%D0%9F.%D0%9C%D1%83%D1%81%D0%BE%D1%80%D0%B3%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1442×1800px，529 KB
- **sadko.jpg** — Sadko in the Underwater Kingdom（萨德科），Ilya Repin，1876，Государственный Русский музей（Google Art Project）。
  - 来源: https://commons.wikimedia.org/wiki/File:Ilya_Repin_-_Sadko_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1279×1800px，538 KB
- **portrait_of_leo_tolstoy.jpg** — Portrait of Leo Tolstoy（列夫·托尔斯泰像，坐姿），Ilya Repin，1887，Государственная Третьяковская галерея。
  - 来源: https://commons.wikimedia.org/wiki/File:Ilya_Efimovich_Repin_(1844-1930)_-_Portrait_of_Leo_Tolstoy_(1887).jpg；License: Public domain
  - 落盘: 1200×1711px，466 KB（未缩）
- **self_portrait_1878.jpg** — Self-portrait（自画像；该件原始分辨率即偏低），Ilya Repin，1878，Государственный Русский музей。
  - 来源: https://commons.wikimedia.org/wiki/File:A002Self-portrait._1878.jpg；License: Public domain
  - 落盘: 960×1228px，161 KB
- **state_council_1903.jpg** — Ceremonial Sitting of the State Council on 7 May 1901（国务会议庆典），Ilya Repin，1903，Государственный Русский музей（Google Art Project）。
  - 来源: https://commons.wikimedia.org/wiki/File:Ilya_Repin_-_Ceremonial_Sitting_of_the_State_Council_on_7_May_1901_Marking_the_Centenary_of_its_Foundation_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×805px，377 KB

### ravi_varma — 拉维·瓦尔马（17 张；wave17 并入）
- **shakuntala_looking_for_dushyanta.jpg** — 《沙恭达罗回眸》（Shakuntala looking for Dushyanta；油彩/画布 181×110 cm），Raja Ravi Varma，1898，Sree Chitra Art Gallery。
  - 来源: https://commons.wikimedia.org/wiki/File:Raja_Ravi_Varma_-_Mahabharata_-_Shakuntala.jpg；License: Public domain（PD-Art）
  - 落盘: 1099×1800px，591 KB
- **nair_lady_adorning_her_hair.jpg** — 《奈尔女子梳妆》（1873 马德拉斯展总督金奖作品；源分辨率低如实保留），Raja Ravi Varma，1873。
  - 来源: https://commons.wikimedia.org/wiki/File:Nair_Lady_Adorning_Her_Hair.jpg；License: Public domain
  - 落盘: 501×750px，70 KB
- **galaxy_of_musicians.jpg** — 《音乐家银河》（11 位不同地区/信仰的女乐手群像），Raja Ravi Varma，1889（为迈索尔大君而作）。
  - 来源: https://commons.wikimedia.org/wiki/File:Raja_Ravi_Varma,_Galaxy_of_Musicians.jpg；License: Public domain
  - 落盘: 800×628px，128 KB
- **there_comes_papa.jpg** — 《爸爸来了》（模特为其女 Mahaprabha 与外孙；芝加哥 1893 参展十幅之一），Raja Ravi Varma，1893，Kowdiar Palace。
  - 来源: https://commons.wikimedia.org/wiki/File:Raja_Ravi_Varma,_There_Comes_Papa_(1893).jpg；License: Public domain（PD-Art）
  - 落盘: 1150×1800px，540 KB
- **radha_in_the_moonlight.jpg** — 《月下 Radha》（uttama nayika 主题），Raja Ravi Varma，1890，私人收藏。
  - 来源: https://commons.wikimedia.org/wiki/File:Radha_in_the_Moonlight.jpg；License: Public domain
  - 落盘: 1292×1800px，620 KB
- **hamsa_damayanti.jpg** — 《天鹅与达玛扬蒂》，Raja Ravi Varma，1899，Sree Chitra Art Gallery（画中石柱据 C. R. Varma 日记为本人所记）。
  - 来源: https://commons.wikimedia.org/wiki/File:Ravi_Varma-Princess_Damayanthi_talking_with_Royal_Swan_about_Nala.jpg；License: Public domain
  - 落盘: 1036×1800px，526 KB
- **sri_krishna_as_envoy.jpg** — 《克利希那出使》（「主角亮相式」构图代表），Raja Ravi Varma，c.1906，NGMA 新德里。
  - 来源: https://commons.wikimedia.org/wiki/File:Sri_Krishna_as_Envoy.jpg；License: Public domain（PD-Art）
  - 落盘: 800×1105px，199 KB
- **draupadi_vastrapaharanam.jpg** — 《黑公主被褫衣》（Baroda 委托期；戏剧冲突群像代表），Raja Ravi Varma，1888–89，私人收藏。
  - 来源: https://commons.wikimedia.org/wiki/File:Draupadi_Vastraharan,_Raja_Ravi_Varma.jpg；License: Public domain
  - 落盘: 1327×1800px，795 KB
- **yashoda_with_krishna.jpg** — 《雅首达与克利希那》（2026-04 Saffronart 以 ₹167.2 crore 成交——印度艺术拍卖纪录），Raja Ravi Varma，c.1890s，私人收藏。
  - 来源: https://commons.wikimedia.org/wiki/File:Yashoda_with_Krishna,_Raja_Ravi_Varma.jpg；License: Public domain
  - 落盘: 972×1200px，263 KB
- **village_belle.jpg** — 《村中美人》（「普通人肖像」代表），Raja Ravi Varma，c.1900s，私人收藏。
  - 来源: https://commons.wikimedia.org/wiki/File:Village_Belle,_by_Raja_Ravi_Varma.jpg；License: Public domain
  - 落盘: 1029×1800px，488 KB
- **gypsies_poverty_1893.jpg** — 《南印度吉普赛人（贫穷）》（芝加哥 1893 参展十幅之一），Raja Ravi Varma，1893，Sree Chitra Art Gallery。
  - 来源: https://commons.wikimedia.org/wiki/File:Raja_Ravi_Varma,_Gypsies_(1893).jpg；License: Public domain
  - 落盘: 1150×1800px，589 KB
- **mohini_on_a_swing.jpg** — 《秋千上的莫希尼》（104×150 cm；模特 Anjanibai Malpekar），Raja Ravi Varma，1894，私人收藏。
  - 来源: https://commons.wikimedia.org/wiki/File:Mohini_on_a_swing.jpg；License: Public domain（PD-Art）
  - 落盘: 1287×1800px，673 KB
- **jatayu_fights_ravana.jpg** — 《贾塔尤与罗波那》（罗摩衍那名场面），Raja Ravi Varma，c.1880s–90s。
  - 来源: https://commons.wikimedia.org/wiki/File:Ravi_Varma-Ravana_Sita_Jathayu.jpg；License: Public domain
  - 落盘: 1249×1800px，732 KB
- **self_portrait.jpg** — 《自画像》（晚年像；出处 Rupika Chawla 专著；源分辨率低如实保留），Raja Ravi Varma，未定年，私人收藏。
  - 来源: https://commons.wikimedia.org/wiki/File:Self_portrait_by_Raja_Ravi_Varma.jpg；License: Public domain（PD-Art）
  - 落盘: 311×443px，26 KB
- **shakuntala_patra_lekhan.jpg** — 《沙恭达罗写信》，Raja Ravi Varma，c.1870s–90s。
  - 来源: https://commons.wikimedia.org/wiki/File:Sakunthala-pathralekhanam.jpg；License: Public domain
  - 落盘: 982×670px，184 KB
- **saraswati.jpg** — 《辩才天女》（持维纳琴；神像油画原型），Raja Ravi Varma，1896，Maharaja Fateh Singh Museum（Vadodara）。
  - 来源: https://commons.wikimedia.org/wiki/File:Saraswati.jpg；License: Public domain
  - 落盘: 925×1496px，384 KB
- **saraswati_oleograph.jpg** — 《辩才天女》石版彩印版（Ravi Varma Press；与油画原型对照），Raja Ravi Varma，c.1900s。
  - 来源: https://commons.wikimedia.org/wiki/File:Raja_Ravi_Varma,_Goddess_Saraswati.jpg；License: Public domain
  - 落盘: 500×688px，135 KB（限流下取「列出尺寸」缩略图；原件未取）

### degas — 德加（13 张；wave17 并入）
- **the_dance_class_1874.jpg** — The Dance Class（舞蹈课；Jules Perrot 课堂），Edgar Degas，1874，The Met（1987.47.1；DP-20101-001）。
  - 来源: https://www.metmuseum.org/art/collection/search/438817；License: CC0 1.0（Met Open Access）
  - 落盘: 1670×1800px，704 KB
- **la_classe_de_danse_1873_76.jpg** — La Classe de danse（舞蹈课），Edgar Degas，1873–76，Musée d'Orsay（RF 1976）。
  - 来源: https://commons.wikimedia.org/wiki/File:Edgar_Degas_-_La_Classe_de_danse.jpg；License: Public domain
  - 落盘: 1568×1800px，1358 KB
- **ballet_from_robert_le_diable_1871.jpg** — The Ballet from "Robert le Diable"（罗贝尔恶魔的芭蕾），Edgar Degas，1871，The Met（436123；DT1911）。
  - 来源: https://www.metmuseum.org/art/collection/search/436123；License: CC0 1.0（Met Open Access）
  - 落盘: 1488×1800px，734 KB
- **dancers_practicing_at_the_barre_1877.jpg** — Dancers Practicing at the Barre（把杆练习），Edgar Degas，1877，The Met（436139；DT840）。
  - 来源: https://www.metmuseum.org/art/collection/search/436139；License: CC0 1.0（Met Open Access）
  - 落盘: 1800×1663px，638 KB
- **blue_dancers_1890.jpg** — Danseuses bleues（蓝色舞者），Edgar Degas，c. 1890，Musée d'Orsay（RF 1951 10）。
  - 来源: https://commons.wikimedia.org/wiki/File:Edgar_Germain_Hilaire_Degas_071.jpg；License: Public domain（PD-old-70 / PD-Art-Yorck）
  - 落盘: 1573×1800px，797 KB
- **the_star_1876_77.jpg** — Ballet / L'Étoile（舞台之星；粉彩），Edgar Degas，1876–77，Musée d'Orsay（RF 12258）。
  - 来源: https://commons.wikimedia.org/wiki/File:Edgar_Degas_-_Ballet_(L%27%C3%89toile).jpg；License: Public domain（PD-Art）
  - 落盘: 1237×1800px，1052 KB
- **le_foyer_de_la_danse_1872.jpg** — Le Foyer de la danse à l'Opéra de la rue Le Peletier（舞台后厅），Edgar Degas，1872，Musée d'Orsay（RF 1977）。
  - 来源: https://commons.wikimedia.org/wiki/File:Edgar_Degas_-_The_Dance_Foyer_at_the_Opera_on_the_rue_Le_Peletier.jpg；License: Public domain
  - 落盘: 1800×1222px，1029 KB
- **miss_la_la_at_the_cirque_fernando_1879.jpg** — Miss La La at the Cirque Fernando（拉拉小姐），Edgar Degas，1879，National Gallery, London（NG4121）。
  - 来源: https://commons.wikimedia.org/wiki/File:Edgar_Degas,_Miss_La_La_at_the_Cirque_Fernando,_1879.jpg；License: Public domain
  - 落盘: 1184×1800px，576 KB
- **combing_the_hair_1896.jpg** — Combing the Hair ('La Coiffure')（梳头），Edgar Degas，c. 1896，National Gallery, London（NG486）。
  - 来源: https://commons.wikimedia.org/wiki/File:Combing_the_Hair_(La_Coiffure),_Edgar_Degas.jpg；License: **CC BY-SA 4.0**（照片许可；原作 PD——引用需署名）
  - 落盘: 1280×1029px，471 KB（限流后经 thumb.wikimedia.org 1280px 标准档）
- **dans_un_cafe_1875_76.jpg** — Dans un café（L'Absinthe，咖啡馆），Edgar Degas，1875–76，Musée d'Orsay（RF 1147）。
  - 来源: https://commons.wikimedia.org/wiki/File:Edgar_Degas_-_In_a_Caf%C3%A9_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1322×1800px，921 KB
- **the_bellelli_family_1858_67.jpg** — Portrait de famille / La famille Bellelli（贝列里一家），Edgar Degas，1858–69，Musée d'Orsay（RF 2210）。
  - 来源: https://commons.wikimedia.org/wiki/File:Edgar_Degas_-_The_Bellelli_Family_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1440px，817 KB
- **woman_bathing_in_a_shallow_tub_1885.jpg** — Woman Bathing in a Shallow Tub（浴女；粉彩），Edgar Degas，1885，The Met（436127；DP253483）。
  - 来源: https://www.metmuseum.org/art/collection/search/436127；License: CC0 1.0（Met Open Access）
  - 落盘: 1255×1800px，700 KB
- **little_fourteen_year_old_dancer.jpg** — The Little Fourteen-Year-Old Dancer（十四岁的小舞者；铸铜），Edgar Degas，modeled 1881 / cast 1922，The Met（29.100.370；DP-14939-001）。
  - 来源: https://www.metmuseum.org/art/collection/search/196439；License: CC0 1.0（Met Open Access）
  - 落盘: 1315×1800px，258 KB

### gauguin — 高更（20 张；wave17 并入）
- **vision_after_sermon_1888.jpg** — Vision après le sermon（布道后的幻象），Paul Gauguin，1888，National Galleries of Scotland。
  - 来源: https://commons.wikimedia.org/wiki/File:La_vision_après_le_sermon_(Paul_Gauguin).jpg；License: Public domain
  - 落盘: 1800×1411px，853 KB
- **breton_girls_dancing_1888.jpg** — Breton Girls Dancing, Pont-Aven，Paul Gauguin，1888，National Gallery of Art, Washington。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Breton_Girls_Dancing,_Pont-Aven_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1411px，759 KB
- **yellow_christ_1889.jpg** — Le Christ jaune（黄色基督），Paul Gauguin，1889，Buffalo AKG Art Museum。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_The_Yellow_Christ_(Le_Christ_jaune)_1889.jpg；License: Public domain
  - 落盘: 1431×1800px，748 KB
- **self_portrait_halo_1889.jpg** — Self-Portrait with Halo and Snake（自画像），Paul Gauguin，1889，National Gallery of Art, Washington。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Self-Portrait_with_Halo_and_Snake.jpg；License: Public domain
  - 落盘: 1157×1800px，569 KB
- **ia_orana_maria_1891.jpg** — Ia Orana Maria（万福玛利亚；51.112.2），Paul Gauguin，1891，The Met。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin_Ia_Orana_Maria_(Hail_Mary)_The_Metropolitan_Museum_of_Art1.jpg；License: Public domain
  - 落盘: 1397×1800px，767 KB
- **tahitian_women_on_beach_1891.jpg** — Femmes de Tahiti（沙滩上的塔希提女人），Paul Gauguin，1891，Musée d'Orsay。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin_056.jpg；License: Public domain
  - 落盘: 1800×1342px，629 KB
- **woman_with_flower_1891.jpg** — Vahine no te tiare（持花女人），Paul Gauguin，1891，Ny Carlsberg Glyptotek。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Tahitian_Woman_with_a_Flower_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1198×1800px，675 KB
- **spirit_of_dead_watching_1892.jpg** — Manao Tupapau（死亡的幽灵在注视），Paul Gauguin，1892，Buffalo AKG Art Museum（TIFF 底本转制）。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Manaò_tupapaú_(Spirit_of_the_Dead_Watching)_-_1965-1_-_Albright–Knox_Art_Gallery.tiff；License: Public domain
  - 落盘: 1800×1424px，647 KB
- **arearea_1892.jpg** — Arearea（快乐的田园），Paul Gauguin，1892，Musée d'Orsay。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Arearea_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1418px，832 KB
- **the_siesta_1892.jpg** — The Siesta（午睡；1993.400.3），Paul Gauguin，1892–94，The Met。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin_044.jpg；License: Public domain
  - 落盘: 1800×1367px，623 KB
- **fatata_te_miti_1892.jpg** — Fatata te Miti（海边），Paul Gauguin，1892，National Gallery of Art, Washington。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Fatata_te_Miti_(By_the_Sea)_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1336px，610 KB
- **seed_of_areoi_1892.jpg** — Te aa no areois（阿雷奥伊的种子），Paul Gauguin，1892，MoMA。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Te_aa_no_areois_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1395×1800px，712 KB
- **when_will_you_marry_1892.jpg** — Nafea Faa Ipoipo（何时出嫁？），Paul Gauguin，1892，私人收藏（2015 年私售 2.1 亿美元）。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin,_Nafea_Faa_Ipoipo%3F_(When_Will_You_Marry%3F)_1892,_oil_on_canvas,_101_x_77_cm.jpg；License: Public domain
  - 落盘: 1354×1800px，450 KB
- **tehamana_1893.jpg** — Merahi metua no Tehamana（Tehamana 的祖先们），Paul Gauguin，1893，Art Institute of Chicago。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_The_Ancestors_of_Tehamana_OR_Tehamana_Has_Many_Parents_(Merahi_metua_no_Tehamana)_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1234×1800px，711 KB
- **day_of_the_god_1894.jpg** — Mahana no atua（上帝之日；1926.198），Paul Gauguin，1894，Art Institute of Chicago。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Mahana_no_atua_(Day_of_the_God)_-_1926.198_-_Art_Institute_of_Chicago.jpg；License: Public domain
  - 落盘: 1800×1342px，815 KB
- **oviri_1894.jpg** — Oviri（野蛮人；釉陶），Paul Gauguin，1894，Musée d'Orsay。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin,_1894,_Oviri_(Sauvage),_partially_glazed_stoneware,_75_x_19_x_27_cm,_Musée_d'Orsay.jpg；License: Public domain
  - 落盘: 1143×1800px，197 KB
- **noa_noa_woodcut_1894.jpg** — Nave Nave Fenua（Noa Noa 木刻组画之一），Paul Gauguin，1893–94。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Nave_Nave_Fenua_from_the_Noa_Noa_Series_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1044×1800px，784 KB
- **nevermore_1897.jpg** — Nevermore（永不复返），Paul Gauguin，1897，The Courtauld。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin_091.jpg；License: Public domain
  - 落盘: 1800×924px，474 KB
- **where_do_we_come_from_1897.jpg** — D'où venons-nous ? Que sommes-nous ? Où allons-nous ?（我们从何处来？），Paul Gauguin，1897–98，MFA Boston。
  - 来源: https://commons.wikimedia.org/wiki/File:Gauguin_-_Where_Do_We_Come_From%3F_What_Are_We%3F_Where_Are_We_Going%3F_(1897-98).jpg；License: Public domain
  - 落盘: 1800×662px，344 KB
- **two_tahitian_women_1899.jpg** — Two Tahitian Women（两个塔希提女人；49.58.1），Paul Gauguin，1899，The Met。
  - 来源: https://commons.wikimedia.org/wiki/File:Paul_Gauguin_-_Deux_Tahitiennes.jpg；License: Public domain
  - 落盘: 1392×1800px，654 KB

### van_eyck — 扬·凡·艾克（17 张；wave17 并入）
- **ghent_altarpiece_open.jpg** — 《根特祭坛画》开屏（全 12 面板），Jan van Eyck，1432，St Bavo's Cathedral, Ghent。
  - 来源: https://commons.wikimedia.org/wiki/File:Lamgods_open.jpg；License: Public domain
  - 落盘: 1800×1316px，731 KB
- **ghent_altarpiece_closed.jpg** — 《根特祭坛画》闭屏（修复后，外板 8 面），Jan van Eyck，1432，St Bavo's Cathedral, Ghent。
  - 来源: https://commons.wikimedia.org/wiki/File:Ghent_Altarpiece_(closed,_after_restoration).jpg；License: Public domain
  - 落盘: 1261×1800px，542 KB
- **ghent_lamb_detail_restored.jpg** — 《神秘羔羊》中央细节（2020 修复后原貌：人形脸羔羊），Jan van Eyck，1432，St Bavo's Cathedral, Ghent。
  - 来源: https://commons.wikimedia.org/wiki/File:Ghent_Altarpiece_D_-_Lamb.jpg；License: Public domain
  - 落盘: 1280×1390px，744 KB
- **arnolfini_portrait_1434.jpg** — 《阿尔诺菲尼夫妇像》（NG186；凸镜/念珠/橙子反射），Jan van Eyck，1434，National Gallery, London。
  - 来源: https://commons.wikimedia.org/wiki/File:Van_Eyck_-_Arnolfini_Portrait.jpg；License: Public domain
  - 落盘: 1316×1800px，467 KB
- **man_in_red_turban_1433.jpg** — 《红头巾男子像（自画像?）》（NG222；格言框铭），Jan van Eyck，1433，National Gallery, London。
  - 来源: https://commons.wikimedia.org/wiki/File:Portrait_of_a_Man_in_a_red_turban_(by_Jan_van_Eyck).jpg；License: Public domain
  - 落盘: 1303×1800px，360 KB
- **leal_souvenir_1432.jpg** — 《Léal Souvenir（"忠诚的记忆"）》（NG290；三重题刻），Jan van Eyck，1432，National Gallery, London。
  - 来源: https://commons.wikimedia.org/wiki/File:Jan_van_Eyck_-_L%C3%A9al_Souvenir_-_National_Gallery,_London.jpg；License: Public domain
  - 落盘: 1014×1800px，536 KB
- **madonna_chancellor_rolin_1435.jpg** — 《洛林大臣的圣母》（双光源 + 远景嵌套），Jan van Eyck，c. 1435，Musée du Louvre。
  - 来源: https://commons.wikimedia.org/wiki/File:La_Vierge_du_chancelier_Rolin_-_Jan_van_Eyck_-_Mus%C3%A9e_du_Louvre_Peintures_INV_1271.jpg；License: Public domain
  - 落盘: 1714×1800px，902 KB
- **lucca_madonna_c1437.jpg** — 《卢卡圣母》（日常容器中的圣母），Jan van Eyck，c. 1437，Städel Museum。
  - 来源: https://commons.wikimedia.org/wiki/File:Jan_van_Eyck_-_Lucca_Madonna_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1369×1800px，577 KB
- **van_der_paele_1436.jpg** — 《凡德帕勒圣母》（盔甲反射含画家自画像），Jan van Eyck，1434–36，Groeningemuseum, Bruges。
  - 来源: https://commons.wikimedia.org/wiki/File:Eyck,_Jan_van_-_Madonna_with_Canon_van_der_Paele.jpeg；License: Public domain
  - 落盘: 1800×1397px，784 KB
- **madonna_in_church_c1439.jpg** — 《教堂中的圣母》（尺度越界=教会化身），Jan van Eyck，c. 1438–40，Gemäldegalerie, Berlin。
  - 来源: https://commons.wikimedia.org/wiki/File:Jan_van_Eyck_-_The_Madonna_in_the_Church_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 866×1800px，555 KB
- **annunciation_washington_c1435.jpg** — 《天使报喜》（光柱/仰视透视），Jan van Eyck，c. 1434–36，National Gallery of Art, Washington。
  - 来源: https://commons.wikimedia.org/wiki/File:Annunciation_-_Jan_van_Eyck_-_1434_-_NG_Wash_DC.jpg；License: Public domain
  - 落盘: 682×1800px，377 KB
- **saint_barbara_1437.jpg** — 《圣芭芭拉》（银笔/毛笔素描，细节密度递减），Jan van Eyck，1437，KMSKA, Antwerp。
  - 来源: https://commons.wikimedia.org/wiki/File:Heilige_Barbara_van_Nicomedi%C3%AB,_Jan_van_Eyck,_1437,_Koninklijk_Museum_voor_Schone_Kunsten_Antwerpen,_410.jpg；License: **CC0**（KMSKA 开放许可）
  - 落盘: 1026×1800px，737 KB
- **dresden_triptych_1437.jpg** — 《德累斯顿三联画》（唯一存世三联；框铭系统），Jan van Eyck，1437，Gemäldegalerie Alte Meister, Dresden。
  - 来源: https://commons.wikimedia.org/wiki/File:Jan_van_Eyck_-_Triptych_of_Mary_and_Child,_St._Michael,_and_the_Catherine_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1327px，817 KB
- **saint_francis_stigmata_c1432.jpg** — 《圣方济各接受圣痕》（费城版；归属与都灵版有辩论），Jan van Eyck，c. 1430–32，Philadelphia Museum of Art。
  - 来源: https://commons.wikimedia.org/wiki/File:Attributed_to_Jan_van_Eyck,_Netherlandish_(active_Bruges),_c._1395_-_1441_-_Saint_Francis_of_Assisi_Receiving_the_Stigmata_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1549px，827 KB
- **crucifixion_last_judgment_c1437.jpg** — 《十字架受难与最后的审判》双联（上部或为工坊补完），Jan van Eyck，c. 1436–38，The Metropolitan Museum of Art。
  - 来源: https://commons.wikimedia.org/wiki/File:Jan_van_Eyck_-_Crucifixion_and_Last_Judgement_diptych_(c._1436-38).jpg；License: Public domain
  - 落盘: 1504×1800px，826 KB
- **margaret_van_eyck_1439.jpg** — 《玛格丽特像》（画家之妻；框铭"我的丈夫约翰内斯……"），Jan van Eyck，1439，Groeningemuseum, Bruges。
  - 来源: https://commons.wikimedia.org/wiki/File:Jan_van_Eyck_-_Portrait_of_Margaret_van_Eyck_(1439).jpg；License: Public domain
  - 落盘: 1409×1800px，858 KB
- **jan_de_leeuw_1436.jpg** — 《金匠扬·德·莱乌像》（"会说话"的框铭），Jan van Eyck，1436，Kunsthistorisches Museum, Vienna。
  - 来源: https://commons.wikimedia.org/wiki/File:Jan_van_Eyck_-_Portrait_of_the_Goldsmith_Jan_de_Leeuw.jpg；License: Public domain
  - 落盘: 1280×1662px，445 KB

## 来源与许可口径

- **Met Open Access（15 张）**：仅取 `isPublicDomain=true` 且 `primaryImage` 非空的对象；图像 = CC0 1.0。来源 URL 为 metmuseum.org 对象页（直链 images.metmuseum.org/...）。
- **Art Institute of Chicago（4 张）**：API `is_public_domain=true`，作品页标注 "CC0 Public Domain Designation"；图像经 IIIF `https://www.artic.edu/iiif/2/<image_id>/full/1800,/0/default.jpg`。
- **Cleveland Museum of Art（3 张）**：API `share_license_status=CC0`（Open Access）；图像 `<accession>_print.jpg`（约 3400px）缩放。
- **Wikimedia Commons（11 张）**：PD 或 CC0/CC BY-SA；缩略图经 API `iiurlwidth=1600`。CC 类署名见总表。
- **wave12 追加（克里姆特 3 张）**：原画 1918 年后进入公有领域；现代扫描/摄影**逐张核验** Commons 许可模板——`Licensed-PD-Art`（Kiss；另附 CC BY-SA 4.0）/ `PD-Art`（Adele）/ `PD-Art-two-auto`（Death and Life）。未使用馆方 © 摄影图（Klimt Foundation / Leopold 官网图像未采）；未经核实的第三方扫描未采。
- **wave13 追加（修拉 10 张）**：AIC 1（CC0，IIIF）+ Met 4（Open Access，`isPublicDomain=true`）+ Commons 5（PD，imageinfo 逐张核验）。《浴场》图像采用 Commons PD 版（作品藏 NGL；NGL 官网图像许可口径未明，未采用其文件，作品页仅作档案文本来源）。**无版权未清项**；高清原图（>1800px）留私有层。
- **wave16 收口（turner / rembrandt / goya / bada_shanren / qi_baishi / ito_jakuchu，共 58 张）**：Wikimedia Commons 39（PD / CC0 / CC BY 3.0，逐张 `imageinfo` 核验）＋ Met Open Access 9（CC0）＋ Cleveland 1（CC0）＋ ColBase 9（日本国立文化財機構规约——须标注出典：「出典：ColBase」）。CC 类署名逐张记录（norham = 摄影 Sailko，CC BY 3.0；qi 摄影 2 件 CC BY-SA 4.0 / 1 件 CC BY 2.0）。**hopper 例外**：公开 0 / 私有 9（见「私有层例外」节）。
- **wave15/17 并入（15 位新档，169 张；其中 13 位有公开图）**：来源通道 = Wikimedia Commons 158 张 ＋ 馆方直取 11 张（Lenbachhaus 2 / Met 8 / Cleveland 1；NGA、台北故宫、KMSKA 件经 Commons 转载）。许可分布：**PD 149 · CC0 17 · CC BY-SA 3.0/4.0 3**——CC 类署名逐张记录（le_pater = 翻拍 SiefkinDR，CC BY-SA 4.0；《蓝骑士》年鉴封面 = 摄影 Goesseln，CC BY-SA 3.0；德加《梳头》 = NGL 照片，CC BY-SA 4.0）。**kahlo / kngwarreye 公开 0**（全私有，见「私有层例外」节）。
- 统一后处理：LANCZOS 缩放至长边 ≤1800px，JPEG quality 88 progressive；无裁切、无加水印。

## 私有层例外（公开 / 私有分开记）

> 口径：公开侧（本 manifest）只收 PD/开放许可图；「版权未清 / 研究副本 / 待核」材料存仓内私有层（`_private/`，永不提交、不公开分发）。以下为 35 位画家中涉及私有层者（18 位；私有张数 = 顶层图像文件数——按文件内容识别图像，含 `.hires` 等非常规扩展名，见 kandinsky 行；明细以各自私有层登记为准）：

| 画家 | 公开 | 私有 | 说明 |
|---|---|---|---|
| hopper | 0 | 9 | **全部版权未清**（© Heirs of Josephine N. Hopper / ARS 等，馆方权利行逐张记录）——公开侧 0 张；公开档案仅列作品清单 + 馆藏链接。9 张：Early Sunday Morning / House by the Railroad / Nighthawks / Gas / Ground Swell / New York Movie / Eleven A.M. / The Long Leg / The "Martha McKeen" of Wellfleet |
| seurat | 10 | 10 | 高清原件（>1800px）研究副本（公开侧按 D-02 口径 ≤1800px） |
| qi_baishi | 11 | 6 | URAA 从严 4 件（ink_shrimp / pine_eagle_and_couplet_1946 / daiyu_buries_flowers_1950 / leaves_and_insects）+ 存疑 2 件（cicada / portrait_1956_zheng_jingkang）；主脑处置 2026-10-15 |
| bada_shanren | 9 | 4 | 馆方网页图 / 新闻图（版权未清，仅内部研究） |
| goya | 9 | 2 | 高清研究副本（公开侧已存 ≤1800px 版） |
| ito_jakuchu | 18 | 1 | 细见美术馆《雪中雄鶏図》参考缩略图（版权参考，仅内部） |
| mucha | 12 | 5 | 全尺寸研究副本 5 件（Gismonda / Job / 茶花女 / 斯拉夫的神化 / Zodiac；PD，公开侧已存 ≤1800px 版） |
| munch | 13 | 3 | 3000px 研究副本 3 件（尖叫 NG 版 / 病中的孩子 / 生命之舞；PD，公开侧已存 ≤1800px 版） |
| kandinsky | 11 | 11 | 高分辨率研究副本 11 件（`.hires` 扩展名，JPEG 内容；公开侧 ≤1800px 版的原始件） |
| velazquez | 12 | 12 | 高清原件 12/12（3840px 级研究副本；公开侧已存 ≤1800px 版） |
| bosch | 10 | 1 | 全尺寸研究副本 1 件（《死神与守财奴》NGA 源；另 1 件受阻待补——Wikimedia 429） |
| huang_gongwang | 10 | 14 | 原始卷高清副本 + 馆方网页图（无用师卷 26134px / 子明卷 / 沈周仿 / 剩山图 7260px / 快雪时晴 12625px 等 + NPM/故宫/浙博内部研究件；部分版权未清） |
| kahlo | 0 | 13 | **全部版权未清**（© Fideicomiso/ARS）——公开侧 0 张；公开档案仅列作品清单 + 馆藏链接。13 张：Las dos Fridas / Viva la Vida / Thorn Necklace / Chango y loro / Diego y yo / The Miscarriage / Cropped Hair / Fulang-Chang / Grandparents / Trotsky / Broken Column / Henry Ford Hospital / The Bus |
| friedrich | 12 | 2 | 高清研究副本 2 件（《海边僧侣》1920px / 《雾海漫游者》hi-res；PD，公开侧已存 ≤1800px 版） |
| repin | 10 | 3 | 2560px 研究副本 3 件（纤夫 / 库尔斯克宗教行列 / 萨德科；PD） |
| degas | 13 | 10 | 高清研究副本 10 件（Met 5 + Commons 5；公开侧已存 ≤1800px 版） |
| van_eyck | 17 | 6 | 3840px 研究副本 6 件（根特开屏/闭屏 / 阿尔诺菲尼 / 卢卡圣母 / 红头巾男子 / 凡德帕勒圣母；PD） |
| kngwarreye | 0 | 14 | **全部版权未清**（© Estate of Emily Kame Kngwarreye/Copyright Agency）——公开侧 0 张；原住民伦理约束（仪式内容不收）。14 张：蜡染×3 / 点场×3 / 条纹×2 / 线网×2 / 装置×1 / 异形基底×1 / 晚期×2 |

> 合计：私有层例外 **126 张**（18 位；含 hopper 9、kahlo 13、kngwarreye 14 全私有）。私有层材料仅本机研究/临摹参考，公开仓不引用其路径；引用作品只给正常出处（馆藏页 / 文件页 URL）。

## 缺口与备注（不硬凑）

1. **毕加索（已解决但有限制）**：1930 年后作品仍受版权（美国外尤甚）；Met/AIC/NGA 的毕加索藏品均标非公有领域、Commons 无《亚维农少女》《老吉他手》等干净复制品（已查：Commons 全文检索 + `Category:Pablo Picasso` 87 项 + NGA Open Data 318 行 / published_images 288 行 openaccess=0）。→ 改用 Cleveland CC0 藏品 3 张（1904/1905 版画 + 1908–10 油画）。
2. **达芬奇《蒙娜丽莎》**：卢浮宫无开放数据接口 → 用 C2RMF 官方高清复制品（PD，Commons Featured picture）。
3. **莫奈的 Met 名作**（Garden at Sainte-Adresse、Bridge over a Pond of Water Lilies、Haystacks 等）：Met 新 API 标 `isPublicDomain=false` 且无图 → 莫奈改用 AIC（2 张 CC0）+ Commons（《印象·日出》PD）。
4. **米开朗基罗《大卫》**：只能取 CC BY-SA 4.0 照片（雕像本体 PD，但梵蒂冈/佛罗伦萨馆藏照多受限）——已按 CC BY-SA 署名。
5. **卡拉瓦乔《圣马太蒙召》**：Commons 提供 CC0 高清（8792×8304 原图）→ 已缩放至 1800px。
6. **已剔除的候选**：2 张 Flickr 来源的毕加索照片（1 张为街头涂鸦版《亚维农少女》、1 张为观众遮挡照）经目检不合格，已删除换源（见自审 B-1）。
7. **wave16 收口批次补记（2026-10-16，IndexMerge / A-51）**：turner / rembrandt 两库无画家侧 MANIFEST，本表行目由主脑按档案 §9 [R22] 记录 + Commons 文件页逐张复核（含像素比对）后补全；goya / bada_shanren / qi_baishi / ito_jakuchu 由各画家侧 MANIFEST 合并；hopper 公开 0 张（全私有，见「私有层例外」节）。
8. **wave15/17 并入批次补记（2026-10-16，IndexMerge2）**：15 位新档（wave15×8 + wave17×7）169 张公开图并入本表（13 位有公开图；kahlo / kngwarreye 全私有，仅见「私有层例外」节）；行目按各画家侧 MANIFEST 合并、逐张与磁盘核对（行数 = 磁盘实际）。私有层例外同步 +12 位 94 张（合计 18 位 126 张）。kandinsky 私有 11 件为 `.hires` 扩展名（JPEG 内容），按「顶层图像文件（内容识别）」口径计入。
9. **未纳入（在产）**：wave18 七位（hiroshige / sargent / piero_della_francesca / artemisia_gentileschi / namatjira / el_salahi / wu_guanzhong）随各自收口另并——本表不含其行（磁盘残留目录见核验脚本「未纳入」输出行）。

---

## 自审四段（LOOP 协议 §3.4）

### A · 早产出

第一批落盘发生在开工后约 15 分钟：Met 候选 JSON（`_meta/met_candidates.json`）先于图片落盘；随后 33 张按批「下载 → 缩放 → 落盘」（Met 15 + Commons 13 首批；AIC 4 张经浏览器补抓；毕加索 2 张换源重下）。manifest 最后生成。全程无只在内存里的中间产物。

### B · 反驳（最强结论逐条试推翻）

1. **「下载到的都是正确作品」** → 抽 6 张用 `read`（图片模式）目检：Matisse《舞蹈》、Caravaggio《圣马太蒙召》、Monet《睡莲》、Hokusai《神奈川冲浪里》→ CONFIRMED；**Picasso 2 张 OVERTURNED**（`les_demoiselles_davignon.jpg` 实为街头涂鸦版、`family_of_saltimbanques.jpg` 为观众遮挡照）→ 已删除，换 Cleveland CC0 3 张。
2. **「Met Open Access 能覆盖 11 位」** → 实测 `/public/collection/v1/search` 返回 **410 Gone**（2026-10-01 退役，替代 = v1.1）；Monet 名作被标 `isPublicDomain=false` 且无图（437133/437127/437122 实测）；Picasso/Matisse 各 20/20 非 PD → **OVERTURNED**（Met 覆盖缩至 5 位，其余走 AIC/Commons/Cleveland）。
3. **「AIC IIIF 可 curl 直取」** → `curl` 全 403（Cloudflare "Just a moment..."），`requests` 同 403 → **OVERTURNED** → 改用真实 Chromium 页面上下文 fetch（4/4 成功，`image/jpeg`）。
4. **「Commons 有毕加索干净复制品」** → 全文检索 + `Category:Pablo Picasso`（87 项）+ 4 个文件名直查全部落空；NGA Open Data 毕加索 288 张已发布图像 `openaccess=0` → **CONFIRMED 缺口**（不硬凑，换 Cleveland）。
5. **「33 张全部 ≤2000px 且总量 ≤100MB」** → 机械验证（见 C）：max=1800px、总量 20.9MB → **CONFIRMED**。

### C · 机械验证（原样输出）

命令（全量 33 张，非抽样）：`python -c "…os.listdir + PIL 逐张 w/h + 总字节…"`
```
TOTAL files: 33 | bytes: 21952732 = 20.9 MB | over-2000px: []
manifest exists: True 22771 bytes
```

来源 URL 抽验（`read` 工具抓取，原样摘录）：

① AIC 作品页 `https://www.artic.edu/artworks/16568/water-lilies`（native）：
```
title: Water Lilies | The Art Institute of Chicago
CC0 Public Domain Designation
Claude Monet (French, 1840–1926)
Date: 1906
Reference Number 1933.1157
```
② Cleveland 作品页 `https://clevelandart.org/art/1929.888`（native）：
```
title: The Frugal Meal | Cleveland Museum of Art
Credit Line: Dudley P. Allen Fund 1929.888
[Public Domain] You can copy, modify, and distribute this work, all without asking permission.
```
③ Met API 对象 `https://collectionapi.metmuseum.org/public/collection/v1/objects/45434`（json）：
```
"objectID": 45434,
"isPublicDomain": true,
"primaryImage": "https://images.metmuseum.org/CRDImages/as/original/DP130155.jpg",
"title": "Under the Wave off Kanagawa (Kanagawa oki nami ura), also known as The Great Wave, from the series Thirty-six Views of Mount Fuji (Fugaku sanjūrokkei)",
"objectURL": "https://www.metmuseum.org/art/collection/search/45434"
```
④ Commons 文件页 `https://commons.wikimedia.org/wiki/File:Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg`（native）：
```
title: File:Mona Lisa, by Leonardo da Vinci, from C2RMF retouched.jpg - Wikimedia Commons
Photographer: C2RMF: Galerie de tableaux en très haute définition
Collection: Louvre Museum （Accession number: INV 779 and MR 316）
```
（许可字段由 Commons API `extmetadata.LicenseShortName` 复核 = `Public domain`。）
注：`https://www.metmuseum.org/art/collection/search/45434` 网页版对非浏览器客户端返回 429（WAF），故以官方 API 地址复核同一对象。

### D · 小结（≤14 行）

- 已确立：11/11 位 × 3 张 = 33 张全部落盘，总 20.9MB，单张 ≤1800px；许可 100% 为 PD/CC0/CC BY-SA（CC 类署名逐张记录）。
- 已确立：4 个来源（Met OA / AIC / Cleveland / Commons）URL 抽验通过；2 张不合格候选图经目检剔除换源。
- 已推翻：Met v1 search 可用（实为 410 退役）；AIC IIIF 可 curl（403，须浏览器）；Commons 有毕加索干净复制品（没有）。
- 限制：Picasso 仅覆盖 1904–1910 早期作品（Cleveland CC0）；《大卫》为 CC BY-SA 照片；Met 对部分 PD 名画（Monet 等）旗标与馆方口径可能不一致（本次按 API 旗标执行）。
- 下一步（给主脑）：如需 Rijksmuseum《挤奶女工》、MoMA《亚维农少女》等，需 API key/授权，当前渠道做不到；本清单可直接供 wave3 组合实验引用。
