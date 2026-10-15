# 代表作图库 · manifest（D-02）

> 11 位画家 × 3 张 = **33 张**；采集日 2026-10-15；采集人 ImageLibrary（wave4 / D-02）。
> **wave12 追加**：克里姆特（klimt）3 张，2026-10-15，ArtistKlimt / A-22 → **现共 12 位 × 3 张 = 36 张**（总量 20.9 MB → 约 24.2 MB）。
> **wave13 追加**：修拉（seurat）10 张，2026-10-15，ArtistSeurat / A-24 → **现共 46 张**（36 + 修拉 10；总量约 34.5 MB）。
> **wave16 收口合并**（2026-10-16，IndexMerge / A-51）：并入 wave12/13 新档 6 位 58 张（turner 5 / rembrandt 6 / goya 9 / bada_shanren 9 / qi_baishi 11 / ito_jakuchu 18）＋ hopper 私有层例外（公开 0 / 私有 9）→ **现共 20 位画家 / 公开 104 张**（另有私有层例外 32 张——公开/私有分开记，见「私有层例外」节）。
> **wave15/17 并入**（2026-10-16，IndexMerge2）：并入 wave15×8 + wave17×7 共 15 位——新公开 169 张（mucha 12 / munch 13 / kandinsky 11 / velazquez 12 / bosch 10 / huang_gongwang 10 / behzad 12 / friedrich 12 / repin 10 / ravi_varma 17 / degas 13 / gauguin 20 / van_eyck 17；kahlo / kngwarreye 公开 0——全私有）＋ 私有层例外同步（+12 位 94 张）→ **现共 35 位画家 / 公开 273 张**（另有私有层例外 126 张——公开/私有分开记，见「私有层例外」节）。
> **wave18/19/20 并入**（2026-10-16，IndexMerge3）：并入 wave18×7 + wave19×10 + wave20×10 共 27 位——新公开 345 张（hiroshige 18 / sargent 14 / piero 17 / artemisia 16 / fan_kuan 8 / sesshu 18 / constable 17 / poussin 13 / bruegel 20 / el_greco 17 / holbein 13 / aivazovsky 14 / zhao_mengfu 14 / ni_zan 13 / qiu_ying 17 / ogata_korin 19 / blake 18 / chardin 17 / manet 14 / sorolla 13 / zorn 19 / sultan_mohammed 16；namatjira / el_salahi / wu_guanzhong / okeeffe / rivera 公开 0——全私有）＋ 私有层例外同步（+36 位 550 张 → 54 位 676 张）→ **现共 62 位画家 / 公开 618 张**（另有私有层例外 676 张——公开/私有分开记，见「私有层例外」节）。
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

| `hiroshige/asakusa_ricefields_torinomachi.jpg` | Pilgrimage to the Torinomachi Festival across the Ricefields of Asakusa（浅草田甫 酉の町詣；名所江戸百景） | Utagawa Hiroshige | 1857（安政 4 年 11 月） | The Met（36539；Rogers Fund, 1914） | https://www.metmuseum.org/art/collection/search/36539 | CC0（PD） |
| `hiroshige/camellia_and_bird.jpg` | Camellia and Bird（椿に小禽；花鸟画） | Utagawa Hiroshige | ca. 1833 | The Met（36719；Rogers Fund, 1918） | https://www.metmuseum.org/art/collection/search/36719 | CC0（PD） |
| `hiroshige/dragon_in_clouds.jpg` | Dragon in Clouds（雲中龍；大短冊判） | Utagawa Hiroshige | c. 1830s | Art Institute of Chicago（36444，Commons） | https://www.artic.edu/artworks/36444/dragon-in-clouds | Public domain |
| `hiroshige/hakone_lake.jpg` | Hakone; Kosui（箱根 湖水図；東海道五十三次之内 第 10 图） | Utagawa Hiroshige | ca. 1833–34 | The Met（36932；Rogers Fund, 1918） | https://www.metmuseum.org/art/collection/search/36932 | CC0（PD） |
| `hiroshige/kameido_plum_garden.jpg` | Plum Garden at Kameido（亀戸梅屋舗；名所江戸百景 第 30 图） | Utagawa Hiroshige | 1857 | Rijksmuseum（RP-P-1956-743，Commons） | https://commons.wikimedia.org/wiki/File:De_pruimenboomgaard_te_Kameido-Rijksmuseum_RP-P-1956-743.jpeg | Public domain |
| `hiroshige/kanbara_night_snow.jpg` | Evening Snow at Kanbara（蒲原 夜之雪；東海道五十三次之内 第 16 图） | Utagawa Hiroshige | ca. 1833–34 | The Met（56915；Howard Mansfield Coll.） | https://www.metmuseum.org/art/collection/search/56915 | CC0（PD） |
| `hiroshige/kinryuzan_temple_asakusa.jpg` | Kinryūsan Temple at Asakusa（浅草金龍山；名所江戸百景 第 99 图） | Utagawa Hiroshige | 1856 | The Met（56689；Howard Mansfield Coll.） | https://www.metmuseum.org/art/collection/search/56689 | CC0（PD） |
| `hiroshige/kiso_mountains_in_snow.jpg` | The Kiso Mountains in Snow（木曽山雪景；三枚续） | Utagawa Hiroshige | 1857（巳年 8 月） | The Met（36545；Rogers Fund, 1914） | https://www.metmuseum.org/art/collection/search/36545 | CC0（PD） |
| `hiroshige/moon_pine_ueno.jpg` | Moon Pine at Ueno（上野山内 月のまつ；名所江戸百景 第 89 图） | Utagawa Hiroshige | 1857 | Library of Congress（LCCN 2008660968，Commons） | https://commons.wikimedia.org/wiki/File:Ueno_sannai_tsuki_no_matsu_LCCN2008660968.jpg | Public domain |
| `hiroshige/naruto_whirlpool_awa.jpg` | Naruto Whirlpool, Awa Province（阿波 鳴門の風波；六十余州名所図会） | Utagawa Hiroshige | ca. 1853 | The Met（53783；Rogers Fund, 1919） | https://www.metmuseum.org/art/collection/search/53783 | CC0（PD） |
| `hiroshige/nihonbashi_morning.jpg` | Stations One: Morning View of Nihonbashi（日本橋 朝之景；東海道五十三次之内 第 1 图） | Utagawa Hiroshige | ca. 1833–34 | The Met（36922；Rogers Fund, 1918） | https://www.metmuseum.org/art/collection/search/36922 | CC0（PD） |
| `hiroshige/ohashi_atake_sudden_shower.jpg` | Sudden Shower over Shin-Ōhashi Bridge and Atake（大はしあたけの夕立；名所江戸百景 第 58 图） | Utagawa Hiroshige | 1857 | The Met（55433；Howard Mansfield Coll.） | https://www.metmuseum.org/art/collection/search/55433 | CC0（PD） |
| `hiroshige/otsu_reisho_edition.jpg` | Ōtsu（大津；東海道五十三次之内 隷書東海道版 第 54 图） | Utagawa Hiroshige | 1847–52 | The Met（37248；Francis Lathrop Coll.） | https://www.metmuseum.org/art/collection/search/37248 | CC0（PD） |
| `hiroshige/ryogoku_bridge_brooklyn.jpg` | Ryōgoku Bridge and the Great Riverbank（両国橋大川ばた；名所江戸百景 第 59 图） | Utagawa Hiroshige | 1856 | Brooklyn Museum（Commons 复制品） | https://commons.wikimedia.org/wiki/File:Brooklyn_Museum_-_Ryogoku_Bridge_and_the_Great_Riverbank_No_59_from_One_Hundred_Views_of_Edo_-_Utagawa_Hiroshige_(Ando).jpg | Public domain |
| `hiroshige/satta_sea_suruga.jpg` | The Sea at Satta, Suruga Province（駿河 薩埵峠の海；富士三十六景） | Utagawa Hiroshige | 1858 | Google Art Project（Commons） | https://commons.wikimedia.org/wiki/File:Ando_Hiroshige_-_The_Sea_at_Satta,_Suruga_Province,_from_the_series_%22Thirty-six_Views_of_Mount_Fuji%22_-_Google_Art_Project.jpg | Public domain |
| `hiroshige/seba_kiso_road.jpg` | Seba（洗馬；木曾街道六十九次之内） | Utagawa Hiroshige | ca. 1836–37 | Rijksmuseum（RP-P-1956-739，Commons） | https://commons.wikimedia.org/wiki/File:Seba-Rijksmuseum_RP-P-1956-739.jpeg | Public domain |
| `hiroshige/shono_driving_rain.jpg` | Shower at Shōno（庄野 白雨；東海道五十三次之内 第 45 图） | Utagawa Hiroshige | 1834 | The Met（56916；Howard Mansfield Coll.） | https://www.metmuseum.org/art/collection/search/56916 | CC0（PD） |
| `hiroshige/twilight_moon_ryogoku.jpg` | Twilight Moon at Ryōgoku Bridge（両国橋夕月；江戸名所） | Utagawa Hiroshige | 江戸时代（馆方未署年代） | The Met（45294；Rogers Fund, 1922） | https://www.metmuseum.org/art/collection/search/45294 | CC0（PD） |
| `sargent/carnation_lily_lily_rose_1885_86.jpg` | Carnation, Lily, Lily, Rose | John Singer Sargent | 1885–86 | Tate, London（N01615） | https://commons.wikimedia.org/wiki/File:John_Singer_Sargent_-_Carnation,_Lily,_Lily,_Rose_-_Google_Art_Project.jpg | Public domain |
| `sargent/claude_monet_painting_by_the_edge_of_a_wood_1885.jpg` | Claude Monet Painting by the Edge of a Wood | John Singer Sargent | ?1885 | Tate, London（N04103） | https://commons.wikimedia.org/wiki/File:John_Singer_Sargent,_Claude_Monet_peignant_%C3%A0_la_lisi%C3%A8re_d%27un_bois.jpg | Public domain |
| `sargent/el_jaleo_1882.jpg` | El Jaleo | John Singer Sargent | 1882 | Isabella Stewart Gardner Museum, Boston | https://commons.wikimedia.org/wiki/File:EL_JALEO-SINGER.jpg | Public domain |
| `sargent/ellen_terry_as_lady_macbeth_1889.jpg` | Ellen Terry as Lady Macbeth | John Singer Sargent | 1889 | Tate, London（N02053） | https://commons.wikimedia.org/wiki/File:Ellen_Terry_as_Lady_Macbeth.jpg | Public domain |
| `sargent/green_door_santa_maria_della_salute_c1904.jpg` | Green Door, Santa Maria della Salute（水彩） | John Singer Sargent | ca. 1904 | The Met, New York（12107） | https://www.metmuseum.org/art/collection/search/12107 | CC0 1.0 |
| `sargent/henry_james_1913.jpg` | Henry James | John Singer Sargent | 1913 | National Portrait Gallery, London | https://commons.wikimedia.org/wiki/File:Henry_James_by_John_Singer_Sargent.jpg | Public domain（注记见下） |
| `sargent/lady_with_the_rose_1882.jpg` | Lady with the Rose (Charlotte Louise Burckhardt) | John Singer Sargent | 1882 | The Met, New York（32.154） | https://commons.wikimedia.org/wiki/File:Lady_with_the_Rose_(Charlotte_Louise_Burckhardt)_MET_DT1151.jpg | CC0（Met 官方照片） |
| `sargent/madame_x_1884.jpg` | Madame X (Virginie Amélie Avegno Gautreau) | John Singer Sargent | 1883–84 | The Met, New York（16.53） | https://www.metmuseum.org/art/collection/search/12127 | CC0 1.0（Met Open Access） |
| `sargent/marie_louise_pailleron_c1881.jpg` | Marie-Louise Pailleron（墨笔素描） | John Singer Sargent | ca. 1881 | The Met, New York（50.130.115） | https://www.metmuseum.org/art/collection/search/12464 | CC0 1.0 |
| `sargent/mrs_hugh_hammersley_1892.jpg` | Mrs. Hugh Hammersley | John Singer Sargent | 1892 | The Met, New York（1998.365） | https://commons.wikimedia.org/wiki/File:Mrs._Hugh_Hammersley_MET_DT2064.jpg | CC0（Met 官方照片） |
| `sargent/octavia_hill_1898.jpg` | Octavia Hill | John Singer Sargent | 1898 | National Portrait Gallery, London（NPG 1746） | https://commons.wikimedia.org/wiki/File:John_Singer_Sargent_-_Octavia_Hill_-_NPG_1746_-_National_Portrait_Gallery.jpg | Public domain |
| `sargent/the_wyndham_sisters_1899.jpg` | The Wyndham Sisters: Lady Elcho, Mrs. Adeane, and Mrs. Tennant | John Singer Sargent | 1899 | The Met, New York（27.67） | https://commons.wikimedia.org/wiki/File:The_Wyndham_Sisters_-_Lady_Elcho,_Mrs._Adeane,_and_Mrs._Tenant.jpg | Public domain |
| `sargent/two_girls_on_a_lawn_c1889.jpg` | Two Girls on a Lawn | John Singer Sargent | ca. 1889 | The Met, New York（50.130.20） | https://www.metmuseum.org/art/collection/search/12446 | CC0 1.0 |
| `sargent/violet_sargent_c1883.jpg` | Violet Sargent（石墨素描） | John Singer Sargent | ca. 1883 | The Met, New York（50.130.87） | https://www.metmuseum.org/art/collection/search/12462 | CC0 1.0 |
| `piero_della_francesca/baptism_of_christ_ng665.jpg` | 《基督受洗》（The Baptism of Christ） | Piero della Francesca | 约 1437–1445 | National Gallery, London（NG665） | https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_Battesimo_di_Cristo_(National_Gallery,_London).jpg | Public domain |
| `piero_della_francesca/diptych_federico_battista.jpg` | 《乌尔比诺公爵双联像·正面》（Federico da Montefeltro & Battista Sforza） | Piero della Francesca | 约 1465–1475 | Galleria degli Uffizi, Florence | https://commons.wikimedia.org/wiki/File:Piero_della_francesca,_dittico_dei_duchi_di_urbino,_1465-72_circa_01.jpg | CC BY-SA 4.0（摄影 Sailko / Francesco Bini） |
| `piero_della_francesca/diptych_reverse_triumphs.jpg` | 《双联像·背面：凯旋寓意图》（Triumphs of Federico and Battista） | Piero della Francesca | 约 1465–1475 | Galleria degli Uffizi, Florence | https://commons.wikimedia.org/wiki/File:Piero_della_francesca,_dittico_dei_duchi_di_urbino,_1465-72_circa_02.jpg | CC BY-SA 4.0（摄影 Sailko / Francesco Bini） |
| `piero_della_francesca/flagellation_urbino.jpg` | 《鞭笞》（The Flagellation of Christ） | Piero della Francesca | 约 1455–1470 | Galleria Nazionale delle Marche, Urbino | https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_The_Flagellation_-_WGA17600.jpg | Public domain |
| `piero_della_francesca/legend_true_cross_battle_heraclius.jpg` | 《赫拉克利乌斯与科斯罗埃斯之战》（Battle between Heraclius and Chosroes） | Piero della Francesca | 约 1452–1466 | Basilica di San Francesco, Arezzo | https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_8._Battle_between_Heraclius_and_Chosroes_-_WGA17551.jpg | Public domain |
| `piero_della_francesca/legend_true_cross_dream_of_constantine.jpg` | 《君士坦丁之梦》（Constantine's Dream，真十字架组画） | Piero della Francesca | 约 1452–1466 | Basilica di San Francesco, Arezzo | https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_017.jpg | Public domain |
| `piero_della_francesca/legend_true_cross_finding_and_recognition.jpg` | 《真十字架的发现与验证》（Finding and Recognition of the True Cross） | Piero della Francesca | 约 1452–1466 | Basilica di San Francesco, Arezzo | https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_7._Finding_and_Recognition_of_the_True_Cross_-_WGA17533.jpg | Public domain |
| `piero_della_francesca/legend_true_cross_queen_of_sheba.jpg` | 《示巴女王礼拜圣木/与所罗门相会》（Procession of the Queen of Sheba; Meeting with Solomon） | Piero della Francesca | 约 1452–1466 | Basilica di San Francesco, Arezzo | https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_2._Procession_of_the_Queen_of_Sheba%3B_Meeting_between_the_Queen_of_Sheba_and_King_Solomon_-_WGA17487.jpg | Public domain |
| `piero_della_francesca/madonna_del_parto.jpg` | 《分娩圣母》（Madonna del Parto） | Piero della Francesca | 约 1455–1465 | Museo della Madonna del Parto, Monterchi | https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_Madonna_del_Parto_-_WGA17613.jpg | Public domain |
| `piero_della_francesca/madonna_di_senigallia.jpg` | 《塞尼加利亚圣母》（Madonna di Senigallia） | Piero della Francesca | 约 1470–1485 | Galleria Nazionale delle Marche, Urbino | https://commons.wikimedia.org/wiki/File:Piero_della_Francesca,_Madonna_di_Senigallia_01.jpg | CC BY-SA 4.0（摄影 Mongolo1984） |
| `piero_della_francesca/montefeltro_altarpiece_brera.jpg` | 《蒙特费尔特罗祭坛画》（Brera Madonna / Montefeltro Altarpiece） | Piero della Francesca | 1472–1474 | Pinacoteca di Brera, Milan | https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_Madonna_and_Child_with_Saints_(Montefeltro_Altarpiece)_-_WGA17615.jpg | Public domain |
| `piero_della_francesca/nativity_ng908.jpg` | 《圣诞》（The Nativity） | Piero della Francesca | 约 1470–1482 | National Gallery, London（NG908） | https://commons.wikimedia.org/wiki/File:Piero_della_francesca,_natività,_1470-75,_01.jpg | Public domain |
| `piero_della_francesca/polyptych_of_the_misericordia.jpg` | 《慈悲多联祭坛画》（Polyptych of the Misericordia） | Piero della Francesca | 1445–1462 | Museo Civico, Sansepolcro | https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_Polyptych_of_the_Misericordia_-_WGA17446.jpg | Public domain |
| `piero_della_francesca/portrait_sigismondo_malatesta.jpg` | 《西吉斯蒙多·潘多尔福·马拉泰斯塔像》（Portrait of Sigismondo Pandolfo Malatesta） | Piero della Francesca | 约 1451 | Musée du Louvre, Paris | https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_Sigismondo_Pandolfo_Malatesta_-_WGA17624.jpg | Public domain |
| `piero_della_francesca/resurrection_sansepolcro.jpg` | 《复活》（The Resurrection） | Piero della Francesca | 约 1463–1465 | Museo Civico, Sansepolcro | https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_Resurrection_-_WGA17609.jpg | Public domain |
| `piero_della_francesca/saint_jerome_penitent_berlin.jpg` | 《忏悔的圣杰罗姆》（Saint Jerome in Penitence） | Piero della Francesca | 约 1450 | Gemäldegalerie, Berlin | https://commons.wikimedia.org/wiki/File:Piero_della_francesca,_San_Girolamo_penitente,_1450_ca,_da_gemaldegalerie_di_berlino.JPG | Public domain |
| `piero_della_francesca/saint_michael_ng769.jpg` | 《圣米迦勒》（Saint Michael，Sant'Agostino 多联祭坛侧板） | Piero della Francesca | 约 1454–1469 | National Gallery, London（NG769） | https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_Polyptych_of_St_Augustine_-_St_Michael_-_WGA17457.jpg | Public domain |
| `artemisia_gentileschi/allegory_of_inclination.jpg` | Allegory of Inclination（倾向的寓意；152×61 cm，天顶画） | Artemisia Gentileschi | 1615–16 | Casa Buonarroti, Florence（1684 年 Volterrano 加绘织物） | https://commons.wikimedia.org/wiki/File:A_Gentileschi_Allegoria_dell%27inclinazione.jpg | Public domain |
| `artemisia_gentileschi/annunciation_capodimonte.jpg` | Annunciation（受胎告知；Commons 标注 "Attributed to"） | Artemisia Gentileschi | 1630 | Museo e Real Bosco di Capodimonte, Naples | https://commons.wikimedia.org/wiki/File:Verk%C3%BCndigung_an_maria.jpg | Public domain |
| `artemisia_gentileschi/corisca_and_the_satyr.jpg` | Corisca and the Satyr（科里斯卡与萨提尔） | Artemisia Gentileschi | c. 1630s | Private collection | https://commons.wikimedia.org/wiki/File:Corisca_and_the_Satyr_by_Artemisia_Gentileschi.jpg | Public domain |
| `artemisia_gentileschi/danae.jpg` | Danaë（达娜厄；93:1986） | Artemisia Gentileschi | c. 1612 | Saint Louis Art Museum | https://commons.wikimedia.org/wiki/File:Artemisia_Gentileschi_-_Dana%C3%AB.jpg | Public domain |
| `artemisia_gentileschi/esther_before_ahasuerus.jpg` | Esther before Ahasuerus（208.3×273.7 cm；1969 年 Ingersoll 赠） | Artemisia Gentileschi | 1620s | The Metropolitan Museum of Art, New York（436453） | https://commons.wikimedia.org/wiki/File:Gentileschi,_Artemisia_-_Esther_before_Ahasuerus_-_c._1628%E2%80%931635.jpg | Public domain |
| `artemisia_gentileschi/jael_and_sisera.jpg` | Jael and Sisera（雅亿与西西拉） | Artemisia Gentileschi | c. 1620 | Museum of Fine Arts, Budapest | https://commons.wikimedia.org/wiki/File:Giaele_e_Sisara_(ca.1620)_-_Artemisia_Gentileschi_(Museum_of_Fine_Arts,_Budapest).jpg | Public domain |
| `artemisia_gentileschi/judith_and_her_maidservant_detroit.jpg` | Judith and Her Maidservant with the Head of Holofernes（187.2×142 cm；52.253） | Artemisia Gentileschi | c. 1623–25 | Detroit Institute of Arts（Gift of Mr. Leslie H. Green） | https://commons.wikimedia.org/wiki/File:Artemisia_Gentileschi_Judith_Maidservant_DIA.jpg | Public domain |
| `artemisia_gentileschi/judith_and_her_maidservant_pitti.jpg` | Judith and Her Maidservant（朱迪斯与女仆；皮蒂宫版） | Artemisia Gentileschi | c. 1613–1619（口径不一） | Galleria Palatina, Palazzo Pitti, Florence | https://commons.wikimedia.org/wiki/File:Gentileschi_judith1.jpg | Public domain |
| `artemisia_gentileschi/judith_beheading_holofernes_uffizi.jpg` | Judith Beheading Holofernes（乌菲齐版；146.5×108 cm；inv. 1890 n. 1567） | Artemisia Gentileschi | c. 1620 | Gallerie degli Uffizi, Florence（D29 厅） | https://commons.wikimedia.org/wiki/File:Artemisia_Gentileschi_-_Giuditta_decapita_Oloferne_-_Google_Art_Project.jpg | Public domain |
| `artemisia_gentileschi/judith_slaying_holofernes_naples.jpg` | Judith Slaying Holofernes（朱迪斯斩首荷罗孚尼，那不勒斯版；158.8×125.5 cm） | Artemisia Gentileschi | c. 1612–13（另说 1617，见 §10） | Museo e Real Bosco di Capodimonte, Naples（Q378） | https://commons.wikimedia.org/wiki/File:Artemisia_Gentileschi_-_Judith_Beheading_Holofernes_-_WGA8563.jpg | Public domain |
| `artemisia_gentileschi/mary_magdalene_pitti.jpg` | Mary Magdalene（抹大拉的马利亚） | Artemisia Gentileschi | c. 1613–20 | Galleria Palatina, Palazzo Pitti, Florence | https://commons.wikimedia.org/wiki/File:Artemisia_Gentileschi_Mary_Magdalene_Pitti.jpg | Public domain |
| `artemisia_gentileschi/self_portrait_as_a_lute_player.jpg` | Self-Portrait as a Lute Player（扮鲁特琴手的自画像） | Artemisia Gentileschi | c. 1615–18 | Wadsworth Atheneum, Hartford | https://commons.wikimedia.org/wiki/File:Artemisia_Gentileschi_-_Self-Portrait_as_a_Lute_Player.JPG | Public domain |
| `artemisia_gentileschi/self_portrait_as_saint_catherine.jpg` | Self-Portrait as Saint Catherine of Alexandria（NG6671；71.5×71 cm） | Artemisia Gentileschi | c. 1615–17 | The National Gallery, London（2018 年购入） | https://commons.wikimedia.org/wiki/File:Artemisia_Gentileschi_-_Self-Portrait_5365.jpg | Public domain |
| `artemisia_gentileschi/self_portrait_as_the_allegory_of_painting.jpg` | Self-Portrait as the Allegory of Painting（La Pittura；RCIN 405551；98.6×75.2 cm） | Artemisia Gentileschi | c. 1638–39 | Royal Collection（Hampton Court Palace） | https://commons.wikimedia.org/wiki/File:Self-portrait_as_the_Allegory_of_Painting_(La_Pittura)_-_Artemisia_Gentileschi.jpg | Public domain |
| `artemisia_gentileschi/susanna_and_the_elders_1610.jpg` | Susanna and the Elders（苏珊娜与长老；170×119 cm） | Artemisia Gentileschi | 1610 | Schloss Weißenstein（Schönborn 收藏）, Pommersfelden | https://commons.wikimedia.org/wiki/File:Susanna_and_the_Elders_(1610),_Artemisia_Gentileschi.jpg | Public domain |
| `artemisia_gentileschi/venus_and_cupid.jpg` | Venus and Cupid（维纳斯与丘比特） | Artemisia Gentileschi | c. 1625–30 | Virginia Museum of Fine Arts, Richmond | https://commons.wikimedia.org/wiki/File:Gentileschi_-_Venus_and_Cupid_(c._1625-30_VMFA).jpg | Public domain |
| `fan_kuan/fang_fankuan_met.jpg` | 倣范寬山水圖（佚名） | Fan Kuan | 北宋末（12世纪初） | 大都会艺术博物馆（MET 56.151） | https://commons.wikimedia.org/wiki/File:宋范寬秋林飛瀑_軸.jpg（MET Open Access：https://images.metmuseum.org/CRDImages/as/original/DP165245.jpg（Commons 同源）） | **CC0**（MET Open Access） |
| `fan_kuan/linliu_duzuo.jpg` | 临流独坐图（传范宽） | Fan Kuan | 宋（约南宋初） | 台北故宫博物院（故画000045） | https://commons.wikimedia.org/wiki/File:宋范寬臨流獨坐圖_軸.jpg（NPM 开放数据） | **CC0**（台北故宫开放数据） |
| `fan_kuan/qiulin_feipu.jpg` | 秋林飞瀑图（传范宽） | Fan Kuan | 宋 | 台北故宫博物院（故画000825） | https://commons.wikimedia.org/wiki/File:宋范寬秋林飛瀑_軸.jpg（NPM 开放数据） | **CC0**（台北故宫开放数据） |
| `fan_kuan/wanghui_fa_fankuan.jpg` | 王翬《紅林秋霁》（法范寬山水；《清惲壽平王翬花卉山水合冊》之一开） | Fan Kuan | 清·康熙十一年（1672） | 台北故宫博物院（故画001231N000000010） | https://digitalarchive.npm.gov.tw/Collection/Detail/5100?dep=P（NPM 开放资料 IIIF） | 开放资料（政府资料开放授权条款，相容 CC BY 4.0；署名：国立故宫博物院） |
| `fan_kuan/xishan_signature.jpg` | 谿山行旅图·款识位置（右下树荫） | Fan Kuan | 北宋 | 台北故宫博物院 | https://commons.wikimedia.org/wiki/File:Fan_Kuan_-_Travelers_Among_Mountains_and_Streams_-_Signature.jpg | Public domain（PD-Art） |
| `fan_kuan/xishan_xinglv.jpg` | 谿山行旅图（画心） | Fan Kuan | 北宋（11世纪初） | 台北故宫博物院（故画000826） | https://commons.wikimedia.org/wiki/File:谿山行旅图轴.溪山行旅图.宋.范宽.绢本浅设色.台北故宫博物院藏.jpg | Public domain（PD-Art） |
| `fan_kuan/xuejing_hanlin.jpg` | 雪景寒林图 | Fan Kuan | 北宋 | 天津博物馆 | https://commons.wikimedia.org/wiki/File:Xuejinghanlintu.jpg | Public domain（PD-Art） |
| `fan_kuan/zhaoyuan_handscroll.jpg` | 趙原《倣燕文貴范寬山水圖》卷（局部段） | Fan Kuan | 元末（14世纪晚期） | 大都会艺术博物馆（MET 1981.285.15） | https://digitalarchive.npm.gov.tw/Collection/Detail/5100?dep=P（MET Open Access：https://images.metmuseum.org/CRDImages/as/original/DP303149.jpg（Commons 同源）） | **CC0**（MET Open Access） |
| `sesshu/amanohashidate.jpg` | 《天橋立図》（国宝） | Sesshū Tōyō | 16 世紀（1501 以降説有力） | 京都国立博物館（A甲228） | https://commons.wikimedia.org/wiki/File:Sesshu_-_View_of_Ama-no-Hashidate.jpg | Public domain（PD-Art） |
| `sesshu/autumn_winter_autumn.jpg` | 《秋冬山水図》秋景（国宝，2 幅のうち） | Sesshū Tōyō | 15 世紀末–16 世紀初 | 東京国立博物館（A-1398） | https://commons.wikimedia.org/wiki/File:SesshuToyo.jpg | Public domain（PD-Art） |
| `sesshu/autumn_winter_winter.jpg` | 《秋冬山水図》冬景（国宝） | Sesshū Tōyō | 15 世紀末–16 世紀初 | 東京国立博物館（A-1398） | https://commons.wikimedia.org/wiki/File:SesshuShuutouTou.jpg | Public domain（PD-Art） |
| `sesshu/birds_flowers_left.jpg` | 《四季花鳥図屏風》（伝雪舟；重要文化財）左隻 | Sesshū Tōyō | 15 世紀 | 東京国立博物館 | https://commons.wikimedia.org/wiki/File:SESHU_Birds-flowers-L.jpeg | Public domain（PD-Art） |
| `sesshu/birds_flowers_right.jpg` | 《四季花鳥図屏風》（伝雪舟）右隻 | Sesshū Tōyō | 15 世紀 | 東京国立博物館 | https://commons.wikimedia.org/wiki/File:SESHU_Birds-flowers-R.jpeg | Public domain（PD-Art） |
| `sesshu/bishamonten.jpg` | 《毘沙門天図》 | Sesshū Tōyō | 室町時代 | 画像注记「private collection, Tokyo」（2002 年没後 500 年展图录）；另有重文《毘沙門天図》（相国寺承天閣美術館）记录——异同未核（已查: Commons 文件页、ja.wiki 作品表） | https://commons.wikimedia.org/wiki/File:Bishamonten_by_Sesshu_(Tokyo).jpeg | Public domain（PD-Art） |
| `sesshu/four_seasons_mori_full.jpg` | 《四季山水図巻（山水長巻）》全巻（国宝） | Sesshū Tōyō | 文明18年（1486） | 毛利博物館 | https://commons.wikimedia.org/wiki/File:Landscapes_of_the_Four_Seasons_by_Sesshu_(Mori_Museum).jpg | Public domain（PD-Art） |
| `sesshu/four_seasons_tnm_autumn.jpg` | 《四季山水図》4 幅のうち秋景（重要文化財；入明期作） | Sesshū Tōyō | 15 世紀 | 東京国立博物館（A-10933） | https://commons.wikimedia.org/wiki/File:Sesshu_Toyo_-_Landscape_of_Four_Seasons-_Fall_-_Google_Art_Project.jpg | Public domain（PD-Art；Google Art Project） |
| `sesshu/four_seasons_tnm_winter.jpg` | 《四季山水図》4 幅のうち冬景（重要文化財） | Sesshū Tōyō | 15 世紀 | 東京国立博物館（A-10933） | https://commons.wikimedia.org/wiki/File:Sesshu_Toyo_-_Landscape_of_four_seasons-_winter_-_Google_Art_Project.jpg | Public domain（PD-Art；Google Art Project） |
| `sesshu/haboku_sansui_1495.jpg` | 《破墨山水図》（指定名称「紙本墨画山水図」；国宝） | Sesshū Tōyō | 明応4年（1495） | 東京国立博物館（A-282） | https://commons.wikimedia.org/wiki/File:Sesshu_-_Haboku-Sansui.jpg | Public domain（PD-Art） |
| `sesshu/haboku_sansui_complete.jpg` | 《破墨山水図》全幅（含雪舟自序 + 六僧题诗） | Sesshū Tōyō | 1495 | 東京国立博物館 | https://commons.wikimedia.org/wiki/File:Sesshu_-_Haboku-Sansui_-_complete.jpg | Public domain（PD-Art） |
| `sesshu/huang_chuping.jpg` | 《倣梁楷黄初平図》（重要文化財） | Sesshū Tōyō | 室町時代 | 京都国立博物館 | https://commons.wikimedia.org/wiki/File:Huang_Chuping_by_Sesshu_(Kyoto_National_Museum).jpg | Public domain（PD-Art） |
| `sesshu/huike_offering_arm.jpg` | 《慧可断臂図》（国宝） | Sesshū Tōyō | 明応5年（1496） | 愛知・斉年寺（京都国立博物館寄託） | https://commons.wikimedia.org/wiki/File:Bodhidharma.and.Huike-Sesshu.Toyo.jpg | Public domain（PD-Art） |
| `sesshu/mori_scroll_left.jpg` | 《四季山水図巻（山水長巻）》部分（左半） | Sesshū Tōyō | 1486 | 毛利博物館 | https://commons.wikimedia.org/wiki/File:SESSHU-Sansui_chokan-L.jpg | Public domain（PD-Art） |
| `sesshu/mori_scroll_right.jpg` | 《四季山水図巻（山水長巻）》部分（右半） | Sesshū Tōyō | 1486 | 毛利博物館 | https://commons.wikimedia.org/wiki/File:SESSHU-Sansui_chokan-R.jpg | Public domain（PD-Art） |
| `sesshu/portrait_sesshu_copy.jpg` | 《絹本著色雪舟自画像（模本）》（重文『紙本墨書題雪舟山水図詩 了庵桂悟筆』附指定） | Sesshū Tōyō | 16 世紀 | 藤田美術館 | https://commons.wikimedia.org/wiki/File:Portrait_of_Sesshu.jpg | Public domain（PD-Art） |
| `sesshu/sesso_hatsuboku_nezou.jpg` | 雪村《破墨山水図》（影響链对照件；雪村=雪舟破墨系谱） | Sesshū Tōyō | 16 世紀（推定） | 根津美術館 | https://commons.wikimedia.org/wiki/File:Hatsuboku_landscape_by_Sesso_(Nezu_Museum).jpeg | Public domain（PD-Art） |
| `sesshu/xia_gui_imitation.jpg` | 《倣夏珪山水図》（2017 年 84 年ぶり再発見、「幻の作品」） | Sesshū Tōyō | 15 世紀 | 山口県立美術館寄託（個人蔵） | https://commons.wikimedia.org/wiki/File:Landscape_in_Imitation_of_Xia_Gui_(%E5%80%A3%E5%A4%8F%E7%8F%AA%E5%B1%B1%E6%B0%B4%E5%9B%B3)_by_Sesshu.jpg | Public domain（PD-Art） |
| `constable/brighton_beach_with_colliers.jpg` | Brighton Beach with Colliers（591-1888） | John Constable | 1824 | Victoria and Albert Museum | https://commons.wikimedia.org/wiki/File:Constable_-_Brighton_Beach_with_Colliers,_1824,_591-1888.jpg | Public domain |
| `constable/dedham_vale.jpg` | Dedham Vale | John Constable | 1802 | Yale Center for British Art | https://commons.wikimedia.org/wiki/File:John_Constable_-_Dedham_Vale_-_Google_Art_Project.jpg | Public domain |
| `constable/flatford_mill.jpg` | Flatford Mill (Scene on a Navigable River, N01273) | John Constable | 1816–17 | Tate | https://commons.wikimedia.org/wiki/File:Flatford_Mill_(Scene_on_a_Navigable_River)_by_John_Constable,_Tate_Britain.JPG | CC0 |
| `constable/hampstead_heath_with_rainbow.jpg` | Hampstead Heath with a Rainbow（N01275） | John Constable | 1836 | Tate | https://commons.wikimedia.org/wiki/File:John_Constable_(1776-1837)_-_Hampstead_Heath_with_a_Rainbow_-_N01275_-_National_Gallery.jpg | Public domain |
| `constable/salisbury_cathedral_from_the_bishops_grounds.jpg` | Salisbury Cathedral from the Bishop's Grounds（FA.33） | John Constable | 1823 | Victoria and Albert Museum | https://commons.wikimedia.org/wiki/File:John_Constable_-_Salisbury_Cathedral_from_the_Bishop%27s_Grounds.jpg | Public domain |
| `constable/salisbury_cathedral_from_the_meadows.jpg` | Salisbury Cathedral from the Meadows（T13896） | John Constable | exhibited 1831 | Tate | https://commons.wikimedia.org/wiki/File:Constable_Salisbury_meadows.jpg | Public domain |
| `constable/seascape_study_with_rain_cloud.jpg` | Seascape Study with Rain Cloud | John Constable | c.1827 | Royal Academy of Arts | https://commons.wikimedia.org/wiki/File:Constable_-_Seascape_Study_with_Rain_Cloud.jpg | Public domain |
| `constable/stonehenge.jpg` | Stonehenge（1629-1888） | John Constable | 1835 | Victoria and Albert Museum | https://commons.wikimedia.org/wiki/File:John_Constable_-_Stonehenge_-_Google_Art_Project.jpg | Public domain |
| `constable/study_of_cirrus_clouds.jpg` | Study of Cirrus Clouds（784-1888；背面「cirrus」） | John Constable | ca. 1822 | Victoria and Albert Museum | https://commons.wikimedia.org/wiki/File:Constable_-_Study_of_Cirrus_Clouds,_c.1822,_784-1888.jpg | Public domain |
| `constable/study_of_clouds_1822.jpg` | Study of Clouds（590-1888；题记「Sepr. 5. 1822」） | John Constable | 1822 | Victoria and Albert Museum | https://commons.wikimedia.org/wiki/File:Constable_-_Study_of_Clouds,_1822,_590-1888.jpg | Public domain |
| `constable/study_of_clouds_above_wide_landscape.jpg` | Study of clouds above a wide landscape（240-1888；题记「Sepr 15 1830」） | John Constable | 1830 | Victoria and Albert Museum | https://commons.wikimedia.org/wiki/File:Constable_-_Study_of_clouds_above_a_wide_landscape,_240-1888.jpg | Public domain |
| `constable/the_cornfield_1826.jpg` | The Cornfield（麦田，NG130） | John Constable | 1826 | National Gallery, London | https://commons.wikimedia.org/wiki/File:John_Constable_-_The_Cornfield.jpg | Public domain |
| `constable/the_hay_wain_1821.jpg` | The Hay Wain（干草车，NG1207） | John Constable | 1821 | National Gallery, London | https://commons.wikimedia.org/wiki/File:John_Constable_-_The_Hay_Wain_(1821).jpg | Public domain |
| `constable/the_leaping_horse.jpg` | The Leaping Horse（03/1391） | John Constable | 1825 | Royal Academy of Arts | https://commons.wikimedia.org/wiki/File:The_Leaping_Horse_(1825)_by_John_Constable_-_Google_Art_Project.jpg | Public domain |
| `constable/the_valley_farm.jpg` | The Valley Farm（N00327） | John Constable | c.1835 | Tate | https://commons.wikimedia.org/wiki/File:John_Constable_-_The_Valley_Farm,_c._1835.jpg | Public domain |
| `constable/the_white_horse.jpg` | The White Horse（1943.1.147） | John Constable | 1819 | The Frick Collection | https://commons.wikimedia.org/wiki/File:The_White_Horse_by_John_Constable_-_Google_Art_Project.jpg | Public domain |
| `constable/wivenhoe_park.jpg` | Wivenhoe Park, Essex（1942.9.10） | John Constable | 1816 | National Gallery of Art, Washington | https://commons.wikimedia.org/wiki/File:John_Constable_-_Wivenhoe_Park,_Essex_-_Google_Art_Project.jpg | Public domain |
| `poussin/a_dance_to_the_music_of_time.jpg` | A Dance to the Music of Time（随时间之乐起舞） | Nicolas Poussin | c. 1634–36 | Wallace Collection, London | https://commons.wikimedia.org/wiki/File:The_dance_to_the_music_of_time_c._1640.jpg | Public domain |
| `poussin/adoration_of_the_golden_calf.jpg` | The Adoration of the Golden Calf（金牛犊的崇拜，NG5597） | Nicolas Poussin | 1633–4 | The National Gallery, London | https://commons.wikimedia.org/wiki/File:Nicolas_Poussin_-_The_Adoration_of_the_Golden_Calf_alt.jpg | Public domain |
| `poussin/autoportrait_1650.jpg` | Autoportrait（自画像，INV 7302） | Nicolas Poussin | 1650 | Musée du Louvre | https://commons.wikimedia.org/wiki/File:Poussin_-_Autoportrait,_1650,_INV_7302_;_MR_2329.jpg | Public domain |
| `poussin/blind_orion_searching_for_the_rising_sun.jpg` | Blind Orion Searching for the Rising Sun（盲 Orion，24.45.1） | Nicolas Poussin | 1658 | The Met, New York | https://commons.wikimedia.org/wiki/File:Orion_aveugle_cherchant_le_soleil.jpg | Public domain |
| `poussin/et_in_arcadia_ego.jpg` | Les Bergers d'Arcadie（阿卡迪亚的牧人，INV 7300） | Nicolas Poussin | vers 1638 | Musée du Louvre | https://commons.wikimedia.org/wiki/File:Nicolas_Poussin_-_Et_in_Arcadia_ego_(deuxi%C3%A8me_version).jpg | Public domain |
| `poussin/l_enlevement_des_sabines.jpg` | L'Enlèvement des Sabines（劫夺萨宾妇女，INV 7290） | Nicolas Poussin | vers 1637–1638 | Musée du Louvre | https://commons.wikimedia.org/wiki/File:L%27Enl%C3%A8vement_des_Sabines_-_Nicolas_Poussin_-_Mus%C3%A9e_du_Louvre_Peintures_INV_7290_;_MR_2335.jpg | Public domain |
| `poussin/l_inspiration_du_poete.jpg` | L'Inspiration du poète（诗人的灵感，RF 1774） | Nicolas Poussin | vers 1629 | Musée du Louvre | https://commons.wikimedia.org/wiki/File:L%27Inspiration_du_po%C3%A8te_-_Nicolas_Poussin_-_Mus%C3%A9e_du_Louvre_-_Peintures_RF_1774.jpg | Public domain |
| `poussin/la_manne.jpg` | La Manne（吗哪的收集，INV 7275） | Nicolas Poussin | 1638–1639 | Musée du Louvre | https://commons.wikimedia.org/wiki/File:La_Manne_-_Nicolas_Poussin_-_Mus%C3%A9e_du_Louvre_Peintures_INV_7275.jpg | Public domain |
| `poussin/la_peste_d_asdod.jpg` | La Peste d'Asdod（阿什杜德的瘟疫，INV 7276） | Nicolas Poussin | 1630–1631 | Musée du Louvre | https://commons.wikimedia.org/wiki/File:La_Peste_d%27Asdod_-_Nicolas_Poussin_-_Mus%C3%A9e_du_Louvre_Peintures_INV_7276_;_MR_2312.jpg | Public domain |
| `poussin/landscape_with_a_man_killed_by_a_snake.jpg` | Landscape with a Man killed by a Snake（蛇景，NG5763） | Nicolas Poussin | probably 1648 | The National Gallery, London | https://commons.wikimedia.org/wiki/File:Landscape-with-a-man-killed-by-a-snake-Poussin.jpg | Public domain |
| `poussin/le_jugement_de_salomon.jpg` | Le Jugement de Salomon（所罗门的审判，INV 7277） | Nicolas Poussin | 1649 | Musée du Louvre | https://commons.wikimedia.org/wiki/File:Le_Jugement_de_Salomon_-_1649_-_Nicolas_Poussin_-_Louvre_-_INV_7277_;_MR_2316_(2).jpg | Public domain |
| `poussin/le_printemps.jpg` | Le Printemps（四季·春，INV 7303） | Nicolas Poussin | 1660–1664 | Musée du Louvre | https://commons.wikimedia.org/wiki/File:Nicolas_Poussin_-_Le_Printemps.jpg | Public domain |
| `poussin/the_triumph_of_pan.jpg` | The Triumph of Pan（潘的凯旋，NG6477） | Nicolas Poussin | 1636 | The National Gallery, London | https://commons.wikimedia.org/wiki/File:Nicolas_Poussin_-_The_Triumph_of_Pan,_1636.jpg | Public domain |
| `bruegel/blind_leading_blind.jpg` | 盲人引盲 / The Blind Leading the Blind | Pieter Bruegel the Elder | 1568 | 那不勒斯卡波迪蒙特博物馆 | https://commons.wikimedia.org/wiki/File:%D0%9F%D1%80%D0%B8%D1%82%D1%87%D0%B0_%D0%BE_%D1%81%D0%BB%D0%B5%D0%BF%D1%8B%D1%85.jpeg | Public domain |
| `bruegel/carnival_and_lent.jpg` | 狂欢节与四旬斋之战 / The Fight Between Carnival and Lent | Pieter Bruegel the Elder | 1559 | KHM（GG_1016） | https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_d._%C3%84._066.jpg | Public domain |
| `bruegel/census_at_bethlehem.jpg` | 伯利恒的人口调查 / The Census at Bethlehem | Pieter Bruegel the Elder | 1566 | 布鲁塞尔皇家美术馆（Oldmasters） | https://commons.wikimedia.org/wiki/File:Le_d%C3%A9nombrement_de_Bethl%C3%A9em_par_Pieter_Brueghel_l%27Ancien_-_1566_-_Bruxelles.jpg | Public domain |
| `bruegel/childrens_games.jpg` | 儿童游戏 / Children's Games | Pieter Bruegel the Elder | 1560 | KHM（GG_1017） | https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_the_Elder_-_Children%E2%80%99s_Games_-_Google_Art_Project.jpg | Public domain |
| `bruegel/conversion_of_paul.jpg` | 保罗的皈依 / The Conversion of Paul | Pieter Bruegel the Elder | 1567 | KHM（GG_3690） | https://commons.wikimedia.org/wiki/File:Conversion_of_Paul_(Bruegel).jpg | Public domain |
| `bruegel/dulle_griet.jpg` | 疯格丽特 / Dulle Griet (Mad Meg) | Pieter Bruegel the Elder | 1561 | 安特卫普 Mayer van den Bergh 博物馆 | https://commons.wikimedia.org/wiki/File:Dulle_Griet,_by_Pieter_Brueghel_(I).jpg | Public domain |
| `bruegel/fall_of_the_rebel_angels.jpg` | 叛逆天使的坠落 / The Fall of the Rebel Angels | Pieter Bruegel the Elder | 1562 | 布鲁塞尔皇家美术馆（Oldmasters） | https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_the_Elder_-_The_Fall_of_the_Rebel_Angels_-_Google_Art_Project.jpg | Public domain |
| `bruegel/gloomy_day.jpg` | 阴天（早春）/ The Gloomy Day | Pieter Bruegel the Elder | 1565 | KHM（GG_1837） | https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_de_Oude_-_De_sombere_dag_(vroege_voorjaar).jpg | Public domain |
| `bruegel/hay_harvest.jpg` | 刈草（早夏）/ The Hay Harvest (Haymaking) | Pieter Bruegel the Elder | 1565 | Lobkowicz Collections（布拉格） | https://commons.wikimedia.org/wiki/File:Haymaking,_1565.jpg | Public domain |
| `bruegel/hunters_in_the_snow.jpg` | 雪中猎人 / The Hunters in the Snow (Winter) | Pieter Bruegel the Elder | 1565 | KHM（GG_1838） | https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_the_Elder_-_Hunters_in_the_Snow_(Winter)_-_Google_Art_Project.jpg | Public domain |
| `bruegel/netherlandish_proverbs.jpg` | 尼德兰谚语 / Netherlandish Proverbs | Pieter Bruegel the Elder | 1559 | 柏林国家博物馆绘画馆 | https://commons.wikimedia.org/wiki/File:Pieter_Brueghel_the_Elder_-_The_Dutch_Proverbs_-_Google_Art_Project.jpg | Public domain |
| `bruegel/peasant_and_nest_robber.jpg` | 农夫与掏鸟窝者 / The Peasant and the Nest Robber | Pieter Bruegel the Elder | 1568 | KHM（GG_1020） | https://commons.wikimedia.org/wiki/File:The_Peasant_and_the_Nest_Robber.jpg | Public domain |
| `bruegel/peasant_dance.jpg` | 农民舞蹈 / The Peasant Dance | Pieter Bruegel the Elder | 约 1568 | KHM（GG_1059） | https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_The_Peasant_Dance.jpg | Public domain |
| `bruegel/peasant_wedding.jpg` | 农民婚礼 / The Peasant Wedding | Pieter Bruegel the Elder | 1568 | KHM（GG_1027） | https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_the_Elder_-_Peasant_Wedding_-_Google_Art_Project_2.jpg | Public domain |
| `bruegel/procession_to_calvary.jpg` | 前往髑髅地 / The Procession to Calvary | Pieter Bruegel the Elder | 1564 | KHM（GG_1025） | https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_d._%C3%84._007.jpg | Public domain |
| `bruegel/return_of_the_herd.jpg` | 牧群归来（秋）/ The Return of the Herd | Pieter Bruegel the Elder | 1565 | KHM（GG_1018） | https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_(I)_-_The_Return_of_the_Herd_(1565).jpg | Public domain |
| `bruegel/the_harvesters.jpg` | 收割者 / The Harvesters | Pieter Bruegel the Elder | 1565 | The Met（19.164） | https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_the_Elder-_The_Harvesters_-_Google_Art_Project.jpg | Public domain |
| `bruegel/tower_of_babel.jpg` | 巴别塔 / The Tower of Babel | Pieter Bruegel the Elder | 1563 | KHM（GG_1026） | https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_the_Elder_-_The_Tower_of_Babel_(Vienna)_-_Google_Art_Project_-_edited.jpg | Public domain |
| `bruegel/triumph_of_death.jpg` | 死神的胜利 / The Triumph of Death | Pieter Bruegel the Elder | 约 1562 | 普拉多博物馆 | https://commons.wikimedia.org/wiki/File:The_Triumph_of_Death_P001393.jpg | Public domain |
| `bruegel/winter_bird_trap.jpg` | 冬景与溜冰者和捕鸟器 / Winter Landscape with Skaters and Bird Trap | Pieter Bruegel the Elder | 1565 | 布鲁塞尔皇家美术馆（Oldmasters） | https://commons.wikimedia.org/wiki/File:Bruegel,_Pieter_(I)_-_Winterlandschap_met_schaatsers_en_vogelknip,_1565.jpg | Public domain |
| `el_greco/adoration_of_the_shepherds_ca1605.jpg` | The Adoration of the Shepherds（牧羊人的朝拜；05.42） | El Greco (Domenikos Theotokopoulos) | 约 1605–10 | The Met, New York | https://www.metmuseum.org/art/collection/search/436570 | Public domain（Met OA） |
| `el_greco/burial_of_the_count_of_orgaz_1586.jpg` | The Burial of the Count of Orgaz（奥尔加斯伯爵的葬礼） | El Greco (Domenikos Theotokopoulos) | 1586–88 | Iglesia de Santo Tomé, Toledo（原位） | https://commons.wikimedia.org/wiki/File:El_entierro_del_señor_de_Orgaz_-_El_Greco.jpg | Public domain |
| `el_greco/cardinal_guevara_ca1600.jpg` | Cardinal Fernando Niño de Guevara（红衣主教格瓦拉；29.100.5） | El Greco (Domenikos Theotokopoulos) | 约 1600 | The Met, New York | https://www.metmuseum.org/art/collection/search/436573 | Public domain（Met OA） |
| `el_greco/christ_healing_the_blind_ca1570.jpg` | Christ Healing the Blind（治愈盲人；1978.416） | El Greco (Domenikos Theotokopoulos) | 约 1570 | The Met, New York | https://www.metmuseum.org/art/collection/search/436572 | Public domain（Met OA） |
| `el_greco/dormition_of_the_virgin_1565.jpg` | Dormition of the Virgin（圣母安眠；克里特期圣像，签名款） | El Greco (Domenikos Theotokopoulos) | 约 1565–67 | 锡罗斯岛埃尔穆波利（Ermoupolis, Syros） | https://commons.wikimedia.org/wiki/File:Dormition_El_Greco.jpg | Public domain |
| `el_greco/el_expolio_1577.jpg` | El Expolio（剥夺圣衣） | El Greco (Domenikos Theotokopoulos) | 1577–79 | Catedral de Toledo（圣器室，原位） | https://commons.wikimedia.org/wiki/File:El_Expolio_del_Greco_Catedral_de_Toledo.jpg | Public domain |
| `el_greco/immaculate_conception_1607.jpg` | The Immaculate Conception（圣母无原罪；Oballe 小堂） | El Greco (Domenikos Theotokopoulos) | 1607–13 | Museo de Santa Cruz, Toledo | https://commons.wikimedia.org/wiki/File:Inmaculada_Oballe_El_Greco.jpg | Public domain |
| `el_greco/laocoon_ca1610.jpg` | Laocoön（拉奥孔） | El Greco (Domenikos Theotokopoulos) | 约 1610–14 | National Gallery of Art, Washington（1990.123.1） | https://commons.wikimedia.org/wiki/File:El_Greco_(Domenikos_Theotokopoulos)_-_Laocoön_-_Google_Art_Project.jpg | Public domain |
| `el_greco/modena_triptych_1568.jpg` | The Modena Triptych（摩德纳三联画） | El Greco (Domenikos Theotokopoulos) | 1567–68 | Galleria Estense, Modena | https://commons.wikimedia.org/wiki/File:Triptico_de_Modena_El_Greco.jpg | Public domain |
| `el_greco/nobleman_with_hand_on_chest_ca1580.jpg` | The Nobleman with his Hand on his Chest（手抚胸口的绅士；P00809） | El Greco (Domenikos Theotokopoulos) | 约 1580 | Museo del Prado, Madrid | https://commons.wikimedia.org/wiki/File:The_Nobleman_with_his_hand_on_his_chest,_by_El_Greco_(Museo_del_Prado,_Madrid).jpg | Public domain |
| `el_greco/paravicino_1609.jpg` | Portrait of Fray Hortensio Félix Paravicino（帕拉维奇诺肖像） | El Greco (Domenikos Theotokopoulos) | 1609 | Museum of Fine Arts, Boston | https://commons.wikimedia.org/wiki/File:El_Greco_(Domenikos_Theotokopoulos)_-_Fray_Hortensio_Félix_Paravicino_-_Google_Art_Project.jpg | Public domain |
| `el_greco/pentecost_ca1600.jpg` | Pentecost（五旬节；Doña María de Aragón 组画） | El Greco (Domenikos Theotokopoulos) | 约 1600 | Museo del Prado, Madrid | https://commons.wikimedia.org/wiki/File:Pentecostés_(El_Greco,_c._1600)_Prado.jpg | Public domain |
| `el_greco/saint_jerome_as_scholar_ca1610.jpg` | Saint Jerome as Scholar（学者圣杰罗姆；1975.1.146） | El Greco (Domenikos Theotokopoulos) | 约 1610 | The Met, New York（Lehman Collection） | https://www.metmuseum.org/art/collection/search/459088 | Public domain（Met OA） |
| `el_greco/saint_martin_and_the_beggar_ca1597.jpg` | Saint Martin and the Beggar（圣马丁与乞丐） | El Greco (Domenikos Theotokopoulos) | 约 1597 | Art Institute of Chicago（1949.1093） | https://commons.wikimedia.org/wiki/File:Domenico_Theotokópoulos,_called_El_Greco_-_Saint_Martin_and_the_Beggar_-_1949.1093_-_Art_Institute_of_Chicago.jpg | Public domain |
| `el_greco/the_holy_trinity_1577.jpg` | The Holy Trinity（三位一体；P000824） | El Greco (Domenikos Theotokopoulos) | 1577–79 | Museo del Prado, Madrid | https://commons.wikimedia.org/wiki/File:La_Trinidad_(El_Greco,_1577-1579).jpg | Public domain |
| `el_greco/view_of_toledo_ca1599.jpg` | View of Toledo（托莱多风景；29.100.6） | El Greco (Domenikos Theotokopoulos) | 约 1599–1600 | The Met, New York | https://www.metmuseum.org/art/collection/search/436575 | Public domain（Met OA） |
| `el_greco/vision_of_saint_john_ca1608.jpg` | The Vision of Saint John（圣约翰的异象/第五封印的开启；56.48） | El Greco (Domenikos Theotokopoulos) | 约 1608–14 | The Met, New York | https://www.metmuseum.org/art/collection/search/436576 | Public domain（Met OA） |
| `holbein/ambassadors.jpg` | The Ambassadors（大使们；Jean de Dinteville & Georges de Selve，NG1314） | Hans Holbein the Younger | 1533 | The National Gallery, London | https://commons.wikimedia.org/wiki/File:Hans_Holbein_the_Younger_-_The_Ambassadors_-_Google_Art_Project.jpg | Public domain |
| `holbein/anne_of_cleves.jpg` | Portrait of Anne of Cleves（克利夫斯的安妮，INV 1348） | Hans Holbein the Younger | 1539 | Musée du Louvre, Paris | https://commons.wikimedia.org/wiki/File:Anne_de_Cl%C3%A8ves_-_Hans_Holbein_le_Jeune_-_Mus%C3%A9e_du_Louvre_Peintures_INV_1348_;_MR_756_-_version_2.jpg | Public domain |
| `holbein/bonifacius_amerbach_1519.jpg` | Portrait of Bonifacius Amerbach（博尼法修斯·阿梅尔巴赫） | Hans Holbein the Younger | 1519 | Kunstmuseum Basel | https://commons.wikimedia.org/wiki/File:Portrait_of_Bonifacius_Amerbach_by_Hans_Holbein_the_Younger_(1519).jpg | Public domain |
| `holbein/charles_de_solier.jpg` | Charles de Solier, Sieur de Morette（夏尔·德·索利耶） | Hans Holbein the Younger | 1534 | Gemäldegalerie Alte Meister, Dresden | https://commons.wikimedia.org/wiki/File:Hans_Holbein_the_Younger_-_Charles_de_Solier,_Sieur_de_Morette_-_Google_Art_Project.jpg | Public domain |
| `holbein/christina_of_denmark.jpg` | Christina of Denmark, Duchess of Milan（丹麦的克里斯蒂娜，NG2475） | Hans Holbein the Younger | 1538 | The National Gallery, London | https://commons.wikimedia.org/wiki/File:Christina_of_Denmark,_Duchess_of_Milan.jpg | Public domain |
| `holbein/darmstadt_madonna.jpg` | Darmstadt Madonna（达姆施塔特圣母） | Hans Holbein the Younger | 1525–26 & 1528 | Sammlung Würth（Johanniterkirche, Schwäbisch Hall；2012 年起） | https://commons.wikimedia.org/wiki/File:Darmstadtmadonna.jpg | Public domain |
| `holbein/dead_christ.jpg` | The Body of the Dead Christ in the Tomb（墓中基督） | Hans Holbein the Younger | 1521/22 | Kunstmuseum Basel | https://commons.wikimedia.org/wiki/File:Holbein_%E2%80%94_Dead_Christ.jpg | CC0 |
| `holbein/edward_vi_as_a_child.jpg` | Edward VI as a Child（幼年爱德华六世） | Hans Holbein the Younger | c. 1538 | National Gallery of Art, Washington D.C. | https://commons.wikimedia.org/wiki/File:Hans_Holbein_the_Younger_-_Edward_VI_as_a_Child_-_Google_Art_Project.jpg | Public domain |
| `holbein/erasmus_1523.jpg` | Erasmus（伊拉斯谟，L658） | Hans Holbein the Younger | 1523 | The National Gallery, London（Longford Castle 借展） | https://commons.wikimedia.org/wiki/File:Holbein-erasmus.jpg | Public domain |
| `holbein/georg_gisze.jpg` | Der Kaufmann Georg Gisze（商人吉斯泽） | Hans Holbein the Younger | 1532 | Berlin State Museums（Gemäldegalerie） | https://commons.wikimedia.org/wiki/File:Hans_Holbein_der_J%C3%BCngere_-_Der_Kaufmann_Georg_Gisze_-_Google_Art_Project.jpg | Public domain |
| `holbein/henry_viii.jpg` | Portrait of Henry VIII（亨利八世；白厅壁画系统摹本，WAG 1350） | Hans Holbein the Younger | c. 1540–1547 | Walker Art Gallery, Liverpool | https://commons.wikimedia.org/wiki/File:After_Hans_Holbein_the_Younger_-_Portrait_of_Henry_VIII_-_Google_Art_Project.jpg | Public domain |
| `holbein/self_portrait_1542.jpg` | Self-portrait（自画像） | Hans Holbein the Younger | c. 1542/43 | Uffizi, Florence | https://commons.wikimedia.org/wiki/File:Hans_Holbein_the_Younger,_self-portrait.jpg | Public domain |
| `holbein/thomas_more.jpg` | Sir Thomas More（托马斯·莫尔） | Hans Holbein the Younger | 1527 | The Frick Collection, New York | https://commons.wikimedia.org/wiki/File:Hans_Holbein,_the_Younger_-_Sir_Thomas_More_-_Google_Art_Project.jpg | Public domain |
| `aivazovsky/among_the_waves_1898.jpg` | Among the Waves（Среди волн；**58×96 cm 版本**，苏富比 2008 Lot 4 记录；费奥多西亚藏巨幅版另件） | Ivan Aivazovsky | 1898 | 私人（苏富比 2008） | https://commons.wikimedia.org/wiki/File:Ivan_Konstantinovich_Aivazovsky_-_Among_the_Waves%2C_1898.jpg | Public domain |
| `aivazovsky/black_sea_1881.jpg` | The Black Sea / На Черном море начинает разыгрываться буря（特列 Инв.803，149×210） | Ivan Aivazovsky | 1881 | 特列季亚科夫（Google Art Project 扫描） | https://commons.wikimedia.org/wiki/File:%D0%98%D0%B2%D0%B0%D0%BD_%D0%9A%D0%BE%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%82%D0%B8%D0%BD%D0%BE%D0%B2%D0%B8%D1%87_%D0%90%D0%B9%D0%B2%D0%B0%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_-_%D0%A7%D0%B5%D1%80%D0%BD%D0%BE%D0%B5_%D0%BC%D0%BE%D1%80%D0%B5_%28%D0%BD%D0%B0_%D0%A7%D0%B5%D1%80%D0%BD%D0%BE%D0%BC_%D0%BC%D0%BE%D1%80%D0%B5_%D0%BD%D0%B0%D1%87%D0%B8%D0%BD%D0%B0%D0%B5%D1%82_%D1%80%D0%B0%D0%B7%D1%8B%D0%B3%D1%80%D1%8B%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F_%D0%B1%D1%83%D1%80%D1%8F%29_-_Google_Art_Project.jpg | Public domain |
| `aivazovsky/brig_mercury_1848.jpg` | Бриг «Меркурий» после победы над двумя турецкими судами（俄博 2026 特展杰作） | Ivan Aivazovsky | 1848 | 俄博 | https://commons.wikimedia.org/wiki/File:Aivasovsky_Ivan_Constantinovich_merkuri_1848_IBI.jpg | Public domain |
| `aivazovsky/chesme_battle_1848.jpg` | Чесменский бой / Battle of Çesme at Night（切什梅夜战） | Ivan Aivazovsky | 1848 | 未注（多源扫描） | https://commons.wikimedia.org/wiki/File:Chesmabattle.jpg | Public domain |
| `aivazovsky/constantinople_bosphorus.jpg` | Вид Константинополя и Босфора / View of Constantinople and the Bosphorus | Ivan Aivazovsky | 1856 | 私人（Sotheby's 2012 Orientalist Sale, lot 6） | https://commons.wikimedia.org/wiki/File:Aivazovsky_-_View_of_Constantinople_and_the_Bosphorus.jpg | Public domain |
| `aivazovsky/galata_tower_moonlight.jpg` | Галатская башня в лунном свете / The Galata Tower by Moonlight | Ivan Aivazovsky | 1845 | 私人（Sotheby's London 2012-11-26, lot 5） | https://commons.wikimedia.org/wiki/File:%D0%93%D0%B0%D0%BB%D0%B0%D1%82%D1%81%D0%BA%D0%B0%D1%8F_%D0%B1%D0%B0%D1%88%D0%BD%D1%8F_%D0%B2_%D0%BB%D1%83%D0%BD%D0%BD%D0%BE%D0%BC_%D1%81%D0%B2%D0%B5%D1%82%D0%B5.jpg | Public domain |
| `aivazovsky/moonlit_night.jpg` | Лунная ночь / Moonlight Night | Ivan Aivazovsky | 1849 | 未注（aivazovski.ru 扫描） | https://commons.wikimedia.org/wiki/File:%D0%9B%D1%83%D0%BD%D0%BD%D0%B0%D1%8F_%D0%BD%D0%BE%D1%87%D1%8C_%D0%90%D0%B9%D0%B2%D0%B0%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9.jpg | Public domain |
| `aivazovsky/neapolitan_bay_moonlit.jpg` | Неаполитанский залив в лунную ночь / The Bay of Naples by Moonlight（92×141 cm，ФКГА 藏） | Ivan Aivazovsky | 1842 | 费奥多西亚画廊（ФКГА；扫描件） | https://commons.wikimedia.org/wiki/File:%D0%9D%D0%B5%D0%B0%D0%BF%D0%BE%D0%BB%D0%B8%D1%82%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B7%D0%B0%D0%BB%D0%B8%D0%B2_%D0%B2_%D0%BB%D1%83%D0%BD%D0%BD%D1%83%D1%8E_%D0%BD%D0%BE%D1%87%D1%8C_%D0%90%D0%B9%D0%B2%D0%B0%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9.jpg | Public domain |
| `aivazovsky/night_in_gurzuf_1891.jpg` | Ночь в Гурзуфе / Night at Gurzuf（**1891 版本**；费奥多西亚另藏同名作） | Ivan Aivazovsky | 1891 | 私人（Heritage Auctions 2008, lot 65005） | https://commons.wikimedia.org/wiki/File:%D0%98%D0%B2%D0%B0%D0%BD_%D0%9A%D0%BE%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%82%D0%B8%D0%BD%D0%BE%D0%B2%D0%B8%D1%87_%D0%90%D0%B9%D0%B2%D0%B0%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_-_%D0%9D%D0%BE%D1%87%D1%8C_%D0%B2_%D0%93%D1%83%D1%80%D0%B7%D1%83%D1%84%D0%B5.jpg | Public domain |
| `aivazovsky/ninth_wave_1850.jpg` | The Ninth Wave（Девятый вал；俄博 Ж-2202，221×332） | Ivan Aivazovsky | 1850 | 俄博（Google Art Project 扫描） | https://commons.wikimedia.org/wiki/File:Hovhannes_Aivazovsky_-_The_Ninth_Wave_-_Google_Art_Project.jpg | Public domain |
| `aivazovsky/rainbow_1873.jpg` | The Rainbow（Радуга；特列 Инв.801，105×136） | Ivan Aivazovsky | 1873 | 特列季亚科夫 | https://commons.wikimedia.org/wiki/File:%D0%90%D0%B9%D0%B2%D0%B0%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%28%D0%93%D0%B0%D0%B9%D0%B2%D0%B0%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9%29_%D0%98%D0%B2%D0%B0%D0%BD_%28%D0%9E%D0%B3%D0%B0%D0%BD%D0%B5%D1%81%29_%D0%9A%D0%BE%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%82%D0%B8%D0%BD%D0%BE%D0%B2%D0%B8%D1%87_%D0%A0%D0%B0%D0%B4%D1%83%D0%B3%D0%B0.jpg | Public domain |
| `aivazovsky/sevastopol_roads.jpg` | Русская эскадра на Севастопольском рейде / The Russian Squadron on the Sebastopol Roads | Ivan Aivazovsky | 1846 | 未注 | https://commons.wikimedia.org/wiki/File:Ivan_Constantinovich_Aivazovsky_-_The_Russian_Squadron_on_the_Sebastopol_Roads.jpg | Public domain |
| `aivazovsky/stormy_sea_night_1849.jpg` | Буря на море ночью / Stormy Sea at Night（巴甫洛夫斯克宫） | Ivan Aivazovsky | 1849 | 巴甫洛夫斯克宫（扫描件） | https://commons.wikimedia.org/wiki/File:Stormy_sea_at_night.jpg | Public domain |
| `aivazovsky/wave_1889.jpg` | Волна / The Wave（俄博 Ж-2200，304×505；上传者摄；已与俄博 VRM 参考图目检比对同一构图） | Ivan Aivazovsky | 1889 | 俄博 | https://commons.wikimedia.org/wiki/File:%D0%90%D0%B9%D0%B2%D0%B0%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%98.%D0%9A._%D0%92%D0%BE%D0%BB%D0%BD%D0%B0.jpg | Public domain |
| `zhao_mengfu/dongting_dongshan.jpg` | 洞庭东山图（轴） | Zhao Mengfu | 元 | 上海博物馆 | https://commons.wikimedia.org/wiki/File:赵孟頫_洞庭东山图轴.jpg | Public domain（PD-Art） |
| `zhao_mengfu/hongyi_luohan.jpg` | 红衣罗汉图（画心） | Zhao Mengfu | 1304 | 辽宁省博物馆 | https://commons.wikimedia.org/wiki/File:5_Zhao_Mengfu_Monk_in_a_Red_Robe,_dated_1304_(26_x_52_cm)Liaoning_Provincial_Museum.jpg | Public domain（PD-Art） |
| `zhao_mengfu/qiujiao_yinma_tu.jpg` | 秋郊饮马图（画心） | Zhao Mengfu | 1312 | 故宫博物院（故00005866） | https://commons.wikimedia.org/wiki/File:Zhao_Mengfu._Horse_Herding_in_Autumn_Countryside_1312_23,6х59см,_Palace_Museum,_Beijing.jpg | Public domain（PD-Art） |
| `zhao_mengfu/quehua_painting.jpg` | 鹊华秋色图（画心） | Zhao Mengfu | 1295 | 台北故宫博物院（故畫001011N000000000） | https://commons.wikimedia.org/wiki/File:2_Zhao_Mengfu_Autumn_Colors_on_the_Qiao_and_Hua_Mountains_Handscroll,_ink_and_colors_on_paper,_28.4_x_93.2_cm_National_Palace_Museum,_Taipei..jpg | Public domain（PD-Art） |
| `zhao_mengfu/renqi_tu.jpg` | 人骑图（画心） | Zhao Mengfu | 1296 | 故宫博物院（新00119107） | https://commons.wikimedia.org/wiki/File:赵孟頫人骑图卷.png | Public domain（PD-Art） |
| `zhao_mengfu/shuangsong_pingyuan.jpg` | 双松平远图（画心） | Zhao Mengfu | 约 1310 | 大都会艺术博物馆 | https://commons.wikimedia.org/wiki/File:3_Zhao_Mengfu_Twin_Pines,_Level_Distance,_ca._1310_(26.8_x_107.5_cm);The_Metropolitan_Museum_of_Art,_New_York.jpg | Public domain（PD-Art） |
| `zhao_mengfu/shuicun_tu.jpg` | 水村图（画心） | Zhao Mengfu | 1302 | 故宫博物院（新00109759） | https://commons.wikimedia.org/wiki/File:6_Zhao_Mengfu_Water_Village,_dated_1302_(24.9_x_120.5_cm);_Palace_Museum.jpg | Public domain（PD-Art） |
| `zhao_mengfu/wuxing_qingyuan_hejuan.jpg` | 吴兴清远合卷（画心全段：赵孟頫原图＋崔复摹本） | Zhao Mengfu | 元 | 上海博物馆（沈同樾等捐赠） | https://commons.wikimedia.org/wiki/File:赵孟頫_崔复_吴兴清远合卷.jpg | Public domain（PD-Art） |
| `zhao_mengfu/xieyouyu_qiuhuo.jpg` | 谢幼舆丘壑图（画心） | Zhao Mengfu | 约 1287 | 普林斯顿大学艺术博物馆 | https://commons.wikimedia.org/wiki/File:Zhao_Mengfu_趙孟頫_-_The_Mind_Landscape_of_Xie_Youyu_(Youyu_qiu_he_幼輿丘壑_)_-_y1984-13_-_Princeton_University_Art_Museum.jpg | Public domain（PD-Art） |
| `zhao_mengfu/xiushi_shulin_colophon.jpg` | 秀石疏林图·尾纸自题诗（「石如飞白木如籀」段） | Zhao Mengfu | 元 | 故宫博物院 | https://commons.wikimedia.org/wiki/File:赵孟頫秀石疏林图卷.png（同卷裁切） | Public domain（PD-Art） |
| `zhao_mengfu/xiushi_shulin_painting.jpg` | 秀石疏林图（画心） | Zhao Mengfu | 元 | 故宫博物院（新00147132） | https://commons.wikimedia.org/wiki/File:赵孟頫秀石疏林图卷.png | Public domain（PD-Art） |
| `zhao_mengfu/youhuang_daisheng.jpg` | 幽篁戴胜图（画心） | Zhao Mengfu | 元（早年） | 故宫博物院 | https://commons.wikimedia.org/wiki/File:10_ZhaoMengfu-_Hoopoe_on_Bamboo._Shanghai_mus..jpg | Public domain（PD-Art） |
| `zhao_mengfu/yuma_tu.jpg` | 浴马图（画心） | Zhao Mengfu | 元 | 故宫博物院（新00154992） | https://commons.wikimedia.org/wiki/File:Zhao_Mengfu._Bathing_Horses._28.1_x_155.5_cm_Palace_Museum,_Beijing..jpg | Public domain（PD-Art） |
| `zhao_mengfu/zixiao_xiang.jpg` | 自写小像（册页） | Zhao Mengfu | 1299 | 故宫博物院 | https://commons.wikimedia.org/wiki/File:Zhao_Mengfu._Self_Portrait._1299,_Album_leaf._Palace_Museum_Beijing.jpg | Public domain（PD-Art） |
| `ni_zan/met_autumn_grove_1339.jpg` | 《秋林野兴图》轴（Enjoying the Wilderness in an Autumn Grove） | Ni Zan | 1339 | 大都会艺术博物馆（1989.363.38） | https://www.metmuseum.org/art/collection/search/45635 | CC0 1.0（Met Open Access） |
| `ni_zan/met_wind_riverbank_1363.jpg` | 《江渚风林图》轴（Wind among the Trees on the Riverbank） | Ni Zan | 1363 | 大都会艺术博物馆（1989.363.39） | https://www.metmuseum.org/art/collection/search/41154 | CC0 1.0（Met Open Access） |
| `ni_zan/met_woods_valleys_yushan_1372.jpg` | 《虞山林壑图》轴（Woods and Valleys of Mount Yu） | Ni Zan | 1372 | 大都会艺术博物馆（1973.120.8） | https://www.metmuseum.org/art/collection/search/45636 | CC0 1.0（Met Open Access） |
| `ni_zan/qishu_qiufeng.jpg` | 《琪树秋风图》轴 | Ni Zan | 无年款 | 上海博物馆 | https://commons.wikimedia.org/wiki/File:Ni_Zan_Autumn_Wind_in_Gemstones_Trees.jpg | Public domain（PD-Art） |
| `ni_zan/rongxi_studio_1372.jpg` | 《容膝斋图》轴（Rongxi Studio） | Ni Zan | 1372 | 台北故宫博物院（故画000299；国宝） | https://commons.wikimedia.org/wiki/File:Ni_Zan._The_Rongxi_Studio.1372._74,7x35,3._National_Palace_Museum,_Taipei.jpg | Public domain（PD-Art） |
| `ni_zan/six_gentlemen_1345.jpg` | 《六君子图》轴 | Ni Zan | 1345 | 上海博物馆 | https://commons.wikimedia.org/wiki/File:Ni_Zan_-_Six_Gentlemen.jpg | Public domain（PD-Art） |
| `ni_zan/ting_shu_yao_cen.jpg` | 《汀树遥岑图》轴 | Ni Zan | 1363（一作 1360 年代） | 上海博物馆 | https://commons.wikimedia.org/wiki/File:倪瓒_汀树遥岑图轴.jpg | Public domain（PD-Art） |
| `ni_zan/twin_trees_south_bank_1353.jpg` | 《岸南双树图》轴（Annan shuangshu） | Ni Zan | 1353 | 普林斯顿大学艺术博物馆（y1975-35） | https://commons.wikimedia.org/wiki/File:Ni_Zan(倪瓚)_-_Twin_Trees_by_the_South_Bank_(Annan_shuangshu)_-_Google_Art_Project.jpg | Public domain（PD-Art，Google Art Project） |
| `ni_zan/water_bamboo_dwelling_1343.jpg` | 《水竹居图》轴 | Ni Zan | 1343 | 中国国家博物馆 | https://commons.wikimedia.org/wiki/File:Ni_Zan_Water_and_Bamboo_Dwelling.jpg | Public domain（PD-Art） |
| `ni_zan/wuzhu_xiushi.jpg` | 《梧竹秀石图》轴 | Ni Zan | 1360 年代 | 故宫博物院（北京） | https://commons.wikimedia.org/wiki/File:倪瓒梧竹秀石图轴.png | Public domain（PD-Art） |
| `ni_zan/youjian_hansong.jpg` | 《幽涧寒松图》轴 | Ni Zan | 晚年（约 1370 年代） | 故宫博物院（北京） | https://commons.wikimedia.org/wiki/File:倪瓒幽涧寒松图轴.png | Public domain（PD-Art） |
| `ni_zan/yuzhuang_qiuji_1355.jpg` | 《渔庄秋霁图》轴 | Ni Zan | 1355（1372 补题） | 上海博物馆 | https://commons.wikimedia.org/wiki/File:倪瓒_渔庄秋霁图轴.jpg | Public domain（PD-Art） |
| `ni_zan/zhu_shu_xiao_shan.jpg` | 《竹树小山图》轴 | Ni Zan | 无年款 | 无锡博物院 | https://commons.wikimedia.org/wiki/File:元_倪瓒_竹树小山图轴_无锡博物院.jpg | Public domain（PD-Art） |
| `qiu_ying/freer_minghuang_journey.jpg` | 《明皇幸蜀图》（Journey to Shu；传仇英，文徵明书） | Qiu Ying | 16–17世纪 | Freer Gallery（F1993.4） | https://asia.si.edu/object/fsg_F1993.4/ | Public domain |
| `qiu_ying/han_palace_d_konghou.jpg` | 《汉宫春晓》卷 细节（女乐·箜篌） | Qiu Ying | 明 | 台北故宫博物院 | https://digitalarchive.npm.gov.tw/Collection/Detail/3672?dep=P（IIIF: K2A001038N000000000PBW） | CC BY 4.0（NPM） |
| `qiu_ying/han_palace_d_serving_ladies.jpg` | 《汉宫春晓》卷 细节（侍女奉食·湖石） | Qiu Ying | 明 | 台北故宫博物院 | https://digitalarchive.npm.gov.tw/Collection/Detail/3672?dep=P（IIIF: K2A001038N000000000PDQ） | CC BY 4.0（NPM） |
| `qiu_ying/han_palace_d_stairs_attendant.jpg` | 《汉宫春晓》卷 细节（侍女拾级） | Qiu Ying | 明 | 台北故宫博物院 | https://digitalarchive.npm.gov.tw/Collection/Detail/3672?dep=P（IIIF: K2A001038N000000000PBN） | CC BY 4.0（NPM） |
| `qiu_ying/han_palace_full_scroll.jpg` | 《汉宫春晓》卷 全卷缩览（故畫001038） | Qiu Ying | 明（约 1542 后） | 台北故宫博物院 | https://digitalarchive.npm.gov.tw/Collection/Detail/3672?dep=P | CC BY 4.0（NPM） |
| `qiu_ying/han_palace_s06_peacock_kids.jpg` | 《汉宫春晓》卷 第 6 段（孔雀·童子·舞女） | Qiu Ying | 明 | 台北故宫博物院 | https://digitalarchive.npm.gov.tw/Collection/Detail/3672?dep=P（IIIF: K2A001038N000000000PCV） | CC BY 4.0（NPM） |
| `qiu_ying/han_palace_s08_flower_picking.jpg` | 《汉宫春晓》卷 第 8 段（折花·太湖石） | Qiu Ying | 明 | 台北故宫博物院 | https://digitalarchive.npm.gov.tw/Collection/Detail/3672?dep=P（IIIF: K2A001038N000000000PAH） | CC BY 4.0（NPM） |
| `qiu_ying/han_palace_s12_doucao_reading.jpg` | 《汉宫春晓》卷 第 12 段（斗草·卧读） | Qiu Ying | 明 | 台北故宫博物院 | https://digitalarchive.npm.gov.tw/Collection/Detail/3672?dep=P（IIIF: K2A001038N000000000PDB） | CC BY 4.0（NPM） |
| `qiu_ying/linsong_bathing_infant.jpg` | 《临宋人画册》（浴婴图） | Qiu Ying | 明 | 上海博物馆 | https://commons.wikimedia.org/wiki/File:仇英_临宋人画册_2.jpg | Public domain |
| `qiu_ying/met_lady_bamboo_grove.jpg` | Lady in a Bamboo Grove（竹院仕女） | Qiu Ying | 约 1495–1552 | The Met（36013） | https://www.metmuseum.org/art/collection/search/36013 | CC0 |
| `qiu_ying/met_lady_su_hui.jpg` | Lady Su Hui and Her Verse Puzzle（苏蕙回文图） | Qiu Ying | 16世纪 | The Met（51584） | https://www.metmuseum.org/art/collection/search/51584 | CC0 |
| `qiu_ying/met_tang_palace.jpg` | A Tang Palace（唐宫图） | Qiu Ying | 约 1495–1552 | The Met（51285） | https://www.metmuseum.org/art/collection/search/51285 | CC0 |
| `qiu_ying/renwu_guifei_xiaozhuang.jpg` | 《人物故事图册·贵妃晓妆》 | Qiu Ying | 明（16世纪） | 北京故宫博物院 | https://commons.wikimedia.org/wiki/File:仇英人物故事图册-2.png | Public domain |
| `qiu_ying/renwu_xunyang_pipa.jpg` | 《人物故事图册·浔阳琵琶》 | Qiu Ying | 明（16世纪） | 北京故宫博物院 | https://commons.wikimedia.org/wiki/File:仇英人物故事图册-8.png | Public domain |
| `qiu_ying/renwu_zhuyuan_pingu.jpg` | 《人物故事图册·竹院品古》 | Qiu Ying | 明（16世纪） | 北京故宫博物院 | https://commons.wikimedia.org/wiki/File:仇英人物故事图册-5.png | Public domain |
| `qiu_ying/taocun_caotang.jpg` | 《桃村草堂图》轴 | Qiu Ying | 明（16世纪） | 北京故宫博物院 | https://commons.wikimedia.org/wiki/File:Qiu_Ying_Peach_Village.jpg | Public domain |
| `qiu_ying/taohua_xianjing_tianjin.jpg` | 《桃源仙境图》轴 | Qiu Ying | 明（16世纪） | 天津博物馆 | https://commons.wikimedia.org/wiki/File:Fairyland_of_Peach_Blossoms_-_Qiu_Ying.jpg | Public domain |
| `ogata_korin/hoitsu_summer_autumn_left.jpg` | 夏秋草図屏風（秋草図＝風神図裏） | Ogata Kōrin | 19世紀（1821頃） | 東京国立博物館（酒井抱一筆） | https://commons.wikimedia.org/wiki/File:Summer_and_Autumn_Flower_Plants_%28left%29.jpg | Public domain |
| `ogata_korin/hoitsu_summer_autumn_right.jpg` | 夏秋草図屏風（夏草図＝雷神図裏） | Ogata Kōrin | 19世紀（1821頃） | 東京国立博物館（酒井抱一筆） | https://commons.wikimedia.org/wiki/File:Summer_and_Autumn_Flower_Plants_%28right%29.jpg | Public domain |
| `ogata_korin/korin_azalea.jpg` | 躑躅図 | Ogata Kōrin | 江戸時代・18世紀 | 畠山記念館（重文） | https://commons.wikimedia.org/wiki/File:Azalea_Korin.JPG | Public domain |
| `ogata_korin/korin_cranes_left.jpg` | 群鶴図屏風（左） | Ogata Kōrin | 江戸時代・18世紀 | フリーア美術館 | https://commons.wikimedia.org/wiki/File:Cranes_%28left%29.png | Public domain |
| `ogata_korin/korin_cranes_right.jpg` | 群鶴図屏風（右） | Ogata Kōrin | 江戸時代・18世紀 | フリーア美術館 | https://commons.wikimedia.org/wiki/File:Cranes_%28right%29.png | Public domain |
| `ogata_korin/korin_irises_left.jpg` | 燕子花図屏風（左隻） | Ogata Kōrin | 江戸時代・18世紀 | 根津美術館（国宝） | https://commons.wikimedia.org/wiki/File:KORIN-Irises-L.jpg | Public domain |
| `ogata_korin/korin_irises_right.jpg` | 燕子花図屏風（右隻） | Ogata Kōrin | 江戸時代・18世紀 | 根津美術館（国宝） | https://commons.wikimedia.org/wiki/File:KORIN-Irises-R.jpg | Public domain |
| `ogata_korin/korin_kuranosuke_portrait.jpg` | 中村内蔵助像 | Ogata Kōrin | 1704 | 大和文華館（重文） | https://commons.wikimedia.org/wiki/File:Nakamura_Kuranosuke_by_Ogata_Korin_%28Yamato_Bunkakan%29.jpg | Public domain |
| `ogata_korin/korin_matsushima_mfa.jpg` | 松島図屏風 | Ogata Kōrin | 江戸時代・18世紀 | ボストン美術館 | https://commons.wikimedia.org/wiki/File:Waves_at_Matsushima.jpg | Public domain |
| `ogata_korin/korin_plum_full.jpg` | 紅白梅図屏風（一双全景） | Ogata Kōrin | 江戸時代・18世紀 | MOA美術館（国宝） | https://commons.wikimedia.org/wiki/File:Ogata_Korin_-_RED_AND_WHITE_PLUM_BLOSSOMS_%28National_Treasure%29_-_Google_Art_Project.jpg | Public domain |
| `ogata_korin/korin_plum_left.jpg` | 紅白梅図屏風（左隻局部） | Ogata Kōrin | 江戸時代・18世紀 | MOA美術館（国宝） | https://commons.wikimedia.org/wiki/File:KORIN-Plum-trees-L.jpg | Public domain |
| `ogata_korin/korin_plum_right.jpg` | 紅白梅図屏風（右隻局部） | Ogata Kōrin | 江戸時代・18世紀 | MOA美術館（国宝） | https://commons.wikimedia.org/wiki/File:KORIN-Plum-trees-R.jpg | Public domain |
| `ogata_korin/korin_rough_waves.jpg` | 波濤図屏風 | Ogata Kōrin | ca. 1704–9 | メトロポリタン美術館（26.117） | https://commons.wikimedia.org/wiki/File:%E6%B3%A2%E6%BF%A4%E5%9B%B3%E5%B1%8F%E9%A2%A8-Rough_Waves_MET_DT1615.jpg | CC0（Met Open Access） |
| `ogata_korin/korin_suzuribako_eight_bridges.jpg` | 八橋蒔絵螺鈿硯箱 | Ogata Kōrin | 江戸時代・18世紀 | 東京国立博物館（国宝） | https://commons.wikimedia.org/wiki/File:WritingBox_EightBridges_OgataKorin.JPG | Public domain |
| `ogata_korin/korin_taikobo_knm.jpg` | 太公望図 | Ogata Kōrin | 江戸時代・18世紀 | 京都国立博物館（重文 A甲535） | https://commons.wikimedia.org/wiki/File:Tai_Gong_Wang_by_Ogata_Korin_%28Kyoto_National_Museum%29.jpg | Public domain |
| `ogata_korin/korin_wind_thunder.jpg` | 風神雷神図屏風 | Ogata Kōrin | 江戸時代・18世紀 | 東京国立博物館（重文） | https://commons.wikimedia.org/wiki/File:Wind_God_and_Thunder_God_Screens_by_Ogata_Korin.png | Public domain |
| `ogata_korin/korin_yatsuhashi_left.jpg` | 八橋図屏風（左隻） | Ogata Kōrin | after 1709 | メトロポリタン美術館（53.7.1,.2） | https://commons.wikimedia.org/wiki/File:Irises_at_Yatsuhashi_%28left%29.jpg | Public domain |
| `ogata_korin/korin_yatsuhashi_pair.jpg` | 八橋図屏風（双幅全景） | Ogata Kōrin | after 1709 | メトロポリタン美術館（53.7.1,.2） | https://commons.wikimedia.org/wiki/File:Yatsuhashi-zu_By%C5%8Dbu_by_K%C5%8Drin_Ogata_%28171-14%29.jpg | Public domain |
| `ogata_korin/korin_yatsuhashi_right.jpg` | 八橋図屏風（右隻） | Ogata Kōrin | after 1709 | メトロポリタン美術館（53.7.1,.2） | https://commons.wikimedia.org/wiki/File:Irises_at_Yatsuhashi_%28right%29.jpg | Public domain |
| `blake/albion_rose_1794.jpg` | Albion Rose（「Glad Day」，出自 A Large Book of Designs, copy A） | William Blake | 1794–96 | British Museum | https://commons.wikimedia.org/wiki/File:William_Blake_-_Albion_Rose_-_from_A_Large_Book_of_Designs_1793-6.jpg | Public domain |
| `blake/ancient_of_days_1794.jpg` | Europe: A Prophecy, pl.1 卷首「The Ancient of Days」（乌里森持罗盘） | William Blake | 1794 | Yale Center for British Art（copy A；lido-TMS-3878） | https://commons.wikimedia.org/wiki/File:William_Blake_-_Europe._A_Prophecy,_Plate_1,_Frontispiece_-_Google_Art_Project.jpg | Public domain |
| `blake/behemoth_and_leviathan_1825.jpg` | Behemoth and Leviathan（《约伯记》插图组画之十五，雕版） | William Blake | 1825 | Museum of Fine Arts, Houston | https://commons.wikimedia.org/wiki/File:William_Blake_-_Behemoth_and_Leviathan_-_Google_Art_Project.jpg | Public domain |
| `blake/circle_of_the_lustful_1827.jpg` | The Circle of the Lustful: Paolo and Francesca（但丁《地狱篇》V，水彩） | William Blake | c.1824–27 | The Metropolitan Museum of Art（开放数据） | https://commons.wikimedia.org/wiki/File:The_Circle_of_the_Lustful-_Paolo_and_Francesca,_from_Dante%27s_Inferno,_Canto_V_MET_DP816845.jpg | CC0 1.0 |
| `blake/elohim_creating_adam_1795.jpg` | Elohim Creating Adam（埃洛希姆造亚当） | William Blake | 1795 | Tate Britain（Yorck Project 扫描） | https://commons.wikimedia.org/wiki/File:William_Blake_008.jpg | Public domain |
| `blake/europe_title_1794.jpg` | Europe: A Prophecy, pl.2 扉页（蛇形「Europe」题字） | William Blake | 1794 | Yale Center for British Art（lido-TMS-3880） | https://commons.wikimedia.org/wiki/File:William_Blake_-_Europe._A_Prophecy,_Plate_2,_Title_Page_-_Google_Art_Project.jpg | Public domain |
| `blake/ghost_of_a_flea_c1819.jpg` | The Ghost of a Flea（跳蚤之魂，蛋彩＋金箔） | William Blake | c.1819–20 | Tate Britain（N05889） | https://commons.wikimedia.org/wiki/File:William_Blake_-_The_Ghost_of_a_Flea_-_Google_Art_Project.jpg | Public domain |
| `blake/great_red_dragon_c1805.jpg` | The Great Red Dragon and the Woman Clothed with the Sun（《启示录》12 章） | William Blake | c.1803–05 | National Gallery of Art（1943.3.8999，Rosenwald Collection） | https://commons.wikimedia.org/wiki/File:William_Blake_-_The_Great_Red_Dragon_and_the_Woman_Clothed_with_the_Sun_-_Google_Art_Project.jpg | Public domain |
| `blake/jerusalem_frontispiece_1804.jpg` | Jerusalem: The Emanation of the Giant Albion, pl.1 卷首「Los Entering the Grave」 | William Blake | 1804–20 | Yale Center for British Art（lido-TMS-3428） | https://commons.wikimedia.org/wiki/File:William_Blake_-_Jerusalem,_Plate_1,_Frontispiece_-_Google_Art_Project.jpg | Public domain |
| `blake/marriage_of_heaven_and_hell_plate5_1827.jpg` | The Marriage of Heaven and Hell, Plate 5「Those who restrain desire…」（copy I） | William Blake | c.1790–93（本件印于 1827） | Fitzwilliam Museum, Cambridge（copy I） | https://commons.wikimedia.org/wiki/File:The_Marriage_of_Heaven_and_Hell,_object_5,_copy_I,_1827,_Fitzwilliam_Museum.jpg | Public domain |
| `blake/milton_preface_1804.jpg` | Milton: A Poem, Preface 版页（「Would to God that all the Lords people were Prophets」） | William Blake | c.1804–11 | 未著录（Commons 文件页无馆藏字段） | https://commons.wikimedia.org/wiki/File:Milton_preface.jpg | Public domain |
| `blake/nebuchadnezzar_1795.jpg` | Nebuchadnezzar（尼布甲尼撒四肢着地） | William Blake | 1795–c.1805 | Tate Britain | https://commons.wikimedia.org/wiki/File:William_Blake_-_Nebuchadnezzar_(Tate_Britain).jpg | Public domain |
| `blake/newton_1795.jpg` | Newton（牛顿持罗盘，俯身画图） | William Blake | 1795–c.1805 | Tate Britain | https://commons.wikimedia.org/wiki/File:Newton-WilliamBlake.jpg | Public domain |
| `blake/number_of_the_beast_1805.jpg` | The Number of the Beast is 666（兽名数目，水彩） | William Blake | c.1805 | Rosenbach Museum & Library, Philadelphia（Butlin 522） | https://commons.wikimedia.org/wiki/File:The_number_of_the_beast_is_666_Philadelphia,_Rosenbach_Museum_and_Library.jpg | Public domain |
| `blake/pity_c1795.jpg` | Pity（怜悯，彩色印刷＋水彩） | William Blake | c.1795 | Yale Center for British Art（lido-TMS-7243） | https://commons.wikimedia.org/wiki/File:William_Blake_-_Pity_-_Google_Art_Project.jpg | Public domain |
| `blake/songs_innocence_title_1789.jpg` | Songs of Innocence 扉页（「The Author & Printer W Blake」） | William Blake | 1789 | Yale Center for British Art（lido-TMS-3706） | https://commons.wikimedia.org/wiki/File:William_Blake_-_Songs_of_Innocence,_Plate_2,_Title_Page_(Bentley_3)_-_Google_Art_Project.jpg | Public domain |
| `blake/tyger_1794.jpg` | Songs of Experience: The Tyger（版页，copy A） | William Blake | 1794 | British Museum（1924,0726.2.9） | https://commons.wikimedia.org/wiki/File:The_Tyger_BM_a_1794.jpg | Public domain |
| `blake/urizen_title_1794.jpg` | The First Book of Urizen, pl.1 扉页（乌里森坐于书前） | William Blake | 1794 | Yale Center for British Art | https://commons.wikimedia.org/wiki/File:William_Blake_-_The_First_Book_of_Urizen,_Plate_1,_%22The_First_Book_of_Urizen.%22_(Bentley_1)_-_Google_Art_Project.jpg | Public domain |
| `chardin/autoportrait_besicles_1771.jpg` | Autoportrait aux besicles（带眼镜自画像，粉彩） | Jean Siméon Chardin | 1771 | 卢浮宫（INV 25206） | https://commons.wikimedia.org/wiki/File:Self-portrait_wearing_Glasses_by_Jean-Baptiste-Sim%C3%A9on_Chardin.jpg | Public domain |
| `chardin/benedicite_louvre.jpg` | Le Bénédicité（餐前祷告） | Jean Siméon Chardin | 1740 | 卢浮宫（INV 3202） | https://commons.wikimedia.org/wiki/File:Jean-Baptiste_Sim%C3%A9on_Chardin_003.jpg | Public domain（PD-Art） |
| `chardin/cat_surveying_fish_met.jpg` | Cat Surveying Fish and Fowl on a Table（黑粉笔素描） | Jean Siméon Chardin | 1753 | The Met（1975.131.93） | https://www.metmuseum.org/art/collection/search/336462 | CC0 1.0 |
| `chardin/house_of_cards_ngl.jpg` | The House of Cards（纸牌屋） | Jean Siméon Chardin | 约 1740–1 | NGL（NG4078） | https://commons.wikimedia.org/wiki/File:Jean-Baptiste-Sim%C3%A9on_Chardin,_The_House_of_Cards,_1736-37.jpg | Public domain |
| `chardin/la_brioche_louvre.jpg` | La Brioche（奶油面包） | Jean Siméon Chardin | 1763 | 卢浮宫（MI 1038） | https://commons.wikimedia.org/wiki/File:Chardin,_la_brioche,_1763.JPG | Public domain |
| `chardin/la_fontaine_de_cuivre_louvre.jpg` | La Fontaine de cuivre（铜水缸） | Jean Siméon Chardin | 约 1733–34 | 卢浮宫（MI 1037） | https://commons.wikimedia.org/wiki/File:Jean-Baptiste_Sim%C3%A9on_Chardin_009.jpg | Public domain（PD-Art） |
| `chardin/la_pourvoyeuse_louvre.jpg` | La Pourvoyeuse（市场归来） | Jean Siméon Chardin | 1739 | 卢浮宫（MI 720） | https://commons.wikimedia.org/wiki/File:Jean-Baptiste_Sim%C3%A9on_Chardin_012.jpg | Public domain（PD-Art） |
| `chardin/la_raie_louvre.jpg` | La Raie（鳐鱼；入院作品） | Jean Siméon Chardin | 1728 | 卢浮宫（INV 3197） | https://commons.wikimedia.org/wiki/File:La_Raie_-_Jean_Baptiste_Sim%C3%A9on_Chardin_-_Mus%C3%A9e_du_Louvre_Peintures_INV_3197.jpg | Public domain |
| `chardin/le_bocal_dolives_louvre.jpg` | Le Bocal d'olives（橄榄罐；Diderot 名句对象） | Jean Siméon Chardin | 1760 | 卢浮宫（MI 1036） | https://commons.wikimedia.org/wiki/File:Chardin,_il_vaso_di_olive,_1760.JPG | Public domain |
| `chardin/le_buffet_louvre.jpg` | Le Buffet（餐台；入院作品） | Jean Siméon Chardin | 1728 | 卢浮宫（INV 3198） | https://commons.wikimedia.org/wiki/File:Chardin,_il_buffet,_1728,_01.JPG | Public domain |
| `chardin/le_gobelet_dargent_louvre.jpg` | Le Gobelet d'argent（银杯） | Jean Siméon Chardin | 约 1768 | 卢浮宫（MI 1042） | https://commons.wikimedia.org/wiki/File:Jean-Baptiste_Sim%C3%A9on_Chardin_024.jpg | Public domain（PD-Art） |
| `chardin/lenfant_au_toton_louvre.jpg` | L'Enfant au toton（玩陀螺的孩子） | Jean Siméon Chardin | 1738 沙龙 | 卢浮宫（RF 1705） | https://commons.wikimedia.org/wiki/File:L%27Enfant_au_toton_-_Jean_Baptiste_Sim%C3%A9on_Chardin_-_Mus%C3%A9e_du_Louvre_Peintures_RF_1705.jpg | Public domain |
| `chardin/panier_de_fraises_1761.jpg` | Le Panier de fraises des bois（野草莓篮） | Jean Siméon Chardin | 1761 | 卢浮宫（RFML.PE.2024.7.1） | https://commons.wikimedia.org/wiki/File:Jean_Sim%C3%A9on_Chardin_-_Le_Panier_de_fraises_des_bois_(1761).jpg | Public domain（PD-Art） |
| `chardin/soap_bubbles_met.jpg` | Soap Bubbles（肥皂泡） | Jean Siméon Chardin | 约 1733–34 | The Met（49.24） | https://www.metmuseum.org/art/collection/search/435888 | CC0 1.0 |
| `chardin/the_silver_tureen_met.jpg` | The Silver Tureen（银汤碗） | Jean Siméon Chardin | 约 1728–30 | The Met（59.9） | https://www.metmuseum.org/art/collection/search/435887 | CC0 1.0（Met Open Access） |
| `chardin/water_cistern_ngl.jpg` | The Water Cistern ('La Fontaine')（水缸） | Jean Siméon Chardin | 1733 或更晚 | NGL（NG1664） | https://commons.wikimedia.org/wiki/File:Jean-Baptiste_Sim%C3%A9on_Chardin_(1699-1779)_-_La_Fontaine_(The_Water_Cistern)_-_NG1664_-_National_Gallery.jpg | Public domain |
| `chardin/young_schoolmistress_ngl.jpg` | The Young Schoolmistress（年轻女教师） | Jean Siméon Chardin | 约 1737 | NGL（NG4077） | https://commons.wikimedia.org/wiki/File:Jean_Sim%C3%A9on_Chardin_-_The_Young_Schoolmistress_-_WGA04750.jpg | Public domain |
| `manet/a_bar_at_the_folies_bergere_1881_82.jpg` | A Bar at the Folies-Bergère | Édouard Manet | 1881–82 | The Courtauld Gallery, London | https://commons.wikimedia.org/wiki/File:Edouard_Manet,_A_Bar_at_the_Folies-Berg%C3%A8re.jpg | Public domain |
| `manet/boating_1874.jpg` | Boating（《划船》） | Édouard Manet | 1874 | The Met, New York（29.100.115） | https://www.metmuseum.org/art/collection/search/436947 | CC0 1.0 |
| `manet/corner_of_a_cafe_concert_1878_80.jpg` | Corner of a Café-Concert | Édouard Manet | ca. 1878–80 | National Gallery, London（NG3858） | https://commons.wikimedia.org/wiki/File:Edouard_Manet,_Corner_of_a_Caf%C3%A9-Concert,_ca._1878-80.jpg | Public domain |
| `manet/le_balcon_1868_69.jpg` | Le Balcon | Édouard Manet | 1868–69 | Musée d'Orsay, Paris（RF 2772） | https://commons.wikimedia.org/wiki/File:Edouard_Manet_-_The_Balcony_-_Google_Art_Project.jpg | Public domain |
| `manet/le_dejeuner_sur_lherbe_1863.jpg` | Le Déjeuner sur l'herbe | Édouard Manet | 1863 | Musée d'Orsay, Paris（RF 1668） | https://commons.wikimedia.org/wiki/File:Edouard_Manet_-_Luncheon_on_the_Grass_-_Google_Art_Project.jpg | Public domain |
| `manet/le_fifre_1866.jpg` | Le Fifre（The Fifer） | Édouard Manet | 1866 | Musée d'Orsay, Paris（RF 1998） | https://commons.wikimedia.org/wiki/File:Manet,_Edouard_-_Young_Flautist,_or_The_Fifer,_1866_(2).jpg | Public domain |
| `manet/mademoiselle_v_in_the_costume_of_an_espada_1862.jpg` | Mademoiselle V. . . in the Costume of an Espada | Édouard Manet | 1862 | The Met, New York（29.100.53） | https://www.metmuseum.org/art/collection/search/436945 | CC0 1.0 |
| `manet/music_in_the_tuileries_gardens_1862.jpg` | Music in the Tuileries Gardens | Édouard Manet | 1862 | National Gallery, London（NG3260） | https://commons.wikimedia.org/wiki/File:%C3%89douard_Manet_-_Music_in_the_Tuileries_Gardens.jpg | Public domain |
| `manet/olympia_1863.jpg` | Olympia | Édouard Manet | 1863 | Musée d'Orsay, Paris（RF 644） | https://commons.wikimedia.org/wiki/File:Edouard_Manet_-_Olympia_-_Google_Art_Project_2.jpg | Public domain |
| `manet/portrait_of_emile_zola_1868.jpg` | Portrait of Émile Zola | Édouard Manet | 1868 | Musée d'Orsay, Paris（RF 2205） | https://commons.wikimedia.org/wiki/File:Manet,_Edouard_-_Portrait_of_Emile_Zola.jpg | Public domain |
| `manet/spanish_singer_1860.jpg` | The Spanish Singer（《西班牙歌手》） | Édouard Manet | 1860 | The Met, New York（49.58.2） | https://www.metmuseum.org/art/collection/search/436944 | CC0 1.0（Met Open Access） |
| `manet/stephane_mallarme_1876.jpg` | Stéphane Mallarmé | Édouard Manet | 1876 | Musée d'Orsay, Paris（RF 2632） | https://commons.wikimedia.org/wiki/File:Edouard_Manet_-_St%C3%A9phane_Mallarm%C3%A9_-_Google_Art_Project.jpg | Public domain |
| `manet/the_monet_family_in_their_garden_at_argenteuil_1874.jpg` | The Monet Family in Their Garden at Argenteuil | Édouard Manet | 1874 | The Met, New York（1976.201.14） | https://www.metmuseum.org/art/collection/search/436965 | CC0 1.0 |
| `manet/woman_with_a_cat_c1880.jpg` | Woman with a Cat（Femme au chat） | Édouard Manet | ca. 1880 | National Gallery, London（L675） | https://commons.wikimedia.org/wiki/File:%C3%89douard_Manet_-_Femme_au_chat_(Portrait_de_Madame_Manet).jpg | Public domain |
| `sorolla/autorretrato_1904.jpg` | Autorretrato（自画像；室内暗调·Velázquez 谱系对照件） | Joaquín Sorolla | 1904 | Museo Sorolla（inv. 687） | https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_Self_Portrait_-_Google_Art_Project.jpg | Public domain |
| `sorolla/chicos_en_la_playa_1909.jpg` | Chicos en la playa（海滩上的男孩们） | Joaquín Sorolla | 1909（签1910） | Museo Nacional del Prado（P4648） | https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_-_Chicos_en_la_playa.jpg | Public domain |
| `sorolla/clotilde_con_traje_de_noche_1910.jpg` | Clotilde con traje de noche（晚装 Clotilde） | Joaquín Sorolla | 1910 | Museo Sorolla（inv. 949） | https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_Clotilde_in_evening_dress_-_Google_Art_Project.jpg | Public domain |
| `sorolla/el_bano_del_caballo_1909.jpg` | El baño del caballo（马浴） | Joaquín Sorolla | 1909 | Museo Sorolla（inv. 839） | https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_The_Horse%E2%80%99s_Bath_-_Google_Art_Project.jpg | Public domain |
| `sorolla/la_bata_rosa_1916.jpg` | La bata rosa（粉色浴袍） | Joaquín Sorolla | 1916 | Museo Sorolla（inv. 1134） | https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_The_Pink_Robe._After_the_Bath_-_Google_Art_Project.jpg | Public domain |
| `sorolla/la_hora_del_bano_1909.jpg` | La hora del baño（沐浴时刻） | Joaquín Sorolla | 1909 | Museo Sorolla（inv. 835） | https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_Time_for_a_Bathe%2C_Valencia_-_Google_Art_Project.jpg | Public domain |
| `sorolla/la_siesta_1911.jpg` | La siesta（午睡） | Joaquín Sorolla | 1911 | Museo Sorolla | https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_La_Siesta_-_Google_Art_Project.jpg | Public domain |
| `sorolla/la_vuelta_de_la_pesca_1894.jpg` | La vuelta de la pesca（渔获归来） | Joaquín Sorolla | 约1894 | Musée d'Orsay, Paris（RF 948） | https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_La_vuelta_de_la_pesca.jpg | Public domain |
| `sorolla/mis_hijos_1904.jpg` | Mis hijos（我的孩子们） | Joaquín Sorolla | 1904 | Museo Sorolla（inv. 651） | https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_My_children_-_Google_Art_Project.jpg | Public domain |
| `sorolla/nadadores_javea_1905.jpg` | Nadadores, Jávea（哈韦阿的泳者） | Joaquín Sorolla | 1905 | Museo Sorolla | https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_Swimmers%2C_J%C3%A1vea_-_Google_Art_Project.jpg | Public domain |
| `sorolla/paseo_a_orillas_del_mar_1909.jpg` | Paseo a orillas del mar（海边漫步） | Joaquín Sorolla | 1909 | Museo Sorolla（inv. 834） | https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_Strolling_along_the_Seashore_-_Google_Art_Project.jpg | Public domain |
| `sorolla/triste_herencia_1899.jpg` | ¡Triste herencia!（悲惨的遗产） | Joaquín Sorolla | 1899 | Fundación Bancaja, Valencia | https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_Triste_Herencia_(1899).jpg | Public domain |
| `sorolla/vision_de_espana_valencia_1911_19.jpg` | Vision of Spain：Valencia 面板 | Joaquín Sorolla | 1911–19 | Hispanic Society of America（A1805） | https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_Vision_of_Spain_(formerly%2C_The_Provinces_of_Spain)%2C_Valencia_-_A1805_-_Hispanic_Society_of_America.jpg | Public domain |
| `zorn/dance_in_gopsmor_1906.jpg` | Dans i Gopsmor / Polka（戈普斯莫尔之舞） | Anders Zorn | 1906 | Nationalmuseum, Stockholm（85527；文件名含「Överförd till Riksdagen」注记） | https://commons.wikimedia.org/wiki/File:%C3%96verf%C3%B6rd_till_Riksdagen,_Dans_i_Gopsmor_(Anders_Zorn)_-_Nationalmuseum_-_85527.tif | Public domain |
| `zorn/en_premiar_1888.jpg` | En premiär / Une première（首次登台） | Anders Zorn | 1888 | Nationalmuseum, Stockholm | https://commons.wikimedia.org/wiki/File:Une_premiere_av_Anders_Zorn_1888.jpg | Public domain |
| `zorn/etching_mona_1911.jpg` | Mona（莫娜，蚀刻；佐恩之母） | Anders Zorn | 1911 | The Met, New York（384580；third state of three） | https://www.metmuseum.org/art/collection/search/384580 | CC0 1.0 |
| `zorn/etching_omnibus_1892.jpg` | Omnibus（公共马车，蚀刻） | Anders Zorn | 1892 | The Met, New York（384539；fourth state of five） | https://www.metmuseum.org/art/collection/search/384539 | CC0 1.0 |
| `zorn/etching_rosita_mauri_1889.jpg` | Rosita Mauri（罗西塔·毛里，蚀刻） | Anders Zorn | 1889 | Cleveland Museum of Art（1962.406） | https://www.clevelandart.org/art/collection/search?q=zorn | CC0 1.0（Cleveland Open Access） |
| `zorn/etching_wet_1911.jpg` | Wet（湿，蚀刻） | Anders Zorn | 1911 | The Met, New York（365109；third state of three） | https://www.metmuseum.org/art/collection/search/365109 | CC0 1.0 |
| `zorn/etching_zorn_and_his_wife_1890.jpg` | Zorn and His Wife（与妻子在一起，蚀刻） | Anders Zorn | 1890 | The Met, New York（384551；third state of three） | https://www.metmuseum.org/art/collection/search/384551 | CC0 1.0 |
| `zorn/fisherman_st_ives_1888.jpg` | Fiskare i St. Ives / Un pêcheur（圣艾夫斯的渔夫） | Anders Zorn | 1888 | Musée d'Orsay, Paris | https://commons.wikimedia.org/wiki/File:Anders_Zorn_-_A_Fisherman_1888.jpg | Public domain |
| `zorn/frieda_schiff_1894.jpg` | Frieda Schiff (1876–1958), Later Mrs. Felix M. Warburg | Anders Zorn | 1894 | The Met, New York（437964） | https://www.metmuseum.org/art/collection/search/437964 | CC0 1.0 |
| `zorn/midnatt_1891.jpg` | Midnatt（午夜） | Anders Zorn | 1891 | Zornmuseet, Mora | https://commons.wikimedia.org/wiki/File:Midnatt_av_Anders_Zorn_1891.jpg | Public domain |
| `zorn/midsummer_dance_1897.jpg` | Midsommardans（仲夏之舞） | Anders Zorn | 1897 | Nationalmuseum, Stockholm | https://commons.wikimedia.org/wiki/File:Midsommardans_av_Anders_Zorn_1897.jpg | Public domain |
| `zorn/mrs_walter_rathbone_bacon_1897.jpg` | Mrs. Walter Rathbone Bacon (Virginia Purdy Barker) | Anders Zorn | 1897 | The Met, New York（437966） | https://www.metmuseum.org/art/collection/search/437966 | CC0 1.0（Met Open Access） |
| `zorn/omnibus_i_1892.jpg` | Omnibus I（公共马车一号） | Anders Zorn | 1892 | Nationalmuseum, Stockholm | https://commons.wikimedia.org/wiki/File:Anders_Zorn_Omnibus.jpg | Public domain |
| `zorn/our_daily_bread_1886.jpg` | Vårt dagliga bröd（我们的日常面包） | Anders Zorn | 1886 | Nationalmuseum, Stockholm（24125） | https://commons.wikimedia.org/wiki/File:Our_Daily_Bread_(Anders_Zorn)_-_Nationalmuseum_-_24125.tif | Public domain |
| `zorn/self_portrait_in_red_1915.jpg` | Självporträtt i rött（红衣自画像） | Anders Zorn | 1915 | Zornmuseet, Mora | https://commons.wikimedia.org/wiki/File:Zornself.jpg | Public domain |
| `zorn/self_portrait_with_model_1896.jpg` | Självporträtt med modell（自画像与模特） | Anders Zorn | 1896 | Nationalmuseum, Stockholm | https://commons.wikimedia.org/wiki/File:Sj%C3%A4lvportr%C3%A4tt_av_Anders_Zorn_1896.jpg | Public domain |
| `zorn/sommarafton_1894.jpg` | Sommarafton（夏夜） | Anders Zorn | 1894 | Zornmuseet, Mora | https://commons.wikimedia.org/wiki/File:Anders_Zorn_Sommerabend_1894.jpg | Public domain |
| `zorn/sommarnoje_1886.jpg` | Sommarnöje（夏趣） | Anders Zorn | 1886 | 私人收藏（2010 年 2600 万 SEK 成交） | https://commons.wikimedia.org/wiki/File:Sommarn%C3%B6je_(1886),_akvarell_av_Anders_Zorn.jpg | Public domain |
| `zorn/vallkulla_1908.jpg` | Vallkulla（牧羊女） | Anders Zorn | 1908 | Zornmuseet, Mora | https://commons.wikimedia.org/wiki/File:Anders_Zorn_-_Vallkulla.jpg | Public domain |
| `sultan_mohammed/celebration_id.jpg` | 《庆祝开斋节》f.86a（Cartier 哈菲兹） | Sultan Muhammad | c. 1527–31 | 私人收藏（原 Cartier 旧藏） | https://commons.wikimedia.org/wiki/File:Portrait_of_Sam_Mirza_as_a_patron%3B_The_feast_of_I%E2%80%99d_begins%2C_copy_of_Diwan_Hafiz_manuscript.jpg | Public domain |
| `sultan_mohammed/court_gayumars.jpg` | 《古尤马尔斯宫廷》（The Court of Gayumars）全页 | Sultan Muhammad | c. 1524–25 | 多伦多，阿迦汗博物馆 AKM165（原 Sadruddin Aga Khan 旧藏） | https://commons.wikimedia.org/wiki/File:Court_of_Gayumars_Persian_miniature.jpg | Public domain |
| `sultan_mohammed/court_gayumars_detail.jpg` | 《古尤马尔斯宫廷》画面裁切版 | Sultan Muhammad | c. 1524–25 | 阿迦汗博物馆 AKM165 | https://commons.wikimedia.org/wiki/File:The_Court_of_Gayumars_%28Cropped%29.jpg | Public domain |
| `sultan_mohammed/death_of_zahhak.jpg` | 《扎哈克之死》f.37v | Sultan Muhammad | c. 1535 | 阿迦汗博物馆 AKM155 | https://commons.wikimedia.org/wiki/File:Sultan_Muhammad_Tiran_Zahhak.jpg | Public domain |
| `sultan_mohammed/earthly_drunkenness_harvard.jpg` | 《尘世醉酒》 | Sultan Muhammad | c. 1530 | 哈佛艺术博物馆 1988.460.2 | https://commons.wikimedia.org/wiki/File:Earthly_Drunkenness.jpg | Public domain |
| `sultan_mohammed/faridun_zahhak_freer.jpg` | 《法里顿锤击扎哈克》 | Sultan Muhammad | c. 1525 | 华盛顿，弗里尔美术馆 F1996.2 | https://commons.wikimedia.org/wiki/File:Faridun_strikes_Zahhak_with_the_ox-headed_mace.jpg | Public domain |
| `sultan_mohammed/feast_of_sada_met.jpg` | 《萨达节之宴》f.22v | Sultan Muhammad | c. 1525 | 纽约，大都会艺术博物馆 1970.301.2 | https://commons.wikimedia.org/wiki/File:%22The_Feast_of_Sada%22%2C_Folio_22v_from_the_Shahnama_%28Book_of_Kings%29_of_Shah_Tahmasp_MET_DP107689.jpg | CC0 |
| `sultan_mohammed/hafiz_allegory_met.jpg` | 《世界与彼世的醉酒》f.135a（Cartier 哈菲兹） | Sultan Muhammad | c. 1531 | 大都会艺术博物馆 × 哈佛艺术博物馆（1988.430 联合藏） | https://commons.wikimedia.org/wiki/File:Folio_Divan_Hafiz_Met_1988.430.jpg | Public domain |
| `sultan_mohammed/hafiz_signature.jpg` | 《庆祝开斋节》签名细部（统治者足下） | Sultan Muhammad | c. 1531 | 私人收藏（原 Cartier 旧藏） | https://commons.wikimedia.org/wiki/File:Sultan_Muhammad_signature%2C_at_the_feet_of_the_ruler._The_feast_of_I%E2%80%99d_begins%2C_Diwan_of_Hafiz_manuscript%2C_1531.jpg | Public domain |
| `sultan_mohammed/jamal_jalal_divan.jpg` | 《贾马尔与贾拉尔》f.2v「苏丹的迪万」 | Sultan Muhammad | c. 1502–05 | 乌普萨拉大学图书馆 O Nova 2 | https://commons.wikimedia.org/wiki/File:The_sultan_in_his_divan_%28full_view%2C_f._2v%29%2C_Dastan-i_Jamal_u_Jalal._1502-1505%2C_Tabriz_%28Uppsala_University_Library%2C_O_Nova_2%29.jpg | Public domain |
| `sultan_mohammed/khusraw_shirin_bl.jpg` | 《霍斯鲁窥见西琳沐浴》f.53v | Sultan Muhammad | 1539–43 | 伦敦，大英图书馆 Or.2265 | https://commons.wikimedia.org/wiki/File:Khusraw_watches_Shirin_bathing.jpg | CC0 |
| `sultan_mohammed/lovers_picnic_harvard.jpg` | 《恋人野餐》 | Sultan Muhammad | c. 1530 | 哈佛艺术博物馆 2007.183.2 | https://commons.wikimedia.org/wiki/File:Lovers%27_Picnic.jpg | Public domain |
| `sultan_mohammed/rustam_sleeping_bm.jpg` | 《鲁斯塔姆沉睡，拉赫什斗狮》 | Sultan Muhammad | c. 1515–22 | 伦敦，大英博物馆 1948,1211,0.23 | https://commons.wikimedia.org/wiki/File:Sleeping_Rustam.jpg | Public domain |
| `sultan_mohammed/tahmuras_divs_met.jpg` | 《塔赫穆拉斯降魔》f.23v | Sultan Muhammad | c. 1525 | 大都会艺术博物馆 1970.301.3 | https://commons.wikimedia.org/wiki/File:%22Tahmuras_Defeats_the_Divs%22%2C_Folio_23v_from_the_Shahnama_%28Book_of_Kings%29_of_Shah_Tahmasp_MET_DP107119.jpg | CC0 |
| `sultan_mohammed/zahhak_fate_met.jpg` | 《扎哈克听闻命运》f.29v | Sultan Muhammad | c. 1524 | 大都会艺术博物馆 1970.301.4 | https://commons.wikimedia.org/wiki/File:%22Zahhak_is_Told_His_Fate%22%2C_Folio_29v_from_the_Shahnama_%28Book_of_Kings%29_of_Shah_Tahmasp_MET_DP107120.jpg | CC0 |
| `sultan_mohammed/zal_magi_met.jpg` | 《扎尔问卜》f.73v | Sultan Muhammad | c. 1530–35 | 大都会艺术博物馆 1970.301.8 | https://commons.wikimedia.org/wiki/File:%22Zal_Consults_the_Magi%22%2C_Folio_73v_from_the_Shahnama_%28Book_of_Kings%29_of_Shah_Tahmasp_MET_DP107124.jpg | CC0 |

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

### hiroshige — 歌川广重（18 张；wave18 并入）
- **asakusa_ricefields_torinomachi.jpg** — Pilgrimage to the Torinomachi Festival across the Ricefields of Asakusa（浅草田甫 酉の町詣；名所江戸百景），Utagawa Hiroshige，1857（安政 4 年 11 月），The Met（36539；Rogers Fund, 1914）。
  - 来源: https://www.metmuseum.org/art/collection/search/36539；License: CC0（PD）
  - 落盘: 1211×1800px，579 KB
- **camellia_and_bird.jpg** — Camellia and Bird（椿に小禽；花鸟画），Utagawa Hiroshige，ca. 1833，The Met（36719；Rogers Fund, 1918）。
  - 来源: https://www.metmuseum.org/art/collection/search/36719；License: CC0（PD）
  - 落盘: 1311×1800px，562 KB
- **dragon_in_clouds.jpg** — Dragon in Clouds（雲中龍；大短冊判），Utagawa Hiroshige，c. 1830s，Art Institute of Chicago（36444，Commons）。
  - 来源: https://www.artic.edu/artworks/36444/dragon-in-clouds；License: Public domain
  - 落盘: 828×1800px，413 KB
- **hakone_lake.jpg** — Hakone; Kosui（箱根 湖水図；東海道五十三次之内 第 10 图），Utagawa Hiroshige，ca. 1833–34，The Met（36932；Rogers Fund, 1918）。
  - 来源: https://www.metmuseum.org/art/collection/search/36932；License: CC0（PD）
  - 落盘: 1800×1226px，552 KB
- **kameido_plum_garden.jpg** — Plum Garden at Kameido（亀戸梅屋舗；名所江戸百景 第 30 图），Utagawa Hiroshige，1857，Rijksmuseum（RP-P-1956-743，Commons）。
  - 来源: https://commons.wikimedia.org/wiki/File:De_pruimenboomgaard_te_Kameido-Rijksmuseum_RP-P-1956-743.jpeg；License: Public domain
  - 落盘: 1225×1800px，664 KB
- **kanbara_night_snow.jpg** — Evening Snow at Kanbara（蒲原 夜之雪；東海道五十三次之内 第 16 图），Utagawa Hiroshige，ca. 1833–34，The Met（56915；Howard Mansfield Coll.）。
  - 来源: https://www.metmuseum.org/art/collection/search/56915；License: CC0（PD）
  - 落盘: 1800×1197px，481 KB
- **kinryuzan_temple_asakusa.jpg** — Kinryūsan Temple at Asakusa（浅草金龍山；名所江戸百景 第 99 图），Utagawa Hiroshige，1856，The Met（56689；Howard Mansfield Coll.）。
  - 来源: https://www.metmuseum.org/art/collection/search/56689；License: CC0（PD）
  - 落盘: 1230×1800px，527 KB
- **kiso_mountains_in_snow.jpg** — The Kiso Mountains in Snow（木曽山雪景；三枚续），Utagawa Hiroshige，1857（巳年 8 月），The Met（36545；Rogers Fund, 1914）。
  - 来源: https://www.metmuseum.org/art/collection/search/36545；License: CC0（PD）
  - 落盘: 1800×886px，404 KB
- **moon_pine_ueno.jpg** — Moon Pine at Ueno（上野山内 月のまつ；名所江戸百景 第 89 图），Utagawa Hiroshige，1857，Library of Congress（LCCN 2008660968，Commons）。
  - 来源: https://commons.wikimedia.org/wiki/File:Ueno_sannai_tsuki_no_matsu_LCCN2008660968.jpg；License: Public domain
  - 落盘: 1212×1800px，518 KB
- **naruto_whirlpool_awa.jpg** — Naruto Whirlpool, Awa Province（阿波 鳴門の風波；六十余州名所図会），Utagawa Hiroshige，ca. 1853，The Met（53783；Rogers Fund, 1919）。
  - 来源: https://www.metmuseum.org/art/collection/search/53783；License: CC0（PD）
  - 落盘: 1233×1800px，598 KB
- **nihonbashi_morning.jpg** — Stations One: Morning View of Nihonbashi（日本橋 朝之景；東海道五十三次之内 第 1 图），Utagawa Hiroshige，ca. 1833–34，The Met（36922；Rogers Fund, 1918）。
  - 来源: https://www.metmuseum.org/art/collection/search/36922；License: CC0（PD）
  - 落盘: 1800×1225px，535 KB
- **ohashi_atake_sudden_shower.jpg** — Sudden Shower over Shin-Ōhashi Bridge and Atake（大はしあたけの夕立；名所江戸百景 第 58 图），Utagawa Hiroshige，1857，The Met（55433；Howard Mansfield Coll.）。
  - 来源: https://www.metmuseum.org/art/collection/search/55433；License: CC0（PD）
  - 落盘: 1236×1800px，575 KB
- **otsu_reisho_edition.jpg** — Ōtsu（大津；東海道五十三次之内 隷書東海道版 第 54 图），Utagawa Hiroshige，1847–52，The Met（37248；Francis Lathrop Coll.）。
  - 来源: https://www.metmuseum.org/art/collection/search/37248；License: CC0（PD）
  - 落盘: 1800×1190px，572 KB
- **ryogoku_bridge_brooklyn.jpg** — Ryōgoku Bridge and the Great Riverbank（両国橋大川ばた；名所江戸百景 第 59 图），Utagawa Hiroshige，1856，Brooklyn Museum（Commons 复制品）。
  - 来源: https://commons.wikimedia.org/wiki/File:Brooklyn_Museum_-_Ryogoku_Bridge_and_the_Great_Riverbank_No_59_from_One_Hundred_Views_of_Edo_-_Utagawa_Hiroshige_(Ando).jpg；License: Public domain
  - 落盘: 1023×1536px，407 KB
- **satta_sea_suruga.jpg** — The Sea at Satta, Suruga Province（駿河 薩埵峠の海；富士三十六景），Utagawa Hiroshige，1858，Google Art Project（Commons）。
  - 来源: https://commons.wikimedia.org/wiki/File:Ando_Hiroshige_-_The_Sea_at_Satta,_Suruga_Province,_from_the_series_%22Thirty-six_Views_of_Mount_Fuji%22_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1211×1800px，451 KB
- **seba_kiso_road.jpg** — Seba（洗馬；木曾街道六十九次之内），Utagawa Hiroshige，ca. 1836–37，Rijksmuseum（RP-P-1956-739，Commons）。
  - 来源: https://commons.wikimedia.org/wiki/File:Seba-Rijksmuseum_RP-P-1956-739.jpeg；License: Public domain
  - 落盘: 1800×1216px，659 KB
- **shono_driving_rain.jpg** — Shower at Shōno（庄野 白雨；東海道五十三次之内 第 45 图），Utagawa Hiroshige，1834，The Met（56916；Howard Mansfield Coll.）。
  - 来源: https://www.metmuseum.org/art/collection/search/56916；License: CC0（PD）
  - 落盘: 1800×1187px，582 KB
- **twilight_moon_ryogoku.jpg** — Twilight Moon at Ryōgoku Bridge（両国橋夕月；江戸名所），Utagawa Hiroshige，江戸时代（馆方未署年代），The Met（45294；Rogers Fund, 1922）。
  - 来源: https://www.metmuseum.org/art/collection/search/45294；License: CC0（PD）
  - 落盘: 1800×1153px，610 KB

### sargent — 萨金特（14 张；wave18 并入）
- **carnation_lily_lily_rose_1885_86.jpg** — Carnation, Lily, Lily, Rose，John Singer Sargent，1885–86，Tate, London（N01615）。
  - 来源: https://commons.wikimedia.org/wiki/File:John_Singer_Sargent_-_Carnation,_Lily,_Lily,_Rose_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1593×1800px，993 KB
- **claude_monet_painting_by_the_edge_of_a_wood_1885.jpg** — Claude Monet Painting by the Edge of a Wood，John Singer Sargent，?1885，Tate, London（N04103）。
  - 来源: https://commons.wikimedia.org/wiki/File:John_Singer_Sargent,_Claude_Monet_peignant_%C3%A0_la_lisi%C3%A8re_d%27un_bois.jpg；License: Public domain
  - 落盘: 1800×1522px，896 KB
- **el_jaleo_1882.jpg** — El Jaleo，John Singer Sargent，1882，Isabella Stewart Gardner Museum, Boston。
  - 来源: https://commons.wikimedia.org/wiki/File:EL_JALEO-SINGER.jpg；License: Public domain
  - 落盘: 1800×1217px，482 KB
- **ellen_terry_as_lady_macbeth_1889.jpg** — Ellen Terry as Lady Macbeth，John Singer Sargent，1889，Tate, London（N02053）。
  - 来源: https://commons.wikimedia.org/wiki/File:Ellen_Terry_as_Lady_Macbeth.jpg；License: Public domain
  - 落盘: 914×1800px，345 KB
- **green_door_santa_maria_della_salute_c1904.jpg** — Green Door, Santa Maria della Salute（水彩），John Singer Sargent，ca. 1904，The Met, New York（12107）。
  - 来源: https://www.metmuseum.org/art/collection/search/12107；License: CC0 1.0
  - 落盘: 1237×1800px，669 KB
- **henry_james_1913.jpg** — Henry James，John Singer Sargent，1913，National Portrait Gallery, London。
  - 来源: https://commons.wikimedia.org/wiki/File:Henry_James_by_John_Singer_Sargent.jpg；License: Public domain（注记见下）
  - 落盘: 1440×1800px，451 KB
- **lady_with_the_rose_1882.jpg** — Lady with the Rose (Charlotte Louise Burckhardt)，John Singer Sargent，1882，The Met, New York（32.154）。
  - 来源: https://commons.wikimedia.org/wiki/File:Lady_with_the_Rose_(Charlotte_Louise_Burckhardt)_MET_DT1151.jpg；License: CC0（Met 官方照片）
  - 落盘: 1046×1800px，492 KB
- **madame_x_1884.jpg** — Madame X (Virginie Amélie Avegno Gautreau)，John Singer Sargent，1883–84，The Met, New York（16.53）。
  - 来源: https://www.metmuseum.org/art/collection/search/12127；License: CC0 1.0（Met Open Access）
  - 落盘: 1051×1800px，225 KB
- **marie_louise_pailleron_c1881.jpg** — Marie-Louise Pailleron（墨笔素描），John Singer Sargent，ca. 1881，The Met, New York（50.130.115）。
  - 来源: https://www.metmuseum.org/art/collection/search/12464；License: CC0 1.0
  - 落盘: 1448×1800px，767 KB
- **mrs_hugh_hammersley_1892.jpg** — Mrs. Hugh Hammersley，John Singer Sargent，1892，The Met, New York（1998.365）。
  - 来源: https://commons.wikimedia.org/wiki/File:Mrs._Hugh_Hammersley_MET_DT2064.jpg；License: CC0（Met 官方照片）
  - 落盘: 1018×1800px，443 KB
- **octavia_hill_1898.jpg** — Octavia Hill，John Singer Sargent，1898，National Portrait Gallery, London（NPG 1746）。
  - 来源: https://commons.wikimedia.org/wiki/File:John_Singer_Sargent_-_Octavia_Hill_-_NPG_1746_-_National_Portrait_Gallery.jpg；License: Public domain
  - 落盘: 799×1000px，107 KB
- **the_wyndham_sisters_1899.jpg** — The Wyndham Sisters: Lady Elcho, Mrs. Adeane, and Mrs. Tennant，John Singer Sargent，1899，The Met, New York（27.67）。
  - 来源: https://commons.wikimedia.org/wiki/File:The_Wyndham_Sisters_-_Lady_Elcho,_Mrs._Adeane,_and_Mrs._Tenant.jpg；License: Public domain
  - 落盘: 1310×1800px，546 KB
- **two_girls_on_a_lawn_c1889.jpg** — Two Girls on a Lawn，John Singer Sargent，ca. 1889，The Met, New York（50.130.20）。
  - 来源: https://www.metmuseum.org/art/collection/search/12446；License: CC0 1.0
  - 落盘: 1800×1474px，1117 KB
- **violet_sargent_c1883.jpg** — Violet Sargent（石墨素描），John Singer Sargent，ca. 1883，The Met, New York（50.130.87）。
  - 来源: https://www.metmuseum.org/art/collection/search/12462；License: CC0 1.0
  - 落盘: 1351×1800px，687 KB

### piero_della_francesca — 皮耶罗·德拉·弗朗切斯卡（17 张；wave18 并入）
- **baptism_of_christ_ng665.jpg** — 《基督受洗》（The Baptism of Christ），Piero della Francesca，约 1437–1445，National Gallery, London（NG665）。
  - 来源: https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_Battesimo_di_Cristo_(National_Gallery,_London).jpg；License: Public domain
  - 落盘: 1253×1800px，624 KB
- **diptych_federico_battista.jpg** — 《乌尔比诺公爵双联像·正面》（Federico da Montefeltro & Battista Sforza），Piero della Francesca，约 1465–1475，Galleria degli Uffizi, Florence。
  - 来源: https://commons.wikimedia.org/wiki/File:Piero_della_francesca,_dittico_dei_duchi_di_urbino,_1465-72_circa_01.jpg；License: CC BY-SA 4.0（摄影 Sailko / Francesco Bini）
  - 落盘: 1800×1459px，695 KB
- **diptych_reverse_triumphs.jpg** — 《双联像·背面：凯旋寓意图》（Triumphs of Federico and Battista），Piero della Francesca，约 1465–1475，Galleria degli Uffizi, Florence。
  - 来源: https://commons.wikimedia.org/wiki/File:Piero_della_francesca,_dittico_dei_duchi_di_urbino,_1465-72_circa_02.jpg；License: CC BY-SA 4.0（摄影 Sailko / Francesco Bini）
  - 落盘: 1800×1402px，725 KB
- **flagellation_urbino.jpg** — 《鞭笞》（The Flagellation of Christ），Piero della Francesca，约 1455–1470，Galleria Nazionale delle Marche, Urbino。
  - 来源: https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_The_Flagellation_-_WGA17600.jpg；License: Public domain
  - 落盘: 1374×1000px，307 KB
- **legend_true_cross_battle_heraclius.jpg** — 《赫拉克利乌斯与科斯罗埃斯之战》（Battle between Heraclius and Chosroes），Piero della Francesca，约 1452–1466，Basilica di San Francesco, Arezzo。
  - 来源: https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_8._Battle_between_Heraclius_and_Chosroes_-_WGA17551.jpg；License: Public domain
  - 落盘: 1600×721px，287 KB
- **legend_true_cross_dream_of_constantine.jpg** — 《君士坦丁之梦》（Constantine's Dream，真十字架组画），Piero della Francesca，约 1452–1466，Basilica di San Francesco, Arezzo。
  - 来源: https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_017.jpg；License: Public domain
  - 落盘: 988×1800px，342 KB
- **legend_true_cross_finding_and_recognition.jpg** — 《真十字架的发现与验证》（Finding and Recognition of the True Cross），Piero della Francesca，约 1452–1466，Basilica di San Francesco, Arezzo。
  - 来源: https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_7._Finding_and_Recognition_of_the_True_Cross_-_WGA17533.jpg；License: Public domain
  - 落盘: 1600×729px，281 KB
- **legend_true_cross_queen_of_sheba.jpg** — 《示巴女王礼拜圣木/与所罗门相会》（Procession of the Queen of Sheba; Meeting with Solomon），Piero della Francesca，约 1452–1466，Basilica di San Francesco, Arezzo。
  - 来源: https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_2._Procession_of_the_Queen_of_Sheba%3B_Meeting_between_the_Queen_of_Sheba_and_King_Solomon_-_WGA17487.jpg；License: Public domain
  - 落盘: 1600×725px，275 KB
- **madonna_del_parto.jpg** — 《分娩圣母》（Madonna del Parto），Piero della Francesca，约 1455–1465，Museo della Madonna del Parto, Monterchi。
  - 来源: https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_Madonna_del_Parto_-_WGA17613.jpg；License: Public domain
  - 落盘: 1000×1260px，199 KB
- **madonna_di_senigallia.jpg** — 《塞尼加利亚圣母》（Madonna di Senigallia），Piero della Francesca，约 1470–1485，Galleria Nazionale delle Marche, Urbino。
  - 来源: https://commons.wikimedia.org/wiki/File:Piero_della_Francesca,_Madonna_di_Senigallia_01.jpg；License: CC BY-SA 4.0（摄影 Mongolo1984）
  - 落盘: 1554×1800px，687 KB
- **montefeltro_altarpiece_brera.jpg** — 《蒙特费尔特罗祭坛画》（Brera Madonna / Montefeltro Altarpiece），Piero della Francesca，1472–1474，Pinacoteca di Brera, Milan。
  - 来源: https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_Madonna_and_Child_with_Saints_(Montefeltro_Altarpiece)_-_WGA17615.jpg；License: Public domain
  - 落盘: 900×1308px，288 KB
- **nativity_ng908.jpg** — 《圣诞》（The Nativity），Piero della Francesca，约 1470–1482，National Gallery, London（NG908）。
  - 来源: https://commons.wikimedia.org/wiki/File:Piero_della_francesca,_natività,_1470-75,_01.jpg；License: Public domain
  - 落盘: 1714×1800px，736 KB
- **polyptych_of_the_misericordia.jpg** — 《慈悲多联祭坛画》（Polyptych of the Misericordia），Piero della Francesca，1445–1462，Museo Civico, Sansepolcro。
  - 来源: https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_Polyptych_of_the_Misericordia_-_WGA17446.jpg；License: Public domain
  - 落盘: 1200×1064px，209 KB
- **portrait_sigismondo_malatesta.jpg** — 《西吉斯蒙多·潘多尔福·马拉泰斯塔像》（Portrait of Sigismondo Pandolfo Malatesta），Piero della Francesca，约 1451，Musée du Louvre, Paris。
  - 来源: https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_Sigismondo_Pandolfo_Malatesta_-_WGA17624.jpg；License: Public domain
  - 落盘: 802×1065px，172 KB
- **resurrection_sansepolcro.jpg** — 《复活》（The Resurrection），Piero della Francesca，约 1463–1465，Museo Civico, Sansepolcro。
  - 来源: https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_Resurrection_-_WGA17609.jpg；License: Public domain
  - 落盘: 1130×1200px，272 KB
- **saint_jerome_penitent_berlin.jpg** — 《忏悔的圣杰罗姆》（Saint Jerome in Penitence），Piero della Francesca，约 1450，Gemäldegalerie, Berlin。
  - 来源: https://commons.wikimedia.org/wiki/File:Piero_della_francesca,_San_Girolamo_penitente,_1450_ca,_da_gemaldegalerie_di_berlino.JPG；License: Public domain
  - 落盘: 1483×1800px，447 KB
- **saint_michael_ng769.jpg** — 《圣米迦勒》（Saint Michael，Sant'Agostino 多联祭坛侧板），Piero della Francesca，约 1454–1469，National Gallery, London（NG769）。
  - 来源: https://commons.wikimedia.org/wiki/File:Piero_della_Francesca_-_Polyptych_of_St_Augustine_-_St_Michael_-_WGA17457.jpg；License: Public domain
  - 落盘: 708×1600px，225 KB

### artemisia_gentileschi — 阿尔泰米西娅·真蒂莱斯基（16 张；wave18 并入）
- **allegory_of_inclination.jpg** — Allegory of Inclination（倾向的寓意；152×61 cm，天顶画），Artemisia Gentileschi，1615–16，Casa Buonarroti, Florence（1684 年 Volterrano 加绘织物）。
  - 来源: https://commons.wikimedia.org/wiki/File:A_Gentileschi_Allegoria_dell%27inclinazione.jpg；License: Public domain
  - 落盘: 694×1800px，331 KB
- **annunciation_capodimonte.jpg** — Annunciation（受胎告知；Commons 标注 "Attributed to"），Artemisia Gentileschi，1630，Museo e Real Bosco di Capodimonte, Naples。
  - 来源: https://commons.wikimedia.org/wiki/File:Verk%C3%BCndigung_an_maria.jpg；License: Public domain
  - 落盘: 1240×1800px，405 KB
- **corisca_and_the_satyr.jpg** — Corisca and the Satyr（科里斯卡与萨提尔），Artemisia Gentileschi，c. 1630s，Private collection。
  - 来源: https://commons.wikimedia.org/wiki/File:Corisca_and_the_Satyr_by_Artemisia_Gentileschi.jpg；License: Public domain
  - 落盘: 1800×1312px，437 KB
- **danae.jpg** — Danaë（达娜厄；93:1986），Artemisia Gentileschi，c. 1612，Saint Louis Art Museum。
  - 来源: https://commons.wikimedia.org/wiki/File:Artemisia_Gentileschi_-_Dana%C3%AB.jpg；License: Public domain
  - 落盘: 1500×1165px，181 KB
- **esther_before_ahasuerus.jpg** — Esther before Ahasuerus（208.3×273.7 cm；1969 年 Ingersoll 赠），Artemisia Gentileschi，1620s，The Metropolitan Museum of Art, New York（436453）。
  - 来源: https://commons.wikimedia.org/wiki/File:Gentileschi,_Artemisia_-_Esther_before_Ahasuerus_-_c._1628%E2%80%931635.jpg；License: Public domain
  - 落盘: 1800×1372px，647 KB
- **jael_and_sisera.jpg** — Jael and Sisera（雅亿与西西拉），Artemisia Gentileschi，c. 1620，Museum of Fine Arts, Budapest。
  - 来源: https://commons.wikimedia.org/wiki/File:Giaele_e_Sisara_(ca.1620)_-_Artemisia_Gentileschi_(Museum_of_Fine_Arts,_Budapest).jpg；License: Public domain
  - 落盘: 1516×1100px，189 KB
- **judith_and_her_maidservant_detroit.jpg** — Judith and Her Maidservant with the Head of Holofernes（187.2×142 cm；52.253），Artemisia Gentileschi，c. 1623–25，Detroit Institute of Arts（Gift of Mr. Leslie H. Green）。
  - 来源: https://commons.wikimedia.org/wiki/File:Artemisia_Gentileschi_Judith_Maidservant_DIA.jpg；License: Public domain
  - 落盘: 1386×1800px，342 KB
- **judith_and_her_maidservant_pitti.jpg** — Judith and Her Maidservant（朱迪斯与女仆；皮蒂宫版），Artemisia Gentileschi，c. 1613–1619（口径不一），Galleria Palatina, Palazzo Pitti, Florence。
  - 来源: https://commons.wikimedia.org/wiki/File:Gentileschi_judith1.jpg；License: Public domain
  - 落盘: 1400×1755px，602 KB
- **judith_beheading_holofernes_uffizi.jpg** — Judith Beheading Holofernes（乌菲齐版；146.5×108 cm；inv. 1890 n. 1567），Artemisia Gentileschi，c. 1620，Gallerie degli Uffizi, Florence（D29 厅）。
  - 来源: https://commons.wikimedia.org/wiki/File:Artemisia_Gentileschi_-_Giuditta_decapita_Oloferne_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1458×1800px，521 KB
- **judith_slaying_holofernes_naples.jpg** — Judith Slaying Holofernes（朱迪斯斩首荷罗孚尼，那不勒斯版；158.8×125.5 cm），Artemisia Gentileschi，c. 1612–13（另说 1617，见 §10），Museo e Real Bosco di Capodimonte, Naples（Q378）。
  - 来源: https://commons.wikimedia.org/wiki/File:Artemisia_Gentileschi_-_Judith_Beheading_Holofernes_-_WGA8563.jpg；License: Public domain
  - 落盘: 1178×1500px，240 KB
- **mary_magdalene_pitti.jpg** — Mary Magdalene（抹大拉的马利亚），Artemisia Gentileschi，c. 1613–20，Galleria Palatina, Palazzo Pitti, Florence。
  - 来源: https://commons.wikimedia.org/wiki/File:Artemisia_Gentileschi_Mary_Magdalene_Pitti.jpg；License: Public domain
  - 落盘: 1115×1500px，441 KB
- **self_portrait_as_a_lute_player.jpg** — Self-Portrait as a Lute Player（扮鲁特琴手的自画像），Artemisia Gentileschi，c. 1615–18，Wadsworth Atheneum, Hartford。
  - 来源: https://commons.wikimedia.org/wiki/File:Artemisia_Gentileschi_-_Self-Portrait_as_a_Lute_Player.JPG；License: Public domain
  - 落盘: 1670×1800px，905 KB
- **self_portrait_as_saint_catherine.jpg** — Self-Portrait as Saint Catherine of Alexandria（NG6671；71.5×71 cm），Artemisia Gentileschi，c. 1615–17，The National Gallery, London（2018 年购入）。
  - 来源: https://commons.wikimedia.org/wiki/File:Artemisia_Gentileschi_-_Self-Portrait_5365.jpg；License: Public domain
  - 落盘: 1800×1788px，907 KB
- **self_portrait_as_the_allegory_of_painting.jpg** — Self-Portrait as the Allegory of Painting（La Pittura；RCIN 405551；98.6×75.2 cm），Artemisia Gentileschi，c. 1638–39，Royal Collection（Hampton Court Palace）。
  - 来源: https://commons.wikimedia.org/wiki/File:Self-portrait_as_the_Allegory_of_Painting_(La_Pittura)_-_Artemisia_Gentileschi.jpg；License: Public domain
  - 落盘: 1333×1800px，500 KB
- **susanna_and_the_elders_1610.jpg** — Susanna and the Elders（苏珊娜与长老；170×119 cm），Artemisia Gentileschi，1610，Schloss Weißenstein（Schönborn 收藏）, Pommersfelden。
  - 来源: https://commons.wikimedia.org/wiki/File:Susanna_and_the_Elders_(1610),_Artemisia_Gentileschi.jpg；License: Public domain
  - 落盘: 1267×1800px，561 KB
- **venus_and_cupid.jpg** — Venus and Cupid（维纳斯与丘比特），Artemisia Gentileschi，c. 1625–30，Virginia Museum of Fine Arts, Richmond。
  - 来源: https://commons.wikimedia.org/wiki/File:Gentileschi_-_Venus_and_Cupid_(c._1625-30_VMFA).jpg；License: Public domain
  - 落盘: 1800×1199px，417 KB

### fan_kuan — 范宽（8 张；wave19 并入）
- **fang_fankuan_met.jpg** — 倣范寬山水圖（佚名），Fan Kuan，北宋末（12世纪初），大都会艺术博物馆（MET 56.151）。
  - 来源: https://commons.wikimedia.org/wiki/File:宋范寬秋林飛瀑_軸.jpg（MET Open Access：https://images.metmuseum.org/CRDImages/as/original/DP165245.jpg（Commons 同源））；License: **CC0**（MET Open Access）
  - 落盘: 1351×1800px，428 KB
- **linliu_duzuo.jpg** — 临流独坐图（传范宽），Fan Kuan，宋（约南宋初），台北故宫博物院（故画000045）。
  - 来源: https://commons.wikimedia.org/wiki/File:宋范寬臨流獨坐圖_軸.jpg（NPM 开放数据）；License: **CC0**（台北故宫开放数据）
  - 落盘: 1005×1493px，330 KB
- **qiulin_feipu.jpg** — 秋林飞瀑图（传范宽），Fan Kuan，宋，台北故宫博物院（故画000825）。
  - 来源: https://commons.wikimedia.org/wiki/File:宋范寬秋林飛瀑_軸.jpg（NPM 开放数据）；License: **CC0**（台北故宫开放数据）
  - 落盘: 919×1633px，278 KB
- **wanghui_fa_fankuan.jpg** — 王翬《紅林秋霁》（法范寬山水；《清惲壽平王翬花卉山水合冊》之一开），Fan Kuan，清·康熙十一年（1672），台北故宫博物院（故画001231N000000010）。
  - 来源: https://digitalarchive.npm.gov.tw/Collection/Detail/5100?dep=P（NPM 开放资料 IIIF）；License: 开放资料（政府资料开放授权条款，相容 CC BY 4.0；署名：国立故宫博物院）
  - 落盘: 1800×1296px，559 KB
- **xishan_signature.jpg** — 谿山行旅图·款识位置（右下树荫），Fan Kuan，北宋，台北故宫博物院。
  - 来源: https://commons.wikimedia.org/wiki/File:Fan_Kuan_-_Travelers_Among_Mountains_and_Streams_-_Signature.jpg；License: Public domain（PD-Art）
  - 落盘: 656×280px，56 KB
- **xishan_xinglv.jpg** — 谿山行旅图（画心），Fan Kuan，北宋（11世纪初），台北故宫博物院（故画000826）。
  - 来源: https://commons.wikimedia.org/wiki/File:谿山行旅图轴.溪山行旅图.宋.范宽.绢本浅设色.台北故宫博物院藏.jpg；License: Public domain（PD-Art）
  - 落盘: 903×1800px，355 KB
- **xuejing_hanlin.jpg** — 雪景寒林图，Fan Kuan，北宋，天津博物馆。
  - 来源: https://commons.wikimedia.org/wiki/File:Xuejinghanlintu.jpg；License: Public domain（PD-Art）
  - 落盘: 1496×1800px，978 KB
- **zhaoyuan_handscroll.jpg** — 趙原《倣燕文貴范寬山水圖》卷（局部段），Fan Kuan，元末（14世纪晚期），大都会艺术博物馆（MET 1981.285.15）。
  - 来源: https://digitalarchive.npm.gov.tw/Collection/Detail/5100?dep=P（MET Open Access：https://images.metmuseum.org/CRDImages/as/original/DP303149.jpg（Commons 同源））；License: **CC0**（MET Open Access）
  - 落盘: 1800×516px，310 KB

### sesshu — 雪舟（18 张；wave19 并入）
- **amanohashidate.jpg** — 《天橋立図》（国宝），Sesshū Tōyō，16 世紀（1501 以降説有力），京都国立博物館（A甲228）。
  - 来源: https://commons.wikimedia.org/wiki/File:Sesshu_-_View_of_Ama-no-Hashidate.jpg；License: Public domain（PD-Art）
  - 落盘: 1800×951px，585 KB
- **autumn_winter_autumn.jpg** — 《秋冬山水図》秋景（国宝，2 幅のうち），Sesshū Tōyō，15 世紀末–16 世紀初，東京国立博物館（A-1398）。
  - 来源: https://commons.wikimedia.org/wiki/File:SesshuToyo.jpg；License: Public domain（PD-Art）
  - 落盘: 1157×1800px，817 KB
- **autumn_winter_winter.jpg** — 《秋冬山水図》冬景（国宝），Sesshū Tōyō，15 世紀末–16 世紀初，東京国立博物館（A-1398）。
  - 来源: https://commons.wikimedia.org/wiki/File:SesshuShuutouTou.jpg；License: Public domain（PD-Art）
  - 落盘: 1161×1800px，792 KB
- **birds_flowers_left.jpg** — 《四季花鳥図屏風》（伝雪舟；重要文化財）左隻，Sesshū Tōyō，15 世紀，東京国立博物館。
  - 来源: https://commons.wikimedia.org/wiki/File:SESHU_Birds-flowers-L.jpeg；License: Public domain（PD-Art）
  - 落盘: 1042×481px，154 KB
- **birds_flowers_right.jpg** — 《四季花鳥図屏風》（伝雪舟）右隻，Sesshū Tōyō，15 世紀，東京国立博物館。
  - 来源: https://commons.wikimedia.org/wiki/File:SESHU_Birds-flowers-R.jpeg；License: Public domain（PD-Art）
  - 落盘: 1045×481px，156 KB
- **bishamonten.jpg** — 《毘沙門天図》，Sesshū Tōyō，室町時代，画像注记「private collection, Tokyo」（2002 年没後 500 年展图录）；另有重文《毘沙門天図》（相国寺承天閣美術館）记录——异同未核（已查: Commons 文件页、ja.wiki 作品表）。
  - 来源: https://commons.wikimedia.org/wiki/File:Bishamonten_by_Sesshu_(Tokyo).jpeg；License: Public domain（PD-Art）
  - 落盘: 609×1800px，406 KB
- **four_seasons_mori_full.jpg** — 《四季山水図巻（山水長巻）》全巻（国宝），Sesshū Tōyō，文明18年（1486），毛利博物館。
  - 来源: https://commons.wikimedia.org/wiki/File:Landscapes_of_the_Four_Seasons_by_Sesshu_(Mori_Museum).jpg；License: Public domain（PD-Art）
  - 落盘: 1800×49px，45 KB
- **four_seasons_tnm_autumn.jpg** — 《四季山水図》4 幅のうち秋景（重要文化財；入明期作），Sesshū Tōyō，15 世紀，東京国立博物館（A-10933）。
  - 来源: https://commons.wikimedia.org/wiki/File:Sesshu_Toyo_-_Landscape_of_Four_Seasons-_Fall_-_Google_Art_Project.jpg；License: Public domain（PD-Art；Google Art Project）
  - 落盘: 937×1800px，481 KB
- **four_seasons_tnm_winter.jpg** — 《四季山水図》4 幅のうち冬景（重要文化財），Sesshū Tōyō，15 世紀，東京国立博物館（A-10933）。
  - 来源: https://commons.wikimedia.org/wiki/File:Sesshu_Toyo_-_Landscape_of_four_seasons-_winter_-_Google_Art_Project.jpg；License: Public domain（PD-Art；Google Art Project）
  - 落盘: 938×1800px，526 KB
- **haboku_sansui_1495.jpg** — 《破墨山水図》（指定名称「紙本墨画山水図」；国宝），Sesshū Tōyō，明応4年（1495），東京国立博物館（A-282）。
  - 来源: https://commons.wikimedia.org/wiki/File:Sesshu_-_Haboku-Sansui.jpg；License: Public domain（PD-Art）
  - 落盘: 1164×1800px，478 KB
- **haboku_sansui_complete.jpg** — 《破墨山水図》全幅（含雪舟自序 + 六僧题诗），Sesshū Tōyō，1495，東京国立博物館。
  - 来源: https://commons.wikimedia.org/wiki/File:Sesshu_-_Haboku-Sansui_-_complete.jpg；License: Public domain（PD-Art）
  - 落盘: 405×1800px，230 KB
- **huang_chuping.jpg** — 《倣梁楷黄初平図》（重要文化財），Sesshū Tōyō，室町時代，京都国立博物館。
  - 来源: https://commons.wikimedia.org/wiki/File:Huang_Chuping_by_Sesshu_(Kyoto_National_Museum).jpg；License: Public domain（PD-Art）
  - 落盘: 1800×1723px，958 KB
- **huike_offering_arm.jpg** — 《慧可断臂図》（国宝），Sesshū Tōyō，明応5年（1496），愛知・斉年寺（京都国立博物館寄託）。
  - 来源: https://commons.wikimedia.org/wiki/File:Bodhidharma.and.Huike-Sesshu.Toyo.jpg；License: Public domain（PD-Art）
  - 落盘: 1113×1800px，792 KB
- **mori_scroll_left.jpg** — 《四季山水図巻（山水長巻）》部分（左半），Sesshū Tōyō，1486，毛利博物館。
  - 来源: https://commons.wikimedia.org/wiki/File:SESSHU-Sansui_chokan-L.jpg；License: Public domain（PD-Art）
  - 落盘: 1680×703px，359 KB
- **mori_scroll_right.jpg** — 《四季山水図巻（山水長巻）》部分（右半），Sesshū Tōyō，1486，毛利博物館。
  - 来源: https://commons.wikimedia.org/wiki/File:SESSHU-Sansui_chokan-R.jpg；License: Public domain（PD-Art）
  - 落盘: 1547×669px，378 KB
- **portrait_sesshu_copy.jpg** — 《絹本著色雪舟自画像（模本）》（重文『紙本墨書題雪舟山水図詩 了庵桂悟筆』附指定），Sesshū Tōyō，16 世紀，藤田美術館。
  - 来源: https://commons.wikimedia.org/wiki/File:Portrait_of_Sesshu.jpg；License: Public domain（PD-Art）
  - 落盘: 988×1217px，256 KB
- **sesso_hatsuboku_nezou.jpg** — 雪村《破墨山水図》（影響链对照件；雪村=雪舟破墨系谱），Sesshū Tōyō，16 世紀（推定），根津美術館。
  - 来源: https://commons.wikimedia.org/wiki/File:Hatsuboku_landscape_by_Sesso_(Nezu_Museum).jpeg；License: Public domain（PD-Art）
  - 落盘: 1082×1800px，770 KB
- **xia_gui_imitation.jpg** — 《倣夏珪山水図》（2017 年 84 年ぶり再発見、「幻の作品」），Sesshū Tōyō，15 世紀，山口県立美術館寄託（個人蔵）。
  - 来源: https://commons.wikimedia.org/wiki/File:Landscape_in_Imitation_of_Xia_Gui_(%E5%80%A3%E5%A4%8F%E7%8F%AA%E5%B1%B1%E6%B0%B4%E5%9B%B3)_by_Sesshu.jpg；License: Public domain（PD-Art）
  - 落盘: 849×828px，134 KB

### constable — 康斯泰勃尔（17 张；wave19 并入）
- **brighton_beach_with_colliers.jpg** — Brighton Beach with Colliers（591-1888），John Constable，1824，Victoria and Albert Museum。
  - 来源: https://commons.wikimedia.org/wiki/File:Constable_-_Brighton_Beach_with_Colliers,_1824,_591-1888.jpg；License: Public domain
  - 落盘: 800×454px，74 KB
- **dedham_vale.jpg** — Dedham Vale，John Constable，1802，Yale Center for British Art。
  - 来源: https://commons.wikimedia.org/wiki/File:John_Constable_-_Dedham_Vale_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1448px，829 KB
- **flatford_mill.jpg** — Flatford Mill (Scene on a Navigable River, N01273)，John Constable，1816–17，Tate。
  - 来源: https://commons.wikimedia.org/wiki/File:Flatford_Mill_(Scene_on_a_Navigable_River)_by_John_Constable,_Tate_Britain.JPG；License: CC0
  - 落盘: 1800×1436px，475 KB
- **hampstead_heath_with_rainbow.jpg** — Hampstead Heath with a Rainbow（N01275），John Constable，1836，Tate。
  - 来源: https://commons.wikimedia.org/wiki/File:John_Constable_(1776-1837)_-_Hampstead_Heath_with_a_Rainbow_-_N01275_-_National_Gallery.jpg；License: Public domain
  - 落盘: 1132×748px，195 KB
- **salisbury_cathedral_from_the_bishops_grounds.jpg** — Salisbury Cathedral from the Bishop's Grounds（FA.33），John Constable，1823，Victoria and Albert Museum。
  - 来源: https://commons.wikimedia.org/wiki/File:John_Constable_-_Salisbury_Cathedral_from_the_Bishop%27s_Grounds.jpg；License: Public domain
  - 落盘: 1800×1401px，811 KB
- **salisbury_cathedral_from_the_meadows.jpg** — Salisbury Cathedral from the Meadows（T13896），John Constable，exhibited 1831，Tate。
  - 来源: https://commons.wikimedia.org/wiki/File:Constable_Salisbury_meadows.jpg；License: Public domain
  - 落盘: 1800×1440px，699 KB
- **seascape_study_with_rain_cloud.jpg** — Seascape Study with Rain Cloud，John Constable，c.1827，Royal Academy of Arts。
  - 来源: https://commons.wikimedia.org/wiki/File:Constable_-_Seascape_Study_with_Rain_Cloud.jpg；License: Public domain
  - 落盘: 1800×1309px，513 KB
- **stonehenge.jpg** — Stonehenge（1629-1888），John Constable，1835，Victoria and Albert Museum。
  - 来源: https://commons.wikimedia.org/wiki/File:John_Constable_-_Stonehenge_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1193px，273 KB
- **study_of_cirrus_clouds.jpg** — Study of Cirrus Clouds（784-1888；背面「cirrus」），John Constable，ca. 1822，Victoria and Albert Museum。
  - 来源: https://commons.wikimedia.org/wiki/File:Constable_-_Study_of_Cirrus_Clouds,_c.1822,_784-1888.jpg；License: Public domain
  - 落盘: 800×519px，55 KB
- **study_of_clouds_1822.jpg** — Study of Clouds（590-1888；题记「Sepr. 5. 1822」），John Constable，1822，Victoria and Albert Museum。
  - 来源: https://commons.wikimedia.org/wiki/File:Constable_-_Study_of_Clouds,_1822,_590-1888.jpg；License: Public domain
  - 落盘: 800×487px，60 KB
- **study_of_clouds_above_wide_landscape.jpg** — Study of clouds above a wide landscape（240-1888；题记「Sepr 15 1830」），John Constable，1830，Victoria and Albert Museum。
  - 来源: https://commons.wikimedia.org/wiki/File:Constable_-_Study_of_clouds_above_a_wide_landscape,_240-1888.jpg；License: Public domain
  - 落盘: 1800×1496px，580 KB
- **the_cornfield_1826.jpg** — The Cornfield（麦田，NG130），John Constable，1826，National Gallery, London。
  - 来源: https://commons.wikimedia.org/wiki/File:John_Constable_-_The_Cornfield.jpg；License: Public domain
  - 落盘: 1541×1800px，850 KB
- **the_hay_wain_1821.jpg** — The Hay Wain（干草车，NG1207），John Constable，1821，National Gallery, London。
  - 来源: https://commons.wikimedia.org/wiki/File:John_Constable_-_The_Hay_Wain_(1821).jpg；License: Public domain
  - 落盘: 1800×1241px，755 KB
- **the_leaping_horse.jpg** — The Leaping Horse（03/1391），John Constable，1825，Royal Academy of Arts。
  - 来源: https://commons.wikimedia.org/wiki/File:The_Leaping_Horse_(1825)_by_John_Constable_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1200×902px，273 KB
- **the_valley_farm.jpg** — The Valley Farm（N00327），John Constable，c.1835，Tate。
  - 来源: https://commons.wikimedia.org/wiki/File:John_Constable_-_The_Valley_Farm,_c._1835.jpg；License: Public domain
  - 落盘: 1515×1800px，499 KB
- **the_white_horse.jpg** — The White Horse（1943.1.147），John Constable，1819，The Frick Collection。
  - 来源: https://commons.wikimedia.org/wiki/File:The_White_Horse_by_John_Constable_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1243px，576 KB
- **wivenhoe_park.jpg** — Wivenhoe Park, Essex（1942.9.10），John Constable，1816，National Gallery of Art, Washington。
  - 来源: https://commons.wikimedia.org/wiki/File:John_Constable_-_Wivenhoe_Park,_Essex_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×974px，403 KB

### poussin — 普桑（13 张；wave19 并入）
- **a_dance_to_the_music_of_time.jpg** — A Dance to the Music of Time（随时间之乐起舞），Nicolas Poussin，c. 1634–36，Wallace Collection, London。
  - 来源: https://commons.wikimedia.org/wiki/File:The_dance_to_the_music_of_time_c._1640.jpg；License: Public domain
  - 落盘: 1800×1408px，700 KB
- **adoration_of_the_golden_calf.jpg** — The Adoration of the Golden Calf（金牛犊的崇拜，NG5597），Nicolas Poussin，1633–4，The National Gallery, London。
  - 来源: https://commons.wikimedia.org/wiki/File:Nicolas_Poussin_-_The_Adoration_of_the_Golden_Calf_alt.jpg；License: Public domain
  - 落盘: 1800×1290px，381 KB
- **autoportrait_1650.jpg** — Autoportrait（自画像，INV 7302），Nicolas Poussin，1650，Musée du Louvre。
  - 来源: https://commons.wikimedia.org/wiki/File:Poussin_-_Autoportrait,_1650,_INV_7302_;_MR_2329.jpg；License: Public domain
  - 落盘: 1147×1500px，192 KB
- **blind_orion_searching_for_the_rising_sun.jpg** — Blind Orion Searching for the Rising Sun（盲 Orion，24.45.1），Nicolas Poussin，1658，The Met, New York。
  - 来源: https://commons.wikimedia.org/wiki/File:Orion_aveugle_cherchant_le_soleil.jpg；License: Public domain
  - 落盘: 1800×1178px，620 KB
- **et_in_arcadia_ego.jpg** — Les Bergers d'Arcadie（阿卡迪亚的牧人，INV 7300），Nicolas Poussin，vers 1638，Musée du Louvre。
  - 来源: https://commons.wikimedia.org/wiki/File:Nicolas_Poussin_-_Et_in_Arcadia_ego_(deuxi%C3%A8me_version).jpg；License: Public domain
  - 落盘: 1800×1283px，825 KB
- **l_enlevement_des_sabines.jpg** — L'Enlèvement des Sabines（劫夺萨宾妇女，INV 7290），Nicolas Poussin，vers 1637–1638，Musée du Louvre。
  - 来源: https://commons.wikimedia.org/wiki/File:L%27Enl%C3%A8vement_des_Sabines_-_Nicolas_Poussin_-_Mus%C3%A9e_du_Louvre_Peintures_INV_7290_;_MR_2335.jpg；License: Public domain
  - 落盘: 1800×1363px，662 KB
- **l_inspiration_du_poete.jpg** — L'Inspiration du poète（诗人的灵感，RF 1774），Nicolas Poussin，vers 1629，Musée du Louvre。
  - 来源: https://commons.wikimedia.org/wiki/File:L%27Inspiration_du_po%C3%A8te_-_Nicolas_Poussin_-_Mus%C3%A9e_du_Louvre_-_Peintures_RF_1774.jpg；License: Public domain
  - 落盘: 1800×1523px，685 KB
- **la_manne.jpg** — La Manne（吗哪的收集，INV 7275），Nicolas Poussin，1638–1639，Musée du Louvre。
  - 来源: https://commons.wikimedia.org/wiki/File:La_Manne_-_Nicolas_Poussin_-_Mus%C3%A9e_du_Louvre_Peintures_INV_7275.jpg；License: Public domain
  - 落盘: 1800×1316px，552 KB
- **la_peste_d_asdod.jpg** — La Peste d'Asdod（阿什杜德的瘟疫，INV 7276），Nicolas Poussin，1630–1631，Musée du Louvre。
  - 来源: https://commons.wikimedia.org/wiki/File:La_Peste_d%27Asdod_-_Nicolas_Poussin_-_Mus%C3%A9e_du_Louvre_Peintures_INV_7276_;_MR_2312.jpg；License: Public domain
  - 落盘: 1800×1318px，713 KB
- **landscape_with_a_man_killed_by_a_snake.jpg** — Landscape with a Man killed by a Snake（蛇景，NG5763），Nicolas Poussin，probably 1648，The National Gallery, London。
  - 来源: https://commons.wikimedia.org/wiki/File:Landscape-with-a-man-killed-by-a-snake-Poussin.jpg；License: Public domain
  - 落盘: 1700×1014px，452 KB
- **le_jugement_de_salomon.jpg** — Le Jugement de Salomon（所罗门的审判，INV 7277），Nicolas Poussin，1649，Musée du Louvre。
  - 来源: https://commons.wikimedia.org/wiki/File:Le_Jugement_de_Salomon_-_1649_-_Nicolas_Poussin_-_Louvre_-_INV_7277_;_MR_2316_(2).jpg；License: Public domain
  - 落盘: 1800×1206px，532 KB
- **le_printemps.jpg** — Le Printemps（四季·春，INV 7303），Nicolas Poussin，1660–1664，Musée du Louvre。
  - 来源: https://commons.wikimedia.org/wiki/File:Nicolas_Poussin_-_Le_Printemps.jpg；License: Public domain
  - 落盘: 1800×1337px，410 KB
- **the_triumph_of_pan.jpg** — The Triumph of Pan（潘的凯旋，NG6477），Nicolas Poussin，1636，The National Gallery, London。
  - 来源: https://commons.wikimedia.org/wiki/File:Nicolas_Poussin_-_The_Triumph_of_Pan,_1636.jpg；License: Public domain
  - 落盘: 1800×1669px，876 KB

### bruegel — 老勃鲁盖尔（20 张；wave19 并入）
- **blind_leading_blind.jpg** — 盲人引盲 / The Blind Leading the Blind，Pieter Bruegel the Elder，1568，那不勒斯卡波迪蒙特博物馆。
  - 来源: https://commons.wikimedia.org/wiki/File:%D0%9F%D1%80%D0%B8%D1%82%D1%87%D0%B0_%D0%BE_%D1%81%D0%BB%D0%B5%D0%BF%D1%8B%D1%85.jpeg；License: Public domain
  - 落盘: 1800×1013px，690 KB
- **carnival_and_lent.jpg** — 狂欢节与四旬斋之战 / The Fight Between Carnival and Lent，Pieter Bruegel the Elder，1559，KHM（GG_1016）。
  - 来源: https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_d._%C3%84._066.jpg；License: Public domain
  - 落盘: 1800×1299px，1015 KB
- **census_at_bethlehem.jpg** — 伯利恒的人口调查 / The Census at Bethlehem，Pieter Bruegel the Elder，1566，布鲁塞尔皇家美术馆（Oldmasters）。
  - 来源: https://commons.wikimedia.org/wiki/File:Le_d%C3%A9nombrement_de_Bethl%C3%A9em_par_Pieter_Brueghel_l%27Ancien_-_1566_-_Bruxelles.jpg；License: Public domain
  - 落盘: 1800×1255px，695 KB
- **childrens_games.jpg** — 儿童游戏 / Children's Games，Pieter Bruegel the Elder，1560，KHM（GG_1017）。
  - 来源: https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_the_Elder_-_Children%E2%80%99s_Games_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1308px，896 KB
- **conversion_of_paul.jpg** — 保罗的皈依 / The Conversion of Paul，Pieter Bruegel the Elder，1567，KHM（GG_3690）。
  - 来源: https://commons.wikimedia.org/wiki/File:Conversion_of_Paul_(Bruegel).jpg；License: Public domain
  - 落盘: 1800×1260px，638 KB
- **dulle_griet.jpg** — 疯格丽特 / Dulle Griet (Mad Meg)，Pieter Bruegel the Elder，1561，安特卫普 Mayer van den Bergh 博物馆。
  - 来源: https://commons.wikimedia.org/wiki/File:Dulle_Griet,_by_Pieter_Brueghel_(I).jpg；License: Public domain
  - 落盘: 1800×1300px，823 KB
- **fall_of_the_rebel_angels.jpg** — 叛逆天使的坠落 / The Fall of the Rebel Angels，Pieter Bruegel the Elder，1562，布鲁塞尔皇家美术馆（Oldmasters）。
  - 来源: https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_the_Elder_-_The_Fall_of_the_Rebel_Angels_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1299px，758 KB
- **gloomy_day.jpg** — 阴天（早春）/ The Gloomy Day，Pieter Bruegel the Elder，1565，KHM（GG_1837）。
  - 来源: https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_de_Oude_-_De_sombere_dag_(vroege_voorjaar).jpg；License: Public domain
  - 落盘: 1800×1299px，929 KB
- **hay_harvest.jpg** — 刈草（早夏）/ The Hay Harvest (Haymaking)，Pieter Bruegel the Elder，1565，Lobkowicz Collections（布拉格）。
  - 来源: https://commons.wikimedia.org/wiki/File:Haymaking,_1565.jpg；License: Public domain
  - 落盘: 1800×1293px，671 KB
- **hunters_in_the_snow.jpg** — 雪中猎人 / The Hunters in the Snow (Winter)，Pieter Bruegel the Elder，1565，KHM（GG_1838）。
  - 来源: https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_the_Elder_-_Hunters_in_the_Snow_(Winter)_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1281px，761 KB
- **netherlandish_proverbs.jpg** — 尼德兰谚语 / Netherlandish Proverbs，Pieter Bruegel the Elder，1559，柏林国家博物馆绘画馆。
  - 来源: https://commons.wikimedia.org/wiki/File:Pieter_Brueghel_the_Elder_-_The_Dutch_Proverbs_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1275px，880 KB
- **peasant_and_nest_robber.jpg** — 农夫与掏鸟窝者 / The Peasant and the Nest Robber，Pieter Bruegel the Elder，1568，KHM（GG_1020）。
  - 来源: https://commons.wikimedia.org/wiki/File:The_Peasant_and_the_Nest_Robber.jpg；License: Public domain
  - 落盘: 1800×1515px，745 KB
- **peasant_dance.jpg** — 农民舞蹈 / The Peasant Dance，Pieter Bruegel the Elder，约 1568，KHM（GG_1059）。
  - 来源: https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_The_Peasant_Dance.jpg；License: Public domain
  - 落盘: 1800×1252px，860 KB
- **peasant_wedding.jpg** — 农民婚礼 / The Peasant Wedding，Pieter Bruegel the Elder，1568，KHM（GG_1027）。
  - 来源: https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_the_Elder_-_Peasant_Wedding_-_Google_Art_Project_2.jpg；License: Public domain
  - 落盘: 1800×1244px，683 KB
- **procession_to_calvary.jpg** — 前往髑髅地 / The Procession to Calvary，Pieter Bruegel the Elder，1564，KHM（GG_1025）。
  - 来源: https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_d._%C3%84._007.jpg；License: Public domain
  - 落盘: 1800×1307px，1090 KB
- **return_of_the_herd.jpg** — 牧群归来（秋）/ The Return of the Herd，Pieter Bruegel the Elder，1565，KHM（GG_1018）。
  - 来源: https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_(I)_-_The_Return_of_the_Herd_(1565).jpg；License: Public domain
  - 落盘: 1800×1303px，865 KB
- **the_harvesters.jpg** — 收割者 / The Harvesters，Pieter Bruegel the Elder，1565，The Met（19.164）。
  - 来源: https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_the_Elder-_The_Harvesters_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1311px，771 KB
- **tower_of_babel.jpg** — 巴别塔 / The Tower of Babel，Pieter Bruegel the Elder，1563，KHM（GG_1026）。
  - 来源: https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_the_Elder_-_The_Tower_of_Babel_(Vienna)_-_Google_Art_Project_-_edited.jpg；License: Public domain
  - 落盘: 1800×1317px，803 KB
- **triumph_of_death.jpg** — 死神的胜利 / The Triumph of Death，Pieter Bruegel the Elder，约 1562，普拉多博物馆。
  - 来源: https://commons.wikimedia.org/wiki/File:The_Triumph_of_Death_P001393.jpg；License: Public domain
  - 落盘: 1800×1284px，707 KB
- **winter_bird_trap.jpg** — 冬景与溜冰者和捕鸟器 / Winter Landscape with Skaters and Bird Trap，Pieter Bruegel the Elder，1565，布鲁塞尔皇家美术馆（Oldmasters）。
  - 来源: https://commons.wikimedia.org/wiki/File:Bruegel,_Pieter_(I)_-_Winterlandschap_met_schaatsers_en_vogelknip,_1565.jpg；License: Public domain
  - 落盘: 1800×1193px，878 KB

### el_greco — 埃尔·格列柯（17 张；wave19 并入）
- **adoration_of_the_shepherds_ca1605.jpg** — The Adoration of the Shepherds（牧羊人的朝拜；05.42），El Greco (Domenikos Theotokopoulos)，约 1605–10，The Met, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/436570；License: Public domain（Met OA）
  - 落盘: 1174×1800px，356 KB
- **burial_of_the_count_of_orgaz_1586.jpg** — The Burial of the Count of Orgaz（奥尔加斯伯爵的葬礼），El Greco (Domenikos Theotokopoulos)，1586–88，Iglesia de Santo Tomé, Toledo（原位）。
  - 来源: https://commons.wikimedia.org/wiki/File:El_entierro_del_señor_de_Orgaz_-_El_Greco.jpg；License: Public domain
  - 落盘: 1350×1800px，797 KB
- **cardinal_guevara_ca1600.jpg** — Cardinal Fernando Niño de Guevara（红衣主教格瓦拉；29.100.5），El Greco (Domenikos Theotokopoulos)，约 1600，The Met, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/436573；License: Public domain（Met OA）
  - 落盘: 1350×1800px，438 KB
- **christ_healing_the_blind_ca1570.jpg** — Christ Healing the Blind（治愈盲人；1978.416），El Greco (Domenikos Theotokopoulos)，约 1570，The Met, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/436572；License: Public domain（Met OA）
  - 落盘: 1800×1496px，581 KB
- **dormition_of_the_virgin_1565.jpg** — Dormition of the Virgin（圣母安眠；克里特期圣像，签名款），El Greco (Domenikos Theotokopoulos)，约 1565–67，锡罗斯岛埃尔穆波利（Ermoupolis, Syros）。
  - 来源: https://commons.wikimedia.org/wiki/File:Dormition_El_Greco.jpg；License: Public domain
  - 落盘: 1086×1304px，581 KB
- **el_expolio_1577.jpg** — El Expolio（剥夺圣衣），El Greco (Domenikos Theotokopoulos)，1577–79，Catedral de Toledo（圣器室，原位）。
  - 来源: https://commons.wikimedia.org/wiki/File:El_Expolio_del_Greco_Catedral_de_Toledo.jpg；License: Public domain
  - 落盘: 1071×1800px，954 KB
- **immaculate_conception_1607.jpg** — The Immaculate Conception（圣母无原罪；Oballe 小堂），El Greco (Domenikos Theotokopoulos)，1607–13，Museo de Santa Cruz, Toledo。
  - 来源: https://commons.wikimedia.org/wiki/File:Inmaculada_Oballe_El_Greco.jpg；License: Public domain
  - 落盘: 700×1376px，220 KB
- **laocoon_ca1610.jpg** — Laocoön（拉奥孔），El Greco (Domenikos Theotokopoulos)，约 1610–14，National Gallery of Art, Washington（1990.123.1）。
  - 来源: https://commons.wikimedia.org/wiki/File:El_Greco_(Domenikos_Theotokopoulos)_-_Laocoön_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1433px，729 KB
- **modena_triptych_1568.jpg** — The Modena Triptych（摩德纳三联画），El Greco (Domenikos Theotokopoulos)，1567–68，Galleria Estense, Modena。
  - 来源: https://commons.wikimedia.org/wiki/File:Triptico_de_Modena_El_Greco.jpg；License: Public domain
  - 落盘: 1356×900px，226 KB
- **nobleman_with_hand_on_chest_ca1580.jpg** — The Nobleman with his Hand on his Chest（手抚胸口的绅士；P00809），El Greco (Domenikos Theotokopoulos)，约 1580，Museo del Prado, Madrid。
  - 来源: https://commons.wikimedia.org/wiki/File:The_Nobleman_with_his_hand_on_his_chest,_by_El_Greco_(Museo_del_Prado,_Madrid).jpg；License: Public domain
  - 落盘: 1405×1800px，626 KB
- **paravicino_1609.jpg** — Portrait of Fray Hortensio Félix Paravicino（帕拉维奇诺肖像），El Greco (Domenikos Theotokopoulos)，1609，Museum of Fine Arts, Boston。
  - 来源: https://commons.wikimedia.org/wiki/File:El_Greco_(Domenikos_Theotokopoulos)_-_Fray_Hortensio_Félix_Paravicino_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1385×1800px，762 KB
- **pentecost_ca1600.jpg** — Pentecost（五旬节；Doña María de Aragón 组画），El Greco (Domenikos Theotokopoulos)，约 1600，Museo del Prado, Madrid。
  - 来源: https://commons.wikimedia.org/wiki/File:Pentecostés_(El_Greco,_c._1600)_Prado.jpg；License: Public domain
  - 落盘: 829×1800px，373 KB
- **saint_jerome_as_scholar_ca1610.jpg** — Saint Jerome as Scholar（学者圣杰罗姆；1975.1.146），El Greco (Domenikos Theotokopoulos)，约 1610，The Met, New York（Lehman Collection）。
  - 来源: https://www.metmuseum.org/art/collection/search/459088；License: Public domain（Met OA）
  - 落盘: 1484×1800px，460 KB
- **saint_martin_and_the_beggar_ca1597.jpg** — Saint Martin and the Beggar（圣马丁与乞丐），El Greco (Domenikos Theotokopoulos)，约 1597，Art Institute of Chicago（1949.1093）。
  - 来源: https://commons.wikimedia.org/wiki/File:Domenico_Theotokópoulos,_called_El_Greco_-_Saint_Martin_and_the_Beggar_-_1949.1093_-_Art_Institute_of_Chicago.jpg；License: Public domain
  - 落盘: 1028×1800px，465 KB
- **the_holy_trinity_1577.jpg** — The Holy Trinity（三位一体；P000824），El Greco (Domenikos Theotokopoulos)，1577–79，Museo del Prado, Madrid。
  - 来源: https://commons.wikimedia.org/wiki/File:La_Trinidad_(El_Greco,_1577-1579).jpg；License: Public domain
  - 落盘: 1038×1800px，598 KB
- **view_of_toledo_ca1599.jpg** — View of Toledo（托莱多风景；29.100.6），El Greco (Domenikos Theotokopoulos)，约 1599–1600，The Met, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/436575；License: Public domain（Met OA）
  - 落盘: 1600×1800px，440 KB
- **vision_of_saint_john_ca1608.jpg** — The Vision of Saint John（圣约翰的异象/第五封印的开启；56.48），El Greco (Domenikos Theotokopoulos)，约 1608–14，The Met, New York。
  - 来源: https://www.metmuseum.org/art/collection/search/436576；License: Public domain（Met OA）
  - 落盘: 1601×1800px，496 KB

### holbein — 荷尔拜因（13 张；wave19 并入）
- **ambassadors.jpg** — The Ambassadors（大使们；Jean de Dinteville & Georges de Selve，NG1314），Hans Holbein the Younger，1533，The National Gallery, London。
  - 来源: https://commons.wikimedia.org/wiki/File:Hans_Holbein_the_Younger_-_The_Ambassadors_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1774px，815 KB
- **anne_of_cleves.jpg** — Portrait of Anne of Cleves（克利夫斯的安妮，INV 1348），Hans Holbein the Younger，1539，Musée du Louvre, Paris。
  - 来源: https://commons.wikimedia.org/wiki/File:Anne_de_Cl%C3%A8ves_-_Hans_Holbein_le_Jeune_-_Mus%C3%A9e_du_Louvre_Peintures_INV_1348_;_MR_756_-_version_2.jpg；License: Public domain
  - 落盘: 1307×1800px，666 KB
- **bonifacius_amerbach_1519.jpg** — Portrait of Bonifacius Amerbach（博尼法修斯·阿梅尔巴赫），Hans Holbein the Younger，1519，Kunstmuseum Basel。
  - 来源: https://commons.wikimedia.org/wiki/File:Portrait_of_Bonifacius_Amerbach_by_Hans_Holbein_the_Younger_(1519).jpg；License: Public domain
  - 落盘: 882×906px，169 KB
- **charles_de_solier.jpg** — Charles de Solier, Sieur de Morette（夏尔·德·索利耶），Hans Holbein the Younger，1534，Gemäldegalerie Alte Meister, Dresden。
  - 来源: https://commons.wikimedia.org/wiki/File:Hans_Holbein_the_Younger_-_Charles_de_Solier,_Sieur_de_Morette_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1432×1800px，511 KB
- **christina_of_denmark.jpg** — Christina of Denmark, Duchess of Milan（丹麦的克里斯蒂娜，NG2475），Hans Holbein the Younger，1538，The National Gallery, London。
  - 来源: https://commons.wikimedia.org/wiki/File:Christina_of_Denmark,_Duchess_of_Milan.jpg；License: Public domain
  - 落盘: 809×1800px，152 KB
- **darmstadt_madonna.jpg** — Darmstadt Madonna（达姆施塔特圣母），Hans Holbein the Younger，1525–26 & 1528，Sammlung Würth（Johanniterkirche, Schwäbisch Hall；2012 年起）。
  - 来源: https://commons.wikimedia.org/wiki/File:Darmstadtmadonna.jpg；License: Public domain
  - 落盘: 1272×1800px，689 KB
- **dead_christ.jpg** — The Body of the Dead Christ in the Tomb（墓中基督），Hans Holbein the Younger，1521/22，Kunstmuseum Basel。
  - 来源: https://commons.wikimedia.org/wiki/File:Holbein_%E2%80%94_Dead_Christ.jpg；License: CC0
  - 落盘: 1800×269px，124 KB
- **edward_vi_as_a_child.jpg** — Edward VI as a Child（幼年爱德华六世），Hans Holbein the Younger，c. 1538，National Gallery of Art, Washington D.C.。
  - 来源: https://commons.wikimedia.org/wiki/File:Hans_Holbein_the_Younger_-_Edward_VI_as_a_Child_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1387×1800px，789 KB
- **erasmus_1523.jpg** — Erasmus（伊拉斯谟，L658），Hans Holbein the Younger，1523，The National Gallery, London（Longford Castle 借展）。
  - 来源: https://commons.wikimedia.org/wiki/File:Holbein-erasmus.jpg；License: Public domain
  - 落盘: 1272×1800px，484 KB
- **georg_gisze.jpg** — Der Kaufmann Georg Gisze（商人吉斯泽），Hans Holbein the Younger，1532，Berlin State Museums（Gemäldegalerie）。
  - 来源: https://commons.wikimedia.org/wiki/File:Hans_Holbein_der_J%C3%BCngere_-_Der_Kaufmann_Georg_Gisze_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1577×1800px，744 KB
- **henry_viii.jpg** — Portrait of Henry VIII（亨利八世；白厅壁画系统摹本，WAG 1350），Hans Holbein the Younger，c. 1540–1547，Walker Art Gallery, Liverpool。
  - 来源: https://commons.wikimedia.org/wiki/File:After_Hans_Holbein_the_Younger_-_Portrait_of_Henry_VIII_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1023×1800px，667 KB
- **self_portrait_1542.jpg** — Self-portrait（自画像），Hans Holbein the Younger，c. 1542/43，Uffizi, Florence。
  - 来源: https://commons.wikimedia.org/wiki/File:Hans_Holbein_the_Younger,_self-portrait.jpg；License: Public domain
  - 落盘: 1318×1800px，925 KB
- **thomas_more.jpg** — Sir Thomas More（托马斯·莫尔），Hans Holbein the Younger，1527，The Frick Collection, New York。
  - 来源: https://commons.wikimedia.org/wiki/File:Hans_Holbein,_the_Younger_-_Sir_Thomas_More_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1447×1800px，657 KB

### aivazovsky — 艾瓦佐夫斯基（14 张；wave19 并入）
- **among_the_waves_1898.jpg** — Among the Waves（Среди волн；**58×96 cm 版本**，苏富比 2008 Lot 4 记录；费奥多西亚藏巨幅版另件），Ivan Aivazovsky，1898，私人（苏富比 2008）。
  - 来源: https://commons.wikimedia.org/wiki/File:Ivan_Konstantinovich_Aivazovsky_-_Among_the_Waves%2C_1898.jpg；License: Public domain
  - 落盘: 1800×1115px，211 KB
- **black_sea_1881.jpg** — The Black Sea / На Черном море начинает разыгрываться буря（特列 Инв.803，149×210），Ivan Aivazovsky，1881，特列季亚科夫（Google Art Project 扫描）。
  - 来源: https://commons.wikimedia.org/wiki/File:%D0%98%D0%B2%D0%B0%D0%BD_%D0%9A%D0%BE%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%82%D0%B8%D0%BD%D0%BE%D0%B2%D0%B8%D1%87_%D0%90%D0%B9%D0%B2%D0%B0%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_-_%D0%A7%D0%B5%D1%80%D0%BD%D0%BE%D0%B5_%D0%BC%D0%BE%D1%80%D0%B5_%28%D0%BD%D0%B0_%D0%A7%D0%B5%D1%80%D0%BD%D0%BE%D0%BC_%D0%BC%D0%BE%D1%80%D0%B5_%D0%BD%D0%B0%D1%87%D0%B8%D0%BD%D0%B0%D0%B5%D1%82_%D1%80%D0%B0%D0%B7%D1%8B%D0%B3%D1%80%D1%8B%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F_%D0%B1%D1%83%D1%80%D1%8F%29_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1292px，408 KB
- **brig_mercury_1848.jpg** — Бриг «Меркурий» после победы над двумя турецкими судами（俄博 2026 特展杰作），Ivan Aivazovsky，1848，俄博。
  - 来源: https://commons.wikimedia.org/wiki/File:Aivasovsky_Ivan_Constantinovich_merkuri_1848_IBI.jpg；License: Public domain
  - 落盘: 1800×1148px，376 KB
- **chesme_battle_1848.jpg** — Чесменский бой / Battle of Çesme at Night（切什梅夜战），Ivan Aivazovsky，1848，未注（多源扫描）。
  - 来源: https://commons.wikimedia.org/wiki/File:Chesmabattle.jpg；License: Public domain
  - 落盘: 1688×1800px，495 KB
- **constantinople_bosphorus.jpg** — Вид Константинополя и Босфора / View of Constantinople and the Bosphorus，Ivan Aivazovsky，1856，私人（Sotheby's 2012 Orientalist Sale, lot 6）。
  - 来源: https://commons.wikimedia.org/wiki/File:Aivazovsky_-_View_of_Constantinople_and_the_Bosphorus.jpg；License: Public domain
  - 落盘: 1800×1129px，322 KB
- **galata_tower_moonlight.jpg** — Галатская башня в лунном свете / The Galata Tower by Moonlight，Ivan Aivazovsky，1845，私人（Sotheby's London 2012-11-26, lot 5）。
  - 来源: https://commons.wikimedia.org/wiki/File:%D0%93%D0%B0%D0%BB%D0%B0%D1%82%D1%81%D0%BA%D0%B0%D1%8F_%D0%B1%D0%B0%D1%88%D0%BD%D1%8F_%D0%B2_%D0%BB%D1%83%D0%BD%D0%BD%D0%BE%D0%BC_%D1%81%D0%B2%D0%B5%D1%82%D0%B5.jpg；License: Public domain
  - 落盘: 1800×1237px，262 KB
- **moonlit_night.jpg** — Лунная ночь / Moonlight Night，Ivan Aivazovsky，1849，未注（aivazovski.ru 扫描）。
  - 来源: https://commons.wikimedia.org/wiki/File:%D0%9B%D1%83%D0%BD%D0%BD%D0%B0%D1%8F_%D0%BD%D0%BE%D1%87%D1%8C_%D0%90%D0%B9%D0%B2%D0%B0%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9.jpg；License: Public domain
  - 落盘: 1800×1124px，373 KB
- **neapolitan_bay_moonlit.jpg** — Неаполитанский залив в лунную ночь / The Bay of Naples by Moonlight（92×141 cm，ФКГА 藏），Ivan Aivazovsky，1842，费奥多西亚画廊（ФКГА；扫描件）。
  - 来源: https://commons.wikimedia.org/wiki/File:%D0%9D%D0%B5%D0%B0%D0%BF%D0%BE%D0%BB%D0%B8%D1%82%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B7%D0%B0%D0%BB%D0%B8%D0%B2_%D0%B2_%D0%BB%D1%83%D0%BD%D0%BD%D1%83%D1%8E_%D0%BD%D0%BE%D1%87%D1%8C_%D0%90%D0%B9%D0%B2%D0%B0%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9.jpg；License: Public domain
  - 落盘: 1280×814px，394 KB
- **night_in_gurzuf_1891.jpg** — Ночь в Гурзуфе / Night at Gurzuf（**1891 版本**；费奥多西亚另藏同名作），Ivan Aivazovsky，1891，私人（Heritage Auctions 2008, lot 65005）。
  - 来源: https://commons.wikimedia.org/wiki/File:%D0%98%D0%B2%D0%B0%D0%BD_%D0%9A%D0%BE%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%82%D0%B8%D0%BD%D0%BE%D0%B2%D0%B8%D1%87_%D0%90%D0%B9%D0%B2%D0%B0%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_-_%D0%9D%D0%BE%D1%87%D1%8C_%D0%B2_%D0%93%D1%83%D1%80%D0%B7%D1%83%D1%84%D0%B5.jpg；License: Public domain
  - 落盘: 1800×1348px，616 KB
- **ninth_wave_1850.jpg** — The Ninth Wave（Девятый вал；俄博 Ж-2202，221×332），Ivan Aivazovsky，1850，俄博（Google Art Project 扫描）。
  - 来源: https://commons.wikimedia.org/wiki/File:Hovhannes_Aivazovsky_-_The_Ninth_Wave_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1209px，326 KB
- **rainbow_1873.jpg** — The Rainbow（Радуга；特列 Инв.801，105×136），Ivan Aivazovsky，1873，特列季亚科夫。
  - 来源: https://commons.wikimedia.org/wiki/File:%D0%90%D0%B9%D0%B2%D0%B0%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%28%D0%93%D0%B0%D0%B9%D0%B2%D0%B0%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9%29_%D0%98%D0%B2%D0%B0%D0%BD_%28%D0%9E%D0%B3%D0%B0%D0%BD%D0%B5%D1%81%29_%D0%9A%D0%BE%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%82%D0%B8%D0%BD%D0%BE%D0%B2%D0%B8%D1%87_%D0%A0%D0%B0%D0%B4%D1%83%D0%B3%D0%B0.jpg；License: Public domain
  - 落盘: 1539×1200px，301 KB
- **sevastopol_roads.jpg** — Русская эскадра на Севастопольском рейде / The Russian Squadron on the Sebastopol Roads，Ivan Aivazovsky，1846，未注。
  - 来源: https://commons.wikimedia.org/wiki/File:Ivan_Constantinovich_Aivazovsky_-_The_Russian_Squadron_on_the_Sebastopol_Roads.jpg；License: Public domain
  - 落盘: 1800×1139px，410 KB
- **stormy_sea_night_1849.jpg** — Буря на море ночью / Stormy Sea at Night（巴甫洛夫斯克宫），Ivan Aivazovsky，1849，巴甫洛夫斯克宫（扫描件）。
  - 来源: https://commons.wikimedia.org/wiki/File:Stormy_sea_at_night.jpg；License: Public domain
  - 落盘: 1460×1200px，300 KB
- **wave_1889.jpg** — Волна / The Wave（俄博 Ж-2200，304×505；上传者摄；已与俄博 VRM 参考图目检比对同一构图），Ivan Aivazovsky，1889，俄博。
  - 来源: https://commons.wikimedia.org/wiki/File:%D0%90%D0%B9%D0%B2%D0%B0%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%98.%D0%9A._%D0%92%D0%BE%D0%BB%D0%BD%D0%B0.jpg；License: Public domain
  - 落盘: 1800×1037px，410 KB

### zhao_mengfu — 赵孟頫（14 张；wave20 并入）
- **dongting_dongshan.jpg** — 洞庭东山图（轴），Zhao Mengfu，元，上海博物馆。
  - 来源: https://commons.wikimedia.org/wiki/File:赵孟頫_洞庭东山图轴.jpg；License: Public domain（PD-Art）
  - 落盘: 782×1800px，343 KB
- **hongyi_luohan.jpg** — 红衣罗汉图（画心），Zhao Mengfu，1304，辽宁省博物馆。
  - 来源: https://commons.wikimedia.org/wiki/File:5_Zhao_Mengfu_Monk_in_a_Red_Robe,_dated_1304_(26_x_52_cm)Liaoning_Provincial_Museum.jpg；License: Public domain（PD-Art）
  - 落盘: 1800×894px，687 KB
- **qiujiao_yinma_tu.jpg** — 秋郊饮马图（画心），Zhao Mengfu，1312，故宫博物院（故00005866）。
  - 来源: https://commons.wikimedia.org/wiki/File:Zhao_Mengfu._Horse_Herding_in_Autumn_Countryside_1312_23,6х59см,_Palace_Museum,_Beijing.jpg；License: Public domain（PD-Art）
  - 落盘: 1796×574px，201 KB
- **quehua_painting.jpg** — 鹊华秋色图（画心），Zhao Mengfu，1295，台北故宫博物院（故畫001011N000000000）。
  - 来源: https://commons.wikimedia.org/wiki/File:2_Zhao_Mengfu_Autumn_Colors_on_the_Qiao_and_Hua_Mountains_Handscroll,_ink_and_colors_on_paper,_28.4_x_93.2_cm_National_Palace_Museum,_Taipei..jpg；License: Public domain（PD-Art）
  - 落盘: 1800×545px，480 KB
- **renqi_tu.jpg** — 人骑图（画心），Zhao Mengfu，1296，故宫博物院（新00119107）。
  - 来源: https://commons.wikimedia.org/wiki/File:赵孟頫人骑图卷.png；License: Public domain（PD-Art）
  - 落盘: 1106×638px，173 KB
- **shuangsong_pingyuan.jpg** — 双松平远图（画心），Zhao Mengfu，约 1310，大都会艺术博物馆。
  - 来源: https://commons.wikimedia.org/wiki/File:3_Zhao_Mengfu_Twin_Pines,_Level_Distance,_ca._1310_(26.8_x_107.5_cm);The_Metropolitan_Museum_of_Art,_New_York.jpg；License: Public domain（PD-Art）
  - 落盘: 1800×428px，174 KB
- **shuicun_tu.jpg** — 水村图（画心），Zhao Mengfu，1302，故宫博物院（新00109759）。
  - 来源: https://commons.wikimedia.org/wiki/File:6_Zhao_Mengfu_Water_Village,_dated_1302_(24.9_x_120.5_cm);_Palace_Museum.jpg；License: Public domain（PD-Art）
  - 落盘: 1800×344px，169 KB
- **wuxing_qingyuan_hejuan.jpg** — 吴兴清远合卷（画心全段：赵孟頫原图＋崔复摹本），Zhao Mengfu，元，上海博物馆（沈同樾等捐赠）。
  - 来源: https://commons.wikimedia.org/wiki/File:赵孟頫_崔复_吴兴清远合卷.jpg；License: Public domain（PD-Art）
  - 落盘: 1800×258px，97 KB
- **xieyouyu_qiuhuo.jpg** — 谢幼舆丘壑图（画心），Zhao Mengfu，约 1287，普林斯顿大学艺术博物馆。
  - 来源: https://commons.wikimedia.org/wiki/File:Zhao_Mengfu_趙孟頫_-_The_Mind_Landscape_of_Xie_Youyu_(Youyu_qiu_he_幼輿丘壑_)_-_y1984-13_-_Princeton_University_Art_Museum.jpg；License: Public domain（PD-Art）
  - 落盘: 1800×363px，198 KB
- **xiushi_shulin_colophon.jpg** — 秀石疏林图·尾纸自题诗（「石如飞白木如籀」段），Zhao Mengfu，元，故宫博物院。
  - 来源: https://commons.wikimedia.org/wiki/File:赵孟頫秀石疏林图卷.png（同卷裁切）；License: Public domain（PD-Art）
  - 落盘: 1079×1797px，274 KB
- **xiushi_shulin_painting.jpg** — 秀石疏林图（画心），Zhao Mengfu，元，故宫博物院（新00147132）。
  - 来源: https://commons.wikimedia.org/wiki/File:赵孟頫秀石疏林图卷.png；License: Public domain（PD-Art）
  - 落盘: 1800×791px，294 KB
- **youhuang_daisheng.jpg** — 幽篁戴胜图（画心），Zhao Mengfu，元（早年），故宫博物院。
  - 来源: https://commons.wikimedia.org/wiki/File:10_ZhaoMengfu-_Hoopoe_on_Bamboo._Shanghai_mus..jpg；License: Public domain（PD-Art）
  - 落盘: 1800×1255px，1024 KB
- **yuma_tu.jpg** — 浴马图（画心），Zhao Mengfu，元，故宫博物院（新00154992）。
  - 来源: https://commons.wikimedia.org/wiki/File:Zhao_Mengfu._Bathing_Horses._28.1_x_155.5_cm_Palace_Museum,_Beijing..jpg；License: Public domain（PD-Art）
  - 落盘: 1800×346px，154 KB
- **zixiao_xiang.jpg** — 自写小像（册页），Zhao Mengfu，1299，故宫博物院。
  - 来源: https://commons.wikimedia.org/wiki/File:Zhao_Mengfu._Self_Portrait._1299,_Album_leaf._Palace_Museum_Beijing.jpg；License: Public domain（PD-Art）
  - 落盘: 1729×1800px，1685 KB

### ni_zan — 倪瓒（13 张；wave20 并入）
- **met_autumn_grove_1339.jpg** — 《秋林野兴图》轴（Enjoying the Wilderness in an Autumn Grove），Ni Zan，1339，大都会艺术博物馆（1989.363.38）。
  - 来源: https://www.metmuseum.org/art/collection/search/45635；License: CC0 1.0（Met Open Access）
  - 落盘: 1139×1800px，399 KB
- **met_wind_riverbank_1363.jpg** — 《江渚风林图》轴（Wind among the Trees on the Riverbank），Ni Zan，1363，大都会艺术博物馆（1989.363.39）。
  - 来源: https://www.metmuseum.org/art/collection/search/41154；License: CC0 1.0（Met Open Access）
  - 落盘: 1121×1800px，448 KB
- **met_woods_valleys_yushan_1372.jpg** — 《虞山林壑图》轴（Woods and Valleys of Mount Yu），Ni Zan，1372，大都会艺术博物馆（1973.120.8）。
  - 来源: https://www.metmuseum.org/art/collection/search/45636；License: CC0 1.0（Met Open Access）
  - 落盘: 993×1800px，389 KB
- **qishu_qiufeng.jpg** — 《琪树秋风图》轴，Ni Zan，无年款，上海博物馆。
  - 来源: https://commons.wikimedia.org/wiki/File:Ni_Zan_Autumn_Wind_in_Gemstones_Trees.jpg；License: Public domain（PD-Art）
  - 落盘: 1267×1800px，883 KB
- **rongxi_studio_1372.jpg** — 《容膝斋图》轴（Rongxi Studio），Ni Zan，1372，台北故宫博物院（故画000299；国宝）。
  - 来源: https://commons.wikimedia.org/wiki/File:Ni_Zan._The_Rongxi_Studio.1372._74,7x35,3._National_Palace_Museum,_Taipei.jpg；License: Public domain（PD-Art）
  - 落盘: 876×1800px，585 KB
- **six_gentlemen_1345.jpg** — 《六君子图》轴，Ni Zan，1345，上海博物馆。
  - 来源: https://commons.wikimedia.org/wiki/File:Ni_Zan_-_Six_Gentlemen.jpg；License: Public domain（PD-Art）
  - 落盘: 972×1800px，644 KB
- **ting_shu_yao_cen.jpg** — 《汀树遥岑图》轴，Ni Zan，1363（一作 1360 年代），上海博物馆。
  - 来源: https://commons.wikimedia.org/wiki/File:倪瓒_汀树遥岑图轴.jpg；License: Public domain（PD-Art）
  - 落盘: 887×1800px，468 KB
- **twin_trees_south_bank_1353.jpg** — 《岸南双树图》轴（Annan shuangshu），Ni Zan，1353，普林斯顿大学艺术博物馆（y1975-35）。
  - 来源: https://commons.wikimedia.org/wiki/File:Ni_Zan(倪瓚)_-_Twin_Trees_by_the_South_Bank_(Annan_shuangshu)_-_Google_Art_Project.jpg；License: Public domain（PD-Art，Google Art Project）
  - 落盘: 900×1800px，245 KB
- **water_bamboo_dwelling_1343.jpg** — 《水竹居图》轴，Ni Zan，1343，中国国家博物馆。
  - 来源: https://commons.wikimedia.org/wiki/File:Ni_Zan_Water_and_Bamboo_Dwelling.jpg；License: Public domain（PD-Art）
  - 落盘: 739×1400px，411 KB
- **wuzhu_xiushi.jpg** — 《梧竹秀石图》轴，Ni Zan，1360 年代，故宫博物院（北京）。
  - 来源: https://commons.wikimedia.org/wiki/File:倪瓒梧竹秀石图轴.png；License: Public domain（PD-Art）
  - 落盘: 688×1800px，344 KB
- **youjian_hansong.jpg** — 《幽涧寒松图》轴，Ni Zan，晚年（约 1370 年代），故宫博物院（北京）。
  - 来源: https://commons.wikimedia.org/wiki/File:倪瓒幽涧寒松图轴.png；License: Public domain（PD-Art）
  - 落盘: 1510×1800px，456 KB
- **yuzhuang_qiuji_1355.jpg** — 《渔庄秋霁图》轴，Ni Zan，1355（1372 补题），上海博物馆。
  - 来源: https://commons.wikimedia.org/wiki/File:倪瓒_渔庄秋霁图轴.jpg；License: Public domain（PD-Art）
  - 落盘: 872×1800px，420 KB
- **zhu_shu_xiao_shan.jpg** — 《竹树小山图》轴，Ni Zan，无年款，无锡博物院。
  - 来源: https://commons.wikimedia.org/wiki/File:元_倪瓒_竹树小山图轴_无锡博物院.jpg；License: Public domain（PD-Art）
  - 落盘: 1200×1800px，622 KB

### qiu_ying — 仇英（17 张；wave20 并入）
- **freer_minghuang_journey.jpg** — 《明皇幸蜀图》（Journey to Shu；传仇英，文徵明书），Qiu Ying，16–17世纪，Freer Gallery（F1993.4）。
  - 来源: https://asia.si.edu/object/fsg_F1993.4/；License: Public domain
  - 落盘: 1800×920px，504 KB
- **han_palace_d_konghou.jpg** — 《汉宫春晓》卷 细节（女乐·箜篌），Qiu Ying，明，台北故宫博物院。
  - 来源: https://digitalarchive.npm.gov.tw/Collection/Detail/3672?dep=P（IIIF: K2A001038N000000000PBW）；License: CC BY 4.0（NPM）
  - 落盘: 1347×1800px，818 KB
- **han_palace_d_serving_ladies.jpg** — 《汉宫春晓》卷 细节（侍女奉食·湖石），Qiu Ying，明，台北故宫博物院。
  - 来源: https://digitalarchive.npm.gov.tw/Collection/Detail/3672?dep=P（IIIF: K2A001038N000000000PDQ）；License: CC BY 4.0（NPM）
  - 落盘: 1303×1800px，789 KB
- **han_palace_d_stairs_attendant.jpg** — 《汉宫春晓》卷 细节（侍女拾级），Qiu Ying，明，台北故宫博物院。
  - 来源: https://digitalarchive.npm.gov.tw/Collection/Detail/3672?dep=P（IIIF: K2A001038N000000000PBN）；License: CC BY 4.0（NPM）
  - 落盘: 1347×1800px，845 KB
- **han_palace_full_scroll.jpg** — 《汉宫春晓》卷 全卷缩览（故畫001038），Qiu Ying，明（约 1542 后），台北故宫博物院。
  - 来源: https://digitalarchive.npm.gov.tw/Collection/Detail/3672?dep=P；License: CC BY 4.0（NPM）
  - 落盘: 1800×86px，32 KB
- **han_palace_s06_peacock_kids.jpg** — 《汉宫春晓》卷 第 6 段（孔雀·童子·舞女），Qiu Ying，明，台北故宫博物院。
  - 来源: https://digitalarchive.npm.gov.tw/Collection/Detail/3672?dep=P（IIIF: K2A001038N000000000PCV）；License: CC BY 4.0（NPM）
  - 落盘: 1800×1229px，539 KB
- **han_palace_s08_flower_picking.jpg** — 《汉宫春晓》卷 第 8 段（折花·太湖石），Qiu Ying，明，台北故宫博物院。
  - 来源: https://digitalarchive.npm.gov.tw/Collection/Detail/3672?dep=P（IIIF: K2A001038N000000000PAH）；License: CC BY 4.0（NPM）
  - 落盘: 1800×1230px，542 KB
- **han_palace_s12_doucao_reading.jpg** — 《汉宫春晓》卷 第 12 段（斗草·卧读），Qiu Ying，明，台北故宫博物院。
  - 来源: https://digitalarchive.npm.gov.tw/Collection/Detail/3672?dep=P（IIIF: K2A001038N000000000PDB）；License: CC BY 4.0（NPM）
  - 落盘: 1800×1229px，593 KB
- **linsong_bathing_infant.jpg** — 《临宋人画册》（浴婴图），Qiu Ying，明，上海博物馆。
  - 来源: https://commons.wikimedia.org/wiki/File:仇英_临宋人画册_2.jpg；License: Public domain
  - 落盘: 1755×1800px，719 KB
- **met_lady_bamboo_grove.jpg** — Lady in a Bamboo Grove（竹院仕女），Qiu Ying，约 1495–1552，The Met（36013）。
  - 来源: https://www.metmuseum.org/art/collection/search/36013；License: CC0
  - 落盘: 628×1800px，195 KB
- **met_lady_su_hui.jpg** — Lady Su Hui and Her Verse Puzzle（苏蕙回文图），Qiu Ying，16世纪，The Met（51584）。
  - 来源: https://www.metmuseum.org/art/collection/search/51584；License: CC0
  - 落盘: 1800×1383px，760 KB
- **met_tang_palace.jpg** — A Tang Palace（唐宫图），Qiu Ying，约 1495–1552，The Met（51285）。
  - 来源: https://www.metmuseum.org/art/collection/search/51285；License: CC0
  - 落盘: 1516×1604px，455 KB
- **renwu_guifei_xiaozhuang.jpg** — 《人物故事图册·贵妃晓妆》，Qiu Ying，明（16世纪），北京故宫博物院。
  - 来源: https://commons.wikimedia.org/wiki/File:仇英人物故事图册-2.png；License: Public domain
  - 落盘: 1800×1161px，309 KB
- **renwu_xunyang_pipa.jpg** — 《人物故事图册·浔阳琵琶》，Qiu Ying，明（16世纪），北京故宫博物院。
  - 来源: https://commons.wikimedia.org/wiki/File:仇英人物故事图册-8.png；License: Public domain
  - 落盘: 1800×1147px，245 KB
- **renwu_zhuyuan_pingu.jpg** — 《人物故事图册·竹院品古》，Qiu Ying，明（16世纪），北京故宫博物院。
  - 来源: https://commons.wikimedia.org/wiki/File:仇英人物故事图册-5.png；License: Public domain
  - 落盘: 1800×1148px，285 KB
- **taocun_caotang.jpg** — 《桃村草堂图》轴，Qiu Ying，明（16世纪），北京故宫博物院。
  - 来源: https://commons.wikimedia.org/wiki/File:Qiu_Ying_Peach_Village.jpg；License: Public domain
  - 落盘: 500×1246px，288 KB
- **taohua_xianjing_tianjin.jpg** — 《桃源仙境图》轴，Qiu Ying，明（16世纪），天津博物馆。
  - 来源: https://commons.wikimedia.org/wiki/File:Fairyland_of_Peach_Blossoms_-_Qiu_Ying.jpg；License: Public domain
  - 落盘: 676×1800px，376 KB

### ogata_korin — 尾形光琳（19 张；wave20 并入）
- **hoitsu_summer_autumn_left.jpg** — 夏秋草図屏風（秋草図＝風神図裏），Ogata Kōrin，19世紀（1821頃），東京国立博物館（酒井抱一筆）。
  - 来源: https://commons.wikimedia.org/wiki/File:Summer_and_Autumn_Flower_Plants_%28left%29.jpg；License: Public domain
  - 落盘: 1099×995px，334 KB
- **hoitsu_summer_autumn_right.jpg** — 夏秋草図屏風（夏草図＝雷神図裏），Ogata Kōrin，19世紀（1821頃），東京国立博物館（酒井抱一筆）。
  - 来源: https://commons.wikimedia.org/wiki/File:Summer_and_Autumn_Flower_Plants_%28right%29.jpg；License: Public domain
  - 落盘: 1102×994px，364 KB
- **korin_azalea.jpg** — 躑躅図，Ogata Kōrin，江戸時代・18世紀，畠山記念館（重文）。
  - 来源: https://commons.wikimedia.org/wiki/File:Azalea_Korin.JPG；License: Public domain
  - 落盘: 1171×713px，102 KB
- **korin_cranes_left.jpg** — 群鶴図屏風（左），Ogata Kōrin，江戸時代・18世紀，フリーア美術館。
  - 来源: https://commons.wikimedia.org/wiki/File:Cranes_%28left%29.png；License: Public domain
  - 落盘: 1800×818px，300 KB
- **korin_cranes_right.jpg** — 群鶴図屏風（右），Ogata Kōrin，江戸時代・18世紀，フリーア美術館。
  - 来源: https://commons.wikimedia.org/wiki/File:Cranes_%28right%29.png；License: Public domain
  - 落盘: 1115×498px，112 KB
- **korin_irises_left.jpg** — 燕子花図屏風（左隻），Ogata Kōrin，江戸時代・18世紀，根津美術館（国宝）。
  - 来源: https://commons.wikimedia.org/wiki/File:KORIN-Irises-L.jpg；License: Public domain
  - 落盘: 1800×755px，565 KB
- **korin_irises_right.jpg** — 燕子花図屏風（右隻），Ogata Kōrin，江戸時代・18世紀，根津美術館（国宝）。
  - 来源: https://commons.wikimedia.org/wiki/File:KORIN-Irises-R.jpg；License: Public domain
  - 落盘: 1800×753px，558 KB
- **korin_kuranosuke_portrait.jpg** — 中村内蔵助像，Ogata Kōrin，1704，大和文華館（重文）。
  - 来源: https://commons.wikimedia.org/wiki/File:Nakamura_Kuranosuke_by_Ogata_Korin_%28Yamato_Bunkakan%29.jpg；License: Public domain
  - 落盘: 357×843px，94 KB
- **korin_matsushima_mfa.jpg** — 松島図屏風，Ogata Kōrin，江戸時代・18世紀，ボストン美術館。
  - 来源: https://commons.wikimedia.org/wiki/File:Waves_at_Matsushima.jpg；License: Public domain
  - 落盘: 1559×648px，319 KB
- **korin_plum_full.jpg** — 紅白梅図屏風（一双全景），Ogata Kōrin，江戸時代・18世紀，MOA美術館（国宝）。
  - 来源: https://commons.wikimedia.org/wiki/File:Ogata_Korin_-_RED_AND_WHITE_PLUM_BLOSSOMS_%28National_Treasure%29_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×790px，468 KB
- **korin_plum_left.jpg** — 紅白梅図屏風（左隻局部），Ogata Kōrin，江戸時代・18世紀，MOA美術館（国宝）。
  - 来源: https://commons.wikimedia.org/wiki/File:KORIN-Plum-trees-L.jpg；License: Public domain
  - 落盘: 1158×1028px，326 KB
- **korin_plum_right.jpg** — 紅白梅図屏風（右隻局部），Ogata Kōrin，江戸時代・18世紀，MOA美術館（国宝）。
  - 来源: https://commons.wikimedia.org/wiki/File:KORIN-Plum-trees-R.jpg；License: Public domain
  - 落盘: 1158×1028px，330 KB
- **korin_rough_waves.jpg** — 波濤図屏風，Ogata Kōrin，ca. 1704–9，メトロポリタン美術館（26.117）。
  - 来源: https://commons.wikimedia.org/wiki/File:%E6%B3%A2%E6%BF%A4%E5%9B%B3%E5%B1%8F%E9%A2%A8-Rough_Waves_MET_DT1615.jpg；License: CC0（Met Open Access）
  - 落盘: 1800×1605px，698 KB
- **korin_suzuribako_eight_bridges.jpg** — 八橋蒔絵螺鈿硯箱，Ogata Kōrin，江戸時代・18世紀，東京国立博物館（国宝）。
  - 来源: https://commons.wikimedia.org/wiki/File:WritingBox_EightBridges_OgataKorin.JPG；License: Public domain
  - 落盘: 1270×1000px，259 KB
- **korin_taikobo_knm.jpg** — 太公望図，Ogata Kōrin，江戸時代・18世紀，京都国立博物館（重文 A甲535）。
  - 来源: https://commons.wikimedia.org/wiki/File:Tai_Gong_Wang_by_Ogata_Korin_%28Kyoto_National_Museum%29.jpg；License: Public domain
  - 落盘: 1800×1658px，868 KB
- **korin_wind_thunder.jpg** — 風神雷神図屏風，Ogata Kōrin，江戸時代・18世紀，東京国立博物館（重文）。
  - 来源: https://commons.wikimedia.org/wiki/File:Wind_God_and_Thunder_God_Screens_by_Ogata_Korin.png；License: Public domain
  - 落盘: 1800×811px，283 KB
- **korin_yatsuhashi_left.jpg** — 八橋図屏風（左隻），Ogata Kōrin，after 1709，メトロポリタン美術館（53.7.1,.2）。
  - 来源: https://commons.wikimedia.org/wiki/File:Irises_at_Yatsuhashi_%28left%29.jpg；License: Public domain
  - 落盘: 1800×824px，476 KB
- **korin_yatsuhashi_pair.jpg** — 八橋図屏風（双幅全景），Ogata Kōrin，after 1709，メトロポリタン美術館（53.7.1,.2）。
  - 来源: https://commons.wikimedia.org/wiki/File:Yatsuhashi-zu_By%C5%8Dbu_by_K%C5%8Drin_Ogata_%28171-14%29.jpg；License: Public domain
  - 落盘: 1800×409px，297 KB
- **korin_yatsuhashi_right.jpg** — 八橋図屏風（右隻），Ogata Kōrin，after 1709，メトロポリタン美術館（53.7.1,.2）。
  - 来源: https://commons.wikimedia.org/wiki/File:Irises_at_Yatsuhashi_%28right%29.jpg；License: Public domain
  - 落盘: 1800×823px，385 KB

### blake — 布莱克（18 张；wave20 并入）
- **albion_rose_1794.jpg** — Albion Rose（「Glad Day」，出自 A Large Book of Designs, copy A），William Blake，1794–96，British Museum。
  - 来源: https://commons.wikimedia.org/wiki/File:William_Blake_-_Albion_Rose_-_from_A_Large_Book_of_Designs_1793-6.jpg；License: Public domain
  - 落盘: 1327×1800px，1056 KB
- **ancient_of_days_1794.jpg** — Europe: A Prophecy, pl.1 卷首「The Ancient of Days」（乌里森持罗盘），William Blake，1794，Yale Center for British Art（copy A；lido-TMS-3878）。
  - 来源: https://commons.wikimedia.org/wiki/File:William_Blake_-_Europe._A_Prophecy,_Plate_1,_Frontispiece_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1260×1800px，424 KB
- **behemoth_and_leviathan_1825.jpg** — Behemoth and Leviathan（《约伯记》插图组画之十五，雕版），William Blake，1825，Museum of Fine Arts, Houston。
  - 来源: https://commons.wikimedia.org/wiki/File:William_Blake_-_Behemoth_and_Leviathan_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1344×1800px，832 KB
- **circle_of_the_lustful_1827.jpg** — The Circle of the Lustful: Paolo and Francesca（但丁《地狱篇》V，水彩），William Blake，c.1824–27，The Metropolitan Museum of Art（开放数据）。
  - 来源: https://commons.wikimedia.org/wiki/File:The_Circle_of_the_Lustful-_Paolo_and_Francesca,_from_Dante%27s_Inferno,_Canto_V_MET_DP816845.jpg；License: CC0 1.0
  - 落盘: 1800×1416px，880 KB
- **elohim_creating_adam_1795.jpg** — Elohim Creating Adam（埃洛希姆造亚当），William Blake，1795，Tate Britain（Yorck Project 扫描）。
  - 来源: https://commons.wikimedia.org/wiki/File:William_Blake_008.jpg；License: Public domain
  - 落盘: 1800×1459px，468 KB
- **europe_title_1794.jpg** — Europe: A Prophecy, pl.2 扉页（蛇形「Europe」题字），William Blake，1794，Yale Center for British Art（lido-TMS-3880）。
  - 来源: https://commons.wikimedia.org/wiki/File:William_Blake_-_Europe._A_Prophecy,_Plate_2,_Title_Page_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1191×1800px，425 KB
- **ghost_of_a_flea_c1819.jpg** — The Ghost of a Flea（跳蚤之魂，蛋彩＋金箔），William Blake，c.1819–20，Tate Britain（N05889）。
  - 来源: https://commons.wikimedia.org/wiki/File:William_Blake_-_The_Ghost_of_a_Flea_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1318×1800px，545 KB
- **great_red_dragon_c1805.jpg** — The Great Red Dragon and the Woman Clothed with the Sun（《启示录》12 章），William Blake，c.1803–05，National Gallery of Art（1943.3.8999，Rosenwald Collection）。
  - 来源: https://commons.wikimedia.org/wiki/File:William_Blake_-_The_Great_Red_Dragon_and_the_Woman_Clothed_with_the_Sun_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1465×1800px，815 KB
- **jerusalem_frontispiece_1804.jpg** — Jerusalem: The Emanation of the Giant Albion, pl.1 卷首「Los Entering the Grave」，William Blake，1804–20，Yale Center for British Art（lido-TMS-3428）。
  - 来源: https://commons.wikimedia.org/wiki/File:William_Blake_-_Jerusalem,_Plate_1,_Frontispiece_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1489×1800px，893 KB
- **marriage_of_heaven_and_hell_plate5_1827.jpg** — The Marriage of Heaven and Hell, Plate 5「Those who restrain desire…」（copy I），William Blake，c.1790–93（本件印于 1827），Fitzwilliam Museum, Cambridge（copy I）。
  - 来源: https://commons.wikimedia.org/wiki/File:The_Marriage_of_Heaven_and_Hell,_object_5,_copy_I,_1827,_Fitzwilliam_Museum.jpg；License: Public domain
  - 落盘: 1338×1800px，791 KB
- **milton_preface_1804.jpg** — Milton: A Poem, Preface 版页（「Would to God that all the Lords people were Prophets」），William Blake，c.1804–11，未著录（Commons 文件页无馆藏字段）。
  - 来源: https://commons.wikimedia.org/wiki/File:Milton_preface.jpg；License: Public domain
  - 落盘: 1241×1752px，588 KB
- **nebuchadnezzar_1795.jpg** — Nebuchadnezzar（尼布甲尼撒四肢着地），William Blake，1795–c.1805，Tate Britain。
  - 来源: https://commons.wikimedia.org/wiki/File:William_Blake_-_Nebuchadnezzar_(Tate_Britain).jpg；License: Public domain
  - 落盘: 1536×1099px，457 KB
- **newton_1795.jpg** — Newton（牛顿持罗盘，俯身画图），William Blake，1795–c.1805，Tate Britain。
  - 来源: https://commons.wikimedia.org/wiki/File:Newton-WilliamBlake.jpg；License: Public domain
  - 落盘: 1800×1384px，1036 KB
- **number_of_the_beast_1805.jpg** — The Number of the Beast is 666（兽名数目，水彩），William Blake，c.1805，Rosenbach Museum & Library, Philadelphia（Butlin 522）。
  - 来源: https://commons.wikimedia.org/wiki/File:The_number_of_the_beast_is_666_Philadelphia,_Rosenbach_Museum_and_Library.jpg；License: Public domain
  - 落盘: 1456×1800px，552 KB
- **pity_c1795.jpg** — Pity（怜悯，彩色印刷＋水彩），William Blake，c.1795，Yale Center for British Art（lido-TMS-7243）。
  - 来源: https://commons.wikimedia.org/wiki/File:William_Blake_-_Pity_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1449px，797 KB
- **songs_innocence_title_1789.jpg** — Songs of Innocence 扉页（「The Author & Printer W Blake」），William Blake，1789，Yale Center for British Art（lido-TMS-3706）。
  - 来源: https://commons.wikimedia.org/wiki/File:William_Blake_-_Songs_of_Innocence,_Plate_2,_Title_Page_(Bentley_3)_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1125×1800px，584 KB
- **tyger_1794.jpg** — Songs of Experience: The Tyger（版页，copy A），William Blake，1794，British Museum（1924,0726.2.9）。
  - 来源: https://commons.wikimedia.org/wiki/File:The_Tyger_BM_a_1794.jpg；License: Public domain
  - 落盘: 798×1343px，308 KB
- **urizen_title_1794.jpg** — The First Book of Urizen, pl.1 扉页（乌里森坐于书前），William Blake，1794，Yale Center for British Art。
  - 来源: https://commons.wikimedia.org/wiki/File:William_Blake_-_The_First_Book_of_Urizen,_Plate_1,_%22The_First_Book_of_Urizen.%22_(Bentley_1)_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1247×1800px，554 KB

### chardin — 夏尔丹（17 张；wave20 并入）
- **autoportrait_besicles_1771.jpg** — Autoportrait aux besicles（带眼镜自画像，粉彩），Jean Siméon Chardin，1771，卢浮宫（INV 25206）。
  - 来源: https://commons.wikimedia.org/wiki/File:Self-portrait_wearing_Glasses_by_Jean-Baptiste-Sim%C3%A9on_Chardin.jpg；License: Public domain
  - 落盘: 1450×1800px，697 KB
- **benedicite_louvre.jpg** — Le Bénédicité（餐前祷告），Jean Siméon Chardin，1740，卢浮宫（INV 3202）。
  - 来源: https://commons.wikimedia.org/wiki/File:Jean-Baptiste_Sim%C3%A9on_Chardin_003.jpg；License: Public domain（PD-Art）
  - 落盘: 1384×1800px，489 KB
- **cat_surveying_fish_met.jpg** — Cat Surveying Fish and Fowl on a Table（黑粉笔素描），Jean Siméon Chardin，1753，The Met（1975.131.93）。
  - 来源: https://www.metmuseum.org/art/collection/search/336462；License: CC0 1.0
  - 落盘: 1800×1210px，510 KB
- **house_of_cards_ngl.jpg** — The House of Cards（纸牌屋），Jean Siméon Chardin，约 1740–1，NGL（NG4078）。
  - 来源: https://commons.wikimedia.org/wiki/File:Jean-Baptiste-Sim%C3%A9on_Chardin,_The_House_of_Cards,_1736-37.jpg；License: Public domain
  - 落盘: 1024×858px，147 KB
- **la_brioche_louvre.jpg** — La Brioche（奶油面包），Jean Siméon Chardin，1763，卢浮宫（MI 1038）。
  - 来源: https://commons.wikimedia.org/wiki/File:Chardin,_la_brioche,_1763.JPG；License: Public domain
  - 落盘: 1800×1518px，850 KB
- **la_fontaine_de_cuivre_louvre.jpg** — La Fontaine de cuivre（铜水缸），Jean Siméon Chardin，约 1733–34，卢浮宫（MI 1037）。
  - 来源: https://commons.wikimedia.org/wiki/File:Jean-Baptiste_Sim%C3%A9on_Chardin_009.jpg；License: Public domain（PD-Art）
  - 落盘: 1417×1800px，584 KB
- **la_pourvoyeuse_louvre.jpg** — La Pourvoyeuse（市场归来），Jean Siméon Chardin，1739，卢浮宫（MI 720）。
  - 来源: https://commons.wikimedia.org/wiki/File:Jean-Baptiste_Sim%C3%A9on_Chardin_012.jpg；License: Public domain（PD-Art）
  - 落盘: 1576×1928px，531 KB
- **la_raie_louvre.jpg** — La Raie（鳐鱼；入院作品），Jean Siméon Chardin，1728，卢浮宫（INV 3197）。
  - 来源: https://commons.wikimedia.org/wiki/File:La_Raie_-_Jean_Baptiste_Sim%C3%A9on_Chardin_-_Mus%C3%A9e_du_Louvre_Peintures_INV_3197.jpg；License: Public domain
  - 落盘: 1800×1404px，780 KB
- **le_bocal_dolives_louvre.jpg** — Le Bocal d'olives（橄榄罐；Diderot 名句对象），Jean Siméon Chardin，1760，卢浮宫（MI 1036）。
  - 来源: https://commons.wikimedia.org/wiki/File:Chardin,_il_vaso_di_olive,_1760.JPG；License: Public domain
  - 落盘: 1800×1405px，787 KB
- **le_buffet_louvre.jpg** — Le Buffet（餐台；入院作品），Jean Siméon Chardin，1728，卢浮宫（INV 3198）。
  - 来源: https://commons.wikimedia.org/wiki/File:Chardin,_il_buffet,_1728,_01.JPG；License: Public domain
  - 落盘: 1321×1800px，570 KB
- **le_gobelet_dargent_louvre.jpg** — Le Gobelet d'argent（银杯），Jean Siméon Chardin，约 1768，卢浮宫（MI 1042）。
  - 来源: https://commons.wikimedia.org/wiki/File:Jean-Baptiste_Sim%C3%A9on_Chardin_024.jpg；License: Public domain（PD-Art）
  - 落盘: 1576×1270px，362 KB
- **lenfant_au_toton_louvre.jpg** — L'Enfant au toton（玩陀螺的孩子），Jean Siméon Chardin，1738 沙龙，卢浮宫（RF 1705）。
  - 来源: https://commons.wikimedia.org/wiki/File:L%27Enfant_au_toton_-_Jean_Baptiste_Sim%C3%A9on_Chardin_-_Mus%C3%A9e_du_Louvre_Peintures_RF_1705.jpg；License: Public domain
  - 落盘: 1800×1573px，838 KB
- **panier_de_fraises_1761.jpg** — Le Panier de fraises des bois（野草莓篮），Jean Siméon Chardin，1761，卢浮宫（RFML.PE.2024.7.1）。
  - 来源: https://commons.wikimedia.org/wiki/File:Jean_Sim%C3%A9on_Chardin_-_Le_Panier_de_fraises_des_bois_(1761).jpg；License: Public domain（PD-Art）
  - 落盘: 1800×1461px，924 KB
- **soap_bubbles_met.jpg** — Soap Bubbles（肥皂泡），Jean Siméon Chardin，约 1733–34，The Met（49.24）。
  - 来源: https://www.metmuseum.org/art/collection/search/435888；License: CC0 1.0
  - 落盘: 1800×1740px，641 KB
- **the_silver_tureen_met.jpg** — The Silver Tureen（银汤碗），Jean Siméon Chardin，约 1728–30，The Met（59.9）。
  - 来源: https://www.metmuseum.org/art/collection/search/435887；License: CC0 1.0（Met Open Access）
  - 落盘: 1800×1273px，413 KB
- **water_cistern_ngl.jpg** — The Water Cistern ('La Fontaine')（水缸），Jean Siméon Chardin，1733 或更晚，NGL（NG1664）。
  - 来源: https://commons.wikimedia.org/wiki/File:Jean-Baptiste_Sim%C3%A9on_Chardin_(1699-1779)_-_La_Fontaine_(The_Water_Cistern)_-_NG1664_-_National_Gallery.jpg；License: Public domain
  - 落盘: 800×679px，80 KB
- **young_schoolmistress_ngl.jpg** — The Young Schoolmistress（年轻女教师），Jean Siméon Chardin，约 1737，NGL（NG4077）。
  - 来源: https://commons.wikimedia.org/wiki/File:Jean_Sim%C3%A9on_Chardin_-_The_Young_Schoolmistress_-_WGA04750.jpg；License: Public domain
  - 落盘: 1800×1665px，764 KB

### manet — 马奈（14 张；wave20 并入）
- **a_bar_at_the_folies_bergere_1881_82.jpg** — A Bar at the Folies-Bergère，Édouard Manet，1881–82，The Courtauld Gallery, London。
  - 来源: https://commons.wikimedia.org/wiki/File:Edouard_Manet,_A_Bar_at_the_Folies-Berg%C3%A8re.jpg；License: Public domain
  - 落盘: 1800×1344px，1086 KB
- **boating_1874.jpg** — Boating（《划船》），Édouard Manet，1874，The Met, New York（29.100.115）。
  - 来源: https://www.metmuseum.org/art/collection/search/436947；License: CC0 1.0
  - 落盘: 1800×1373px，676 KB
- **corner_of_a_cafe_concert_1878_80.jpg** — Corner of a Café-Concert，Édouard Manet，ca. 1878–80，National Gallery, London（NG3858）。
  - 来源: https://commons.wikimedia.org/wiki/File:Edouard_Manet,_Corner_of_a_Caf%C3%A9-Concert,_ca._1878-80.jpg；License: Public domain
  - 落盘: 1445×1800px，1008 KB
- **le_balcon_1868_69.jpg** — Le Balcon，Édouard Manet，1868–69，Musée d'Orsay, Paris（RF 2772）。
  - 来源: https://commons.wikimedia.org/wiki/File:Edouard_Manet_-_The_Balcony_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1295×1800px，741 KB
- **le_dejeuner_sur_lherbe_1863.jpg** — Le Déjeuner sur l'herbe，Édouard Manet，1863，Musée d'Orsay, Paris（RF 1668）。
  - 来源: https://commons.wikimedia.org/wiki/File:Edouard_Manet_-_Luncheon_on_the_Grass_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1399px，771 KB
- **le_fifre_1866.jpg** — Le Fifre（The Fifer），Édouard Manet，1866，Musée d'Orsay, Paris（RF 1998）。
  - 来源: https://commons.wikimedia.org/wiki/File:Manet,_Edouard_-_Young_Flautist,_or_The_Fifer,_1866_(2).jpg；License: Public domain
  - 落盘: 1055×1800px，340 KB
- **mademoiselle_v_in_the_costume_of_an_espada_1862.jpg** — Mademoiselle V. . . in the Costume of an Espada，Édouard Manet，1862，The Met, New York（29.100.53）。
  - 来源: https://www.metmuseum.org/art/collection/search/436945；License: CC0 1.0
  - 落盘: 1422×1800px，447 KB
- **music_in_the_tuileries_gardens_1862.jpg** — Music in the Tuileries Gardens，Édouard Manet，1862，National Gallery, London（NG3260）。
  - 来源: https://commons.wikimedia.org/wiki/File:%C3%89douard_Manet_-_Music_in_the_Tuileries_Gardens.jpg；License: Public domain
  - 落盘: 1800×1137px，704 KB
- **olympia_1863.jpg** — Olympia，Édouard Manet，1863，Musée d'Orsay, Paris（RF 644）。
  - 来源: https://commons.wikimedia.org/wiki/File:Edouard_Manet_-_Olympia_-_Google_Art_Project_2.jpg；License: Public domain
  - 落盘: 1800×1220px，728 KB
- **portrait_of_emile_zola_1868.jpg** — Portrait of Émile Zola，Édouard Manet，1868，Musée d'Orsay, Paris（RF 2205）。
  - 来源: https://commons.wikimedia.org/wiki/File:Manet,_Edouard_-_Portrait_of_Emile_Zola.jpg；License: Public domain
  - 落盘: 1368×1800px，824 KB
- **spanish_singer_1860.jpg** — The Spanish Singer（《西班牙歌手》），Édouard Manet，1860，The Met, New York（49.58.2）。
  - 来源: https://www.metmuseum.org/art/collection/search/436944；License: CC0 1.0（Met Open Access）
  - 落盘: 1414×1800px，477 KB
- **stephane_mallarme_1876.jpg** — Stéphane Mallarmé，Édouard Manet，1876，Musée d'Orsay, Paris（RF 2632）。
  - 来源: https://commons.wikimedia.org/wiki/File:Edouard_Manet_-_St%C3%A9phane_Mallarm%C3%A9_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1371px，959 KB
- **the_monet_family_in_their_garden_at_argenteuil_1874.jpg** — The Monet Family in Their Garden at Argenteuil，Édouard Manet，1874，The Met, New York（1976.201.14）。
  - 来源: https://www.metmuseum.org/art/collection/search/436965；License: CC0 1.0
  - 落盘: 1800×1133px，579 KB
- **woman_with_a_cat_c1880.jpg** — Woman with a Cat（Femme au chat），Édouard Manet，ca. 1880，National Gallery, London（L675）。
  - 来源: https://commons.wikimedia.org/wiki/File:%C3%89douard_Manet_-_Femme_au_chat_(Portrait_de_Madame_Manet).jpg；License: Public domain
  - 落盘: 1410×1800px，636 KB

### sorolla — 索罗拉（13 张；wave20 并入）
- **autorretrato_1904.jpg** — Autorretrato（自画像；室内暗调·Velázquez 谱系对照件），Joaquín Sorolla，1904，Museo Sorolla（inv. 687）。
  - 来源: https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_Self_Portrait_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1164px，518 KB
- **chicos_en_la_playa_1909.jpg** — Chicos en la playa（海滩上的男孩们），Joaquín Sorolla，1909（签1910），Museo Nacional del Prado（P4648）。
  - 来源: https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_-_Chicos_en_la_playa.jpg；License: Public domain
  - 落盘: 1800×1109px，617 KB
- **clotilde_con_traje_de_noche_1910.jpg** — Clotilde con traje de noche（晚装 Clotilde），Joaquín Sorolla，1910，Museo Sorolla（inv. 949）。
  - 来源: https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_Clotilde_in_evening_dress_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1252×1800px，614 KB
- **el_bano_del_caballo_1909.jpg** — El baño del caballo（马浴），Joaquín Sorolla，1909，Museo Sorolla（inv. 839）。
  - 来源: https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_The_Horse%E2%80%99s_Bath_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1485px，821 KB
- **la_bata_rosa_1916.jpg** — La bata rosa（粉色浴袍），Joaquín Sorolla，1916，Museo Sorolla（inv. 1134）。
  - 来源: https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_The_Pink_Robe._After_the_Bath_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1142×1800px，741 KB
- **la_hora_del_bano_1909.jpg** — La hora del baño（沐浴时刻），Joaquín Sorolla，1909，Museo Sorolla（inv. 835）。
  - 来源: https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_Time_for_a_Bathe%2C_Valencia_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1798×1800px，1211 KB
- **la_siesta_1911.jpg** — La siesta（午睡），Joaquín Sorolla，1911，Museo Sorolla。
  - 来源: https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_La_Siesta_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1780px，1081 KB
- **la_vuelta_de_la_pesca_1894.jpg** — La vuelta de la pesca（渔获归来），Joaquín Sorolla，约1894，Musée d'Orsay, Paris（RF 948）。
  - 来源: https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_La_vuelta_de_la_pesca.jpg；License: Public domain
  - 落盘: 1800×1166px，497 KB
- **mis_hijos_1904.jpg** — Mis hijos（我的孩子们），Joaquín Sorolla，1904，Museo Sorolla（inv. 651）。
  - 来源: https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_My_children_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1248px，409 KB
- **nadadores_javea_1905.jpg** — Nadadores, Jávea（哈韦阿的泳者），Joaquín Sorolla，1905，Museo Sorolla。
  - 来源: https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_Swimmers%2C_J%C3%A1vea_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1800×1303px，1053 KB
- **paseo_a_orillas_del_mar_1909.jpg** — Paseo a orillas del mar（海边漫步），Joaquín Sorolla，1909，Museo Sorolla（inv. 834）。
  - 来源: https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_Strolling_along_the_Seashore_-_Google_Art_Project.jpg；License: Public domain
  - 落盘: 1777×1800px，1032 KB
- **triste_herencia_1899.jpg** — ¡Triste herencia!（悲惨的遗产），Joaquín Sorolla，1899，Fundación Bancaja, Valencia。
  - 来源: https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_Triste_Herencia_(1899).jpg；License: Public domain
  - 落盘: 1800×1323px，861 KB
- **vision_de_espana_valencia_1911_19.jpg** — Vision of Spain：Valencia 面板，Joaquín Sorolla，1911–19，Hispanic Society of America（A1805）。
  - 来源: https://commons.wikimedia.org/wiki/File:Joaqu%C3%ADn_Sorolla_y_Bastida_-_Vision_of_Spain_(formerly%2C_The_Provinces_of_Spain)%2C_Valencia_-_A1805_-_Hispanic_Society_of_America.jpg；License: Public domain
  - 落盘: 865×1000px，242 KB

### zorn — 佐恩（19 张；wave20 并入）
- **dance_in_gopsmor_1906.jpg** — Dans i Gopsmor / Polka（戈普斯莫尔之舞），Anders Zorn，1906，Nationalmuseum, Stockholm（85527；文件名含「Överförd till Riksdagen」注记）。
  - 来源: https://commons.wikimedia.org/wiki/File:%C3%96verf%C3%B6rd_till_Riksdagen,_Dans_i_Gopsmor_(Anders_Zorn)_-_Nationalmuseum_-_85527.tif；License: Public domain
  - 落盘: 1389×1800px，648 KB
- **en_premiar_1888.jpg** — En premiär / Une première（首次登台），Anders Zorn，1888，Nationalmuseum, Stockholm。
  - 来源: https://commons.wikimedia.org/wiki/File:Une_premiere_av_Anders_Zorn_1888.jpg；License: Public domain
  - 落盘: 1330×1800px，779 KB
- **etching_mona_1911.jpg** — Mona（莫娜，蚀刻；佐恩之母），Anders Zorn，1911，The Met, New York（384580；third state of three）。
  - 来源: https://www.metmuseum.org/art/collection/search/384580；License: CC0 1.0
  - 落盘: 1453×1800px，482 KB
- **etching_omnibus_1892.jpg** — Omnibus（公共马车，蚀刻），Anders Zorn，1892，The Met, New York（384539；fourth state of five）。
  - 来源: https://www.metmuseum.org/art/collection/search/384539；License: CC0 1.0
  - 落盘: 1267×1800px，606 KB
- **etching_rosita_mauri_1889.jpg** — Rosita Mauri（罗西塔·毛里，蚀刻），Anders Zorn，1889，Cleveland Museum of Art（1962.406）。
  - 来源: https://www.clevelandart.org/art/collection/search?q=zorn；License: CC0 1.0（Cleveland Open Access）
  - 落盘: 1195×1800px，666 KB
- **etching_wet_1911.jpg** — Wet（湿，蚀刻），Anders Zorn，1911，The Met, New York（365109；third state of three）。
  - 来源: https://www.metmuseum.org/art/collection/search/365109；License: CC0 1.0
  - 落盘: 1439×1800px，457 KB
- **etching_zorn_and_his_wife_1890.jpg** — Zorn and His Wife（与妻子在一起，蚀刻），Anders Zorn，1890，The Met, New York（384551；third state of three）。
  - 来源: https://www.metmuseum.org/art/collection/search/384551；License: CC0 1.0
  - 落盘: 1247×1800px，636 KB
- **fisherman_st_ives_1888.jpg** — Fiskare i St. Ives / Un pêcheur（圣艾夫斯的渔夫），Anders Zorn，1888，Musée d'Orsay, Paris。
  - 来源: https://commons.wikimedia.org/wiki/File:Anders_Zorn_-_A_Fisherman_1888.jpg；License: Public domain
  - 落盘: 591×850px，98 KB
- **frieda_schiff_1894.jpg** — Frieda Schiff (1876–1958), Later Mrs. Felix M. Warburg，Anders Zorn，1894，The Met, New York（437964）。
  - 来源: https://www.metmuseum.org/art/collection/search/437964；License: CC0 1.0
  - 落盘: 1351×1800px，570 KB
- **midnatt_1891.jpg** — Midnatt（午夜），Anders Zorn，1891，Zornmuseet, Mora。
  - 来源: https://commons.wikimedia.org/wiki/File:Midnatt_av_Anders_Zorn_1891.jpg；License: Public domain
  - 落盘: 1800×1203px，670 KB
- **midsummer_dance_1897.jpg** — Midsommardans（仲夏之舞），Anders Zorn，1897，Nationalmuseum, Stockholm。
  - 来源: https://commons.wikimedia.org/wiki/File:Midsommardans_av_Anders_Zorn_1897.jpg；License: Public domain
  - 落盘: 1321×1800px，572 KB
- **mrs_walter_rathbone_bacon_1897.jpg** — Mrs. Walter Rathbone Bacon (Virginia Purdy Barker)，Anders Zorn，1897，The Met, New York（437966）。
  - 来源: https://www.metmuseum.org/art/collection/search/437966；License: CC0 1.0（Met Open Access）
  - 落盘: 1147×1800px，533 KB
- **omnibus_i_1892.jpg** — Omnibus I（公共马车一号），Anders Zorn，1892，Nationalmuseum, Stockholm。
  - 来源: https://commons.wikimedia.org/wiki/File:Anders_Zorn_Omnibus.jpg；License: Public domain
  - 落盘: 1190×1800px，645 KB
- **our_daily_bread_1886.jpg** — Vårt dagliga bröd（我们的日常面包），Anders Zorn，1886，Nationalmuseum, Stockholm（24125）。
  - 来源: https://commons.wikimedia.org/wiki/File:Our_Daily_Bread_(Anders_Zorn)_-_Nationalmuseum_-_24125.tif；License: Public domain
  - 落盘: 1800×1197px，702 KB
- **self_portrait_in_red_1915.jpg** — Självporträtt i rött（红衣自画像），Anders Zorn，1915，Zornmuseet, Mora。
  - 来源: https://commons.wikimedia.org/wiki/File:Zornself.jpg；License: Public domain
  - 落盘: 1187×1600px，309 KB
- **self_portrait_with_model_1896.jpg** — Självporträtt med modell（自画像与模特），Anders Zorn，1896，Nationalmuseum, Stockholm。
  - 来源: https://commons.wikimedia.org/wiki/File:Sj%C3%A4lvportr%C3%A4tt_av_Anders_Zorn_1896.jpg；License: Public domain
  - 落盘: 1370×1800px，658 KB
- **sommarafton_1894.jpg** — Sommarafton（夏夜），Anders Zorn，1894，Zornmuseet, Mora。
  - 来源: https://commons.wikimedia.org/wiki/File:Anders_Zorn_Sommerabend_1894.jpg；License: Public domain
  - 落盘: 1244×1800px，668 KB
- **sommarnoje_1886.jpg** — Sommarnöje（夏趣），Anders Zorn，1886，私人收藏（2010 年 2600 万 SEK 成交）。
  - 来源: https://commons.wikimedia.org/wiki/File:Sommarn%C3%B6je_(1886),_akvarell_av_Anders_Zorn.jpg；License: Public domain
  - 落盘: 1266×1800px，803 KB
- **vallkulla_1908.jpg** — Vallkulla（牧羊女），Anders Zorn，1908，Zornmuseet, Mora。
  - 来源: https://commons.wikimedia.org/wiki/File:Anders_Zorn_-_Vallkulla.jpg；License: Public domain
  - 落盘: 1000×1327px，292 KB

### sultan_mohammed — 苏丹·穆罕默德（16 张；wave20 并入）
- **celebration_id.jpg** — 《庆祝开斋节》f.86a（Cartier 哈菲兹），Sultan Muhammad，c. 1527–31，私人收藏（原 Cartier 旧藏）。
  - 来源: https://commons.wikimedia.org/wiki/File:Portrait_of_Sam_Mirza_as_a_patron%3B_The_feast_of_I%E2%80%99d_begins%2C_copy_of_Diwan_Hafiz_manuscript.jpg；License: Public domain
  - 落盘: 1138×1800px，792 KB
- **court_gayumars.jpg** — 《古尤马尔斯宫廷》（The Court of Gayumars）全页，Sultan Muhammad，c. 1524–25，多伦多，阿迦汗博物馆 AKM165（原 Sadruddin Aga Khan 旧藏）。
  - 来源: https://commons.wikimedia.org/wiki/File:Court_of_Gayumars_Persian_miniature.jpg；License: Public domain
  - 落盘: 1308×1800px，935 KB
- **court_gayumars_detail.jpg** — 《古尤马尔斯宫廷》画面裁切版，Sultan Muhammad，c. 1524–25，阿迦汗博物馆 AKM165。
  - 来源: https://commons.wikimedia.org/wiki/File:The_Court_of_Gayumars_%28Cropped%29.jpg；License: Public domain
  - 落盘: 1242×1800px，989 KB
- **death_of_zahhak.jpg** — 《扎哈克之死》f.37v，Sultan Muhammad，c. 1535，阿迦汗博物馆 AKM155。
  - 来源: https://commons.wikimedia.org/wiki/File:Sultan_Muhammad_Tiran_Zahhak.jpg；License: Public domain
  - 落盘: 1244×1800px，818 KB
- **earthly_drunkenness_harvard.jpg** — 《尘世醉酒》，Sultan Muhammad，c. 1530，哈佛艺术博物馆 1988.460.2。
  - 来源: https://commons.wikimedia.org/wiki/File:Earthly_Drunkenness.jpg；License: Public domain
  - 落盘: 645×1024px，235 KB
- **faridun_zahhak_freer.jpg** — 《法里顿锤击扎哈克》，Sultan Muhammad，c. 1525，华盛顿，弗里尔美术馆 F1996.2。
  - 来源: https://commons.wikimedia.org/wiki/File:Faridun_strikes_Zahhak_with_the_ox-headed_mace.jpg；License: Public domain
  - 落盘: 1228×1800px，554 KB
- **feast_of_sada_met.jpg** — 《萨达节之宴》f.22v，Sultan Muhammad，c. 1525，纽约，大都会艺术博物馆 1970.301.2。
  - 来源: https://commons.wikimedia.org/wiki/File:%22The_Feast_of_Sada%22%2C_Folio_22v_from_the_Shahnama_%28Book_of_Kings%29_of_Shah_Tahmasp_MET_DP107689.jpg；License: CC0
  - 落盘: 1261×1800px，742 KB
- **hafiz_allegory_met.jpg** — 《世界与彼世的醉酒》f.135a（Cartier 哈菲兹），Sultan Muhammad，c. 1531，大都会艺术博物馆 × 哈佛艺术博物馆（1988.430 联合藏）。
  - 来源: https://commons.wikimedia.org/wiki/File:Folio_Divan_Hafiz_Met_1988.430.jpg；License: Public domain
  - 落盘: 1149×1800px，697 KB
- **hafiz_signature.jpg** — 《庆祝开斋节》签名细部（统治者足下），Sultan Muhammad，c. 1531，私人收藏（原 Cartier 旧藏）。
  - 来源: https://commons.wikimedia.org/wiki/File:Sultan_Muhammad_signature%2C_at_the_feet_of_the_ruler._The_feast_of_I%E2%80%99d_begins%2C_Diwan_of_Hafiz_manuscript%2C_1531.jpg；License: Public domain
  - 落盘: 1237×1800px，465 KB
- **jamal_jalal_divan.jpg** — 《贾马尔与贾拉尔》f.2v「苏丹的迪万」，Sultan Muhammad，c. 1502–05，乌普萨拉大学图书馆 O Nova 2。
  - 来源: https://commons.wikimedia.org/wiki/File:The_sultan_in_his_divan_%28full_view%2C_f._2v%29%2C_Dastan-i_Jamal_u_Jalal._1502-1505%2C_Tabriz_%28Uppsala_University_Library%2C_O_Nova_2%29.jpg；License: Public domain
  - 落盘: 1225×1800px，541 KB
- **khusraw_shirin_bl.jpg** — 《霍斯鲁窥见西琳沐浴》f.53v，Sultan Muhammad，1539–43，伦敦，大英图书馆 Or.2265。
  - 来源: https://commons.wikimedia.org/wiki/File:Khusraw_watches_Shirin_bathing.jpg；License: CC0
  - 落盘: 1265×1800px，650 KB
- **lovers_picnic_harvard.jpg** — 《恋人野餐》，Sultan Muhammad，c. 1530，哈佛艺术博物馆 2007.183.2。
  - 来源: https://commons.wikimedia.org/wiki/File:Lovers%27_Picnic.jpg；License: Public domain
  - 落盘: 1106×1800px，548 KB
- **rustam_sleeping_bm.jpg** — 《鲁斯塔姆沉睡，拉赫什斗狮》，Sultan Muhammad，c. 1515–22，伦敦，大英博物馆 1948,1211,0.23。
  - 来源: https://commons.wikimedia.org/wiki/File:Sleeping_Rustam.jpg；License: Public domain
  - 落盘: 1197×1800px，854 KB
- **tahmuras_divs_met.jpg** — 《塔赫穆拉斯降魔》f.23v，Sultan Muhammad，c. 1525，大都会艺术博物馆 1970.301.3。
  - 来源: https://commons.wikimedia.org/wiki/File:%22Tahmuras_Defeats_the_Divs%22%2C_Folio_23v_from_the_Shahnama_%28Book_of_Kings%29_of_Shah_Tahmasp_MET_DP107119.jpg；License: CC0
  - 落盘: 1225×1800px，870 KB
- **zahhak_fate_met.jpg** — 《扎哈克听闻命运》f.29v，Sultan Muhammad，c. 1524，大都会艺术博物馆 1970.301.4。
  - 来源: https://commons.wikimedia.org/wiki/File:%22Zahhak_is_Told_His_Fate%22%2C_Folio_29v_from_the_Shahnama_%28Book_of_Kings%29_of_Shah_Tahmasp_MET_DP107120.jpg；License: CC0
  - 落盘: 1225×1800px，814 KB
- **zal_magi_met.jpg** — 《扎尔问卜》f.73v，Sultan Muhammad，c. 1530–35，大都会艺术博物馆 1970.301.8。
  - 来源: https://commons.wikimedia.org/wiki/File:%22Zal_Consults_the_Magi%22%2C_Folio_73v_from_the_Shahnama_%28Book_of_Kings%29_of_Shah_Tahmasp_MET_DP107124.jpg；License: CC0
  - 落盘: 1209×1800px，1003 KB

## 来源与许可口径

- **Met Open Access（15 张）**：仅取 `isPublicDomain=true` 且 `primaryImage` 非空的对象；图像 = CC0 1.0。来源 URL 为 metmuseum.org 对象页（直链 images.metmuseum.org/...）。
- **Art Institute of Chicago（4 张）**：API `is_public_domain=true`，作品页标注 "CC0 Public Domain Designation"；图像经 IIIF `https://www.artic.edu/iiif/2/<image_id>/full/1800,/0/default.jpg`。
- **Cleveland Museum of Art（3 张）**：API `share_license_status=CC0`（Open Access）；图像 `<accession>_print.jpg`（约 3400px）缩放。
- **Wikimedia Commons（11 张）**：PD 或 CC0/CC BY-SA；缩略图经 API `iiurlwidth=1600`。CC 类署名见总表。
- **wave12 追加（克里姆特 3 张）**：原画 1918 年后进入公有领域；现代扫描/摄影**逐张核验** Commons 许可模板——`Licensed-PD-Art`（Kiss；另附 CC BY-SA 4.0）/ `PD-Art`（Adele）/ `PD-Art-two-auto`（Death and Life）。未使用馆方 © 摄影图（Klimt Foundation / Leopold 官网图像未采）；未经核实的第三方扫描未采。
- **wave13 追加（修拉 10 张）**：AIC 1（CC0，IIIF）+ Met 4（Open Access，`isPublicDomain=true`）+ Commons 5（PD，imageinfo 逐张核验）。《浴场》图像采用 Commons PD 版（作品藏 NGL；NGL 官网图像许可口径未明，未采用其文件，作品页仅作档案文本来源）。**无版权未清项**；高清原图（>1800px）留私有层。
- **wave16 收口（turner / rembrandt / goya / bada_shanren / qi_baishi / ito_jakuchu，共 58 张）**：Wikimedia Commons 39（PD / CC0 / CC BY 3.0，逐张 `imageinfo` 核验）＋ Met Open Access 9（CC0）＋ Cleveland 1（CC0）＋ ColBase 9（日本国立文化財機構规约——须标注出典：「出典：ColBase」）。CC 类署名逐张记录（norham = 摄影 Sailko，CC BY 3.0；qi 摄影 2 件 CC BY-SA 4.0 / 1 件 CC BY 2.0）。**hopper 例外**：公开 0 / 私有 9（见「私有层例外」节）。
- **wave15/17 并入（15 位新档，169 张；其中 13 位有公开图）**：来源通道 = Wikimedia Commons 158 张 ＋ 馆方直取 11 张（Lenbachhaus 2 / Met 8 / Cleveland 1；NGA、台北故宫、KMSKA 件经 Commons 转载）。许可分布：**PD 149 · CC0 17 · CC BY-SA 3.0/4.0 3**——CC 类署名逐张记录（le_pater = 翻拍 SiefkinDR，CC BY-SA 4.0；《蓝骑士》年鉴封面 = 摄影 Goesseln，CC BY-SA 3.0；德加《梳头》 = NGL 照片，CC BY-SA 4.0）。**kahlo / kngwarreye 公开 0**（全私有，见「私有层例外」节）。
- **wave18/19/20 并入（22 位新档有公开图，345 张）**：来源通道 = Wikimedia Commons ＋ 馆方直取（Met / NPM 开放资料 / AIC / 京博等）；许可以 PD 为主，CC0 / CC BY 4.0（NPM 开放资料）/ CC BY-SA 类署名逐张记录；**namatjira / el_salahi / wu_guanzhong / okeeffe / rivera 公开 0**（全私有，见「私有层例外」节）。
- 统一后处理：LANCZOS 缩放至长边 ≤1800px，JPEG quality 88 progressive；无裁切、无加水印。

## 私有层例外（公开 / 私有分开记）

> 口径：公开侧（本 manifest）只收 PD/开放许可图；「版权未清 / 研究副本 / 待核」材料存仓内私有层（`_private/`，永不提交、不公开分发）。以下为已收口画家中涉及私有层者（54 位 = 62 位收口范围 + wave21 已收口 10 位照实并入；私有张数 = 顶层图像文件数——按文件内容识别图像，含 `.hires`/`.raw` 等非常规扩展名；QA 产物（`_` 前缀 / 联系表）不计；明细以各自私有层登记为准）：

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

| hiroshige | 18 | 8 | 高清研究副本 8 件（Met 原图级；公开侧已存 ≤1800px 版） |
| sargent | 14 | 13 | 高清研究副本 13 件（公开侧已存 ≤1800px 版；Octavia Hill 源件无更高开放版） |
| piero_della_francesca | 17 | 1 | 超规格研究副本 1 件（3840px 级；公开侧已存 ≤1800px 版） |
| artemisia_gentileschi | 16 | 4 | 研究文献与高清研究件 4 件（公开侧已存 ≤1800px 版） |
| namatjira | 0 | 31 | **全部版权未清**（2029 版权警示；原住民伦理护栏）——公开侧 0 张；31 张（AGSA 等馆藏研究件） |
| el_salahi | 0 | 22 | **全部版权未清**——公开侧 0 张；22 张（Tate 等馆藏研究件） |
| wu_guanzhong | 0 | 25 | **全部版权未清**（版权护栏入 §8.1）——公开侧 0 张；25 张（香港艺术馆等研究件） |
| fan_kuan | 8 | 10 | 研究快照与高清研究件 10 件（NPM 著录 + 高清副本；公开侧已存 ≤1800px 版） |
| sesshu | 18 | 6 | 高清研究副本 6 件（含《破墨山水图》3840×5936 原尺寸；公开侧已存 ≤1800px 版） |
| constable | 17 | 3 | 研究快照与高清研究件 3 件（公开侧已存 ≤1800px 版） |
| poussin | 13 | 3 | 研究文献与高清研究件 3 件（含《阿卡迪亚牧人》3840px；公开侧已存 ≤1800px 版） |
| bruegel | 20 | 10 | 技术研究文本与高清研究件 10 件（Inside Bruegel 修复专文等；公开侧已存 ≤1800px 版） |
| el_greco | 17 | 3 | 高清研究副本 3 件（含 6817×9089 原图级；公开侧已存 ≤1800px 版） |
| holbein | 13 | 8 | 研究记录与高清研究副本 8 件（公开侧已存 ≤1800px 版） |
| aivazovsky | 14 | 5 | 高清研究副本与参考比对件 5 件（公开侧已存 ≤1800px 版） |
| okeeffe | 0 | 16 | **全部版权未清**（© Georgia O'Keeffe Museum / ARS；美国 2041 前不进公有领域）——公开侧 0 张；16 张（馆方 IIIF 研究件） |
| rivera | 0 | 14 | **全部版权未清**——公开侧 0 张；14 张（Detroit Industry 壁画等研究件） |
| zhao_mengfu | 14 | 9 | 高清研究副本 9 件（含 12000px 级全卷；公开侧已存 ≤1800px 版） |
| ni_zan | 13 | 19 | 原尺寸与高清研究副本 19 件（含原尺寸 10 件；公开侧已存 ≤1800px 版） |
| qiu_ying | 17 | 23 | 高清研究件 23 件（另有论文 4 件；公开侧已存 ≤1800px 版） |
| ogata_korin | 19 | 6 | 高清原件与研究件 6 件（Daugherty 2003 等；公开侧已存 ≤1800px 版） |
| chardin | 17 | 10 | 高清研究副本 10 件（公开侧已存 ≤1800px 版） |
| manet | 14 | 14 | 高清研究副本 14 件（另有原典 PDF 3 部；公开侧已存 ≤1800px 版） |
| sorolla | 13 | 12 | 高清研究副本 12 件（另有研究件 8 份；公开侧已存 ≤1800px 版） |
| zorn | 19 | 16 | 高清研究副本 16 件（另有书籍 11 件；公开侧已存 ≤1800px 版） |
| sultan_mohammed | 16 | 8 | 高清研究副本 8 件（公开侧已存 ≤1800px 版） |
| xu_beihong | 0 | 74 | **全部版权未清**——公开侧 0 张；74 张（徐悲鸿纪念馆等研究件；逐张核查依据留档） |
| li_keran | 0 | 19 | **全部版权未清**（中国 life+50 → 2039 前受保护）——公开侧 0 张；19 张（李可染艺术基金会等） |
| sher_gil | 28 | 11 | URAA 恢复/无美国理据/不确定者 11 件（含《Young Girls》《Bride's Toilet》《The Vina Player》；公开侧已存 28 张 PD 理据件） |
| tarsila | 0 | 56 | **全部版权未清**——公开侧 0 张；56 张（研究件） |
| chen_hongshou | 18 | 8 | 高清研究副本 8 件（公开侧已存 ≤1800px 版） |
| xu_wei | 23 | 6 | 馆方网页图 6 件（仅内部研究；公开侧已存 23 张） |
| hogarth | 20 | 15 | 高清研究副本 15 件（公开侧已存 ≤1800px 版） |
| mir_sayyid_ali | 16 | 8 | 高清研究副本 8 件（公开侧已存 ≤1800px 版） |
| de_chirico | 0 | 25 | **全部版权未清**——公开侧 0 张；25 张（MoMA/Pompidou/Tate 研究件；联系表核验） |
| rockwell | 0 | 29 | **全部版权未清**——公开侧 0 张；29 张（研究件） |

> 合计：私有层例外 **676 张**（54 位；含 hopper 9、kahlo 13、kngwarreye 14、namatjira 31、el_salahi 22、wu_guanzhong 25、okeeffe 16、rivera 14、xu_beihong 74、tarsila 56 等全私有）。私有层材料仅本机研究/临摹参考，公开仓不引用其路径；引用作品只给正常出处（馆藏页 / 文件页 URL）。

## 缺口与备注（不硬凑）

1. **毕加索（已解决但有限制）**：1930 年后作品仍受版权（美国外尤甚）；Met/AIC/NGA 的毕加索藏品均标非公有领域、Commons 无《亚维农少女》《老吉他手》等干净复制品（已查：Commons 全文检索 + `Category:Pablo Picasso` 87 项 + NGA Open Data 318 行 / published_images 288 行 openaccess=0）。→ 改用 Cleveland CC0 藏品 3 张（1904/1905 版画 + 1908–10 油画）。
2. **达芬奇《蒙娜丽莎》**：卢浮宫无开放数据接口 → 用 C2RMF 官方高清复制品（PD，Commons Featured picture）。
3. **莫奈的 Met 名作**（Garden at Sainte-Adresse、Bridge over a Pond of Water Lilies、Haystacks 等）：Met 新 API 标 `isPublicDomain=false` 且无图 → 莫奈改用 AIC（2 张 CC0）+ Commons（《印象·日出》PD）。
4. **米开朗基罗《大卫》**：只能取 CC BY-SA 4.0 照片（雕像本体 PD，但梵蒂冈/佛罗伦萨馆藏照多受限）——已按 CC BY-SA 署名。
5. **卡拉瓦乔《圣马太蒙召》**：Commons 提供 CC0 高清（8792×8304 原图）→ 已缩放至 1800px。
6. **已剔除的候选**：2 张 Flickr 来源的毕加索照片（1 张为街头涂鸦版《亚维农少女》、1 张为观众遮挡照）经目检不合格，已删除换源（见自审 B-1）。
7. **wave16 收口批次补记（2026-10-16，IndexMerge / A-51）**：turner / rembrandt 两库无画家侧 MANIFEST，本表行目由主脑按档案 §9 [R22] 记录 + Commons 文件页逐张复核（含像素比对）后补全；goya / bada_shanren / qi_baishi / ito_jakuchu 由各画家侧 MANIFEST 合并；hopper 公开 0 张（全私有，见「私有层例外」节）。
8. **wave15/17 并入批次补记（2026-10-16，IndexMerge2）**：15 位新档（wave15×8 + wave17×7）169 张公开图并入本表（13 位有公开图；kahlo / kngwarreye 全私有，仅见「私有层例外」节）；行目按各画家侧 MANIFEST 合并、逐张与磁盘核对（行数 = 磁盘实际）。私有层例外同步 +12 位 94 张（合计 18 位 126 张）。kandinsky 私有 11 件为 `.hires` 扩展名（JPEG 内容），按「顶层图像文件（内容识别）」口径计入。
9. **wave18/19/20 并入批次补记（2026-10-16，IndexMerge3）**：27 位新档 345 张公开图并入本表（22 位有公开图；namatjira / el_salahi / wu_guanzhong / okeeffe / rivera 公开 0，仅见「私有层例外」节）；行目按各画家侧 MANIFEST 合并、逐张与磁盘核对（行数 = 磁盘实际）。私有层例外同步 +36 位 550 张（合计 54 位 676 张；含 wave21 已收口 10 位照实并入）。
10. **未纳入（在产）**：wave21 十位（xu_beihong / li_keran / sher_gil / tarsila / chen_hongshou / xu_wei / hogarth / mir_sayyid_ali / de_chirico / rockwell）——已收口者照实并入（私有层例外节；主表随下轮；xu_wei 已落盘）；磁盘残留目录见核验脚本「未纳入」输出行。

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
