# connectomic-paper-datasets
Collection of connectomic papers and datasets.
Public available annotated EM datasets with papers and download paths are in [connectomic-datasets.xlsx](https://github.com/Levishery/connectomic-paper-datasets/tree/main/connectomic-datasets.xlsx). Please tell me if any dataset is missing.

Recommended code: a deep learning framework powered by PyTorch for automatic and semi-automatic semantic and instance segmentation in connectomics, which is called [PyTorch Connectomics (PyTC)](https://github.com/zudi-lin/pytorch_connectomics). [[paper](https://arxiv.org/abs/2112.05754)]

## Important Papers
### MICrONS Cell 2022
- **Multiscale and multimodal reconstruction of cortical structure and function**
[[Paper](https://www.biorxiv.org/content/10.1101/2020.10.14.338681v2.full.pdf)]
[[Dataset](https://www.microns-explorer.org/)]
[[Neuroglancer](https://ngl.microns-explorer.org/#!%7B%22dimensions%22:%7B%22x%22:%5B4e-9%2C%22m%22%5D%2C%22y%22:%5B4e-9%2C%22m%22%5D%2C%22z%22:%5B4e-8%2C%22m%22%5D%7D%2C%22position%22:%5B255109.53125%2C183187.046875%2C22258.5%5D%2C%22crossSectionScale%22:1.9075602118137613%2C%22projectionOrientation%22:%5B0.04550134390592575%2C-0.0007258548284880817%2C-0.007786378730088472%2C0.9989336729049683%5D%2C%22projectionScale%22:227699.57371186817%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%7B%22url%22:%22precomputed://https://bossdb-open-data.s3.amazonaws.com/iarpa_microns/minnie/minnie65/em%22%2C%22subsources%22:%7B%22default%22:true%7D%2C%22enableDefaultSubsources%22:false%7D%2C%22tab%22:%22source%22%2C%22shaderControls%22:%7B%22normalized%22:%7B%22range%22:%5B86%2C172%5D%7D%7D%2C%22name%22:%22img65%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%7B%22url%22:%22precomputed://https://bossdb-open-data.s3.amazonaws.com/iarpa_microns/minnie/minnie35/em%22%2C%22subsources%22:%7B%22default%22:true%7D%2C%22enableDefaultSubsources%22:false%7D%2C%22tab%22:%22source%22%2C%22shaderControls%22:%7B%22normalized%22:%7B%22range%22:%5B112%2C172%5D%7D%7D%2C%22name%22:%22img35%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22precomputed://gs://iarpa_microns/minnie/minnie65/seg%22%2C%22tab%22:%22segments%22%2C%22annotationColor%22:%22#8f8f8a%22%2C%22selectedAlpha%22:0.41%2C%22notSelectedAlpha%22:0.06%2C%22segments%22:%5B%22864691135099901728%22%2C%22864691135207735929%22%2C%22864691135334584297%22%2C%22864691135358985048%22%2C%22864691135415666362%22%2C%22864691135609594119%22%2C%22864691135761634358%22%2C%22864691135855890478%22%2C%22864691135974639471%22%2C%22864691136039640318%22%2C%22864691137019596142%22%5D%2C%22segmentQuery%22:%22864691135207735929%2C%20864691136194248918%2C%20864691135517422218%2C%20864691135753932237%2C%20%20%20%20%20%20%20%20864691135367058169%2C%20864691135293126156%2C%20864691136108768952%2C%20%20%20%20%20%20%20%20864691135974639471%2C%20864691135953898760%2C%20864691136116205476%2C%20%20%20%20%20%20%20%20864691135609687047%2C%20864691136951664863%2C%20864691136008689326%2C%20%20%20%20%20%20%20%20864691136023889209%2C%20864691135564752471%2C%20864691136011067043%2C%20%20%20%20%20%20%20%20864691136378815445%2C%20864691135584074360%2C%20864691137019596142%2C%20%20%20%20%20%20%20%20864691136903144370%2C%20864691135809608652%2C%20864691136227020113%2C%20%20%20%20%20%20%20%20864691135888577417%2C%20864691135440543560%2C%20864691135865773189%2C%20%20%20%20%20%20%20%20864691135367033849%2C%20864691135117980637%2C%20864691135583884664%2C%20%20%20%20%20%20%20%20864691135718541617%2C%20864691135099901728%2C%20864691135385422677%2C%20%20%20%20%20%20%20%20864691134884807418%2C%20864691135272206865%2C%20864691135617953423%2C%20%20%20%20%20%20%20%20864691135593659947%2C%20864691135700409211%2C%20864691135233242713%2C%20%20%20%20%20%20%20%20864691135975633475%2C%20864691135508879113%2C%20864691136084313196%2C%20%20%20%20%20%20%20%20864691136023980601%2C%20864691135776732256%2C%20864691136811995507%2C%20%20%20%20%20%20%20%20864691135337845734%2C%20864691135382556378%2C%20864691135358985048%2C%20%20%20%20%20%20%20%20864691136436509342%2C%20864691135782544435%2C%20864691135334584297%2C%20%20%20%20%20%20%20%20864691135815579983%2C%20864691136108938168%2C%20864691135975539779%2C%20%20%20%20%20%20%20%20864691135848030814%2C%20864691135952122147%2C%20864691135761634358%2C%20%20%20%20%20%20%20%20864691135497743635%2C%20864691135564739159%2C%20864691135517531786%2C%20%20%20%20%20%20%20%20864691136903228594%2C%20864691135915343462%2C%20864691135462420637%2C%20%20%20%20%20%20%20%20864691135775906989%2C%20864691136925601354%2C%20864691135415666362%2C%20%20%20%20%20%20%20%20864691136378859477%2C%20864691136309871706%2C%20864691135884023664%2C%20%20%20%20%20%20%20%20864691135937286404%2C%20864691136812081779%2C%20864691135609594119%2C%20%20%20%20%20%20%20%20864691135761725238%2C%20864691135724393131%2C%20864691134988722810%2C%20%20%20%20%20%20%20%20864691136209328060%2C%20864691135855890478%2C%20864691136227167569%2C%20%20%20%20%20%20%20%20864691135953985800%2C%20864691136039640318%2C%20864691134988768122%22%2C%22colorSeed%22:3123229499%2C%22name%22:%22seg65%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22precomputed://gs://minnie35_2020_meshed_seg/neuroglancer/seg/minnie35%22%2C%22tab%22:%22source%22%2C%22annotationColor%22:%22#979795%22%2C%22selectedAlpha%22:0.41%2C%22notSelectedAlpha%22:0.06%2C%22colorSeed%22:1012597943%2C%22name%22:%22seg35%22%7D%5D%2C%22showSlices%22:false%2C%22selectedLayer%22:%7B%22visible%22:true%2C%22layer%22:%22seg65%22%7D%2C%22layout%22:%7B%22type%22:%22xy-3d%22%2C%22orthographicProjection%22:true%7D%7D)]

### H01 preprint
- **A connectomic study of a petascale fragment of human cerebral cortex**
[[Paper](https://www.biorxiv.org/content/10.1101/2021.05.29.446289v4)]
[[Dataset](https://h01-release.storage.googleapis.com/data.html)]
[[Neuroglancer](https://h01-dot-neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22x%22:%5B8e-9%2C%22m%22%5D%2C%22y%22:%5B8e-9%2C%22m%22%5D%2C%22z%22:%5B3.3e-8%2C%22m%22%5D%7D%2C%22crossSectionScale%22:2.74318246533235%2C%22projectionOrientation%22:%5B0.48089489340782166%2C-0.5692054033279419%2C0.13241595029830933%2C-0.6536140441894531%5D%2C%22projectionScale%22:8651.330411012967%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%22precomputed://gs://h01-release/data/20210601/4nm_raw%22%2C%22tab%22:%22source%22%2C%22name%22:%224nm%20EM%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%7B%22url%22:%22precomputed://gs://h01-release/data/20210601/c3%22%2C%22subsources%22:%7B%22default%22:true%2C%22bounds%22:true%2C%22properties%22:true%2C%22mesh%22:true%7D%2C%22enableDefaultSubsources%22:false%7D%2C%22panels%22:%5B%7B%22flex%22:1.55%2C%22tab%22:%22segments%22%7D%5D%2C%22segments%22:%5B%2212857642016%22%2C%2213046505828%22%2C%2213951650786%22%2C%2214794814799%22%2C%2215539757452%22%2C%222120664699%22%2C%2221348269172%22%2C%2221635455184%22%2C%2222948012913%22%2C%2227216368299%22%2C%2228104985461%22%2C%2228862498148%22%2C%2229210178754%22%2C%222950980117%22%2C%2229672577804%22%2C%2229730222317%22%2C%2229977680734%22%2C%2230224642109%22%2C%2230501462297%22%2C%2230516077733%22%2C%2230573824944%22%2C%2230588382028%22%2C%2230605127877%22%2C%2230865392105%22%2C%2230941549387%22%2C%2231068084020%22%2C%223106947392%22%2C%2231082523968%22%2C%2231083559920%22%2C%2231140649483%22%2C%2231274759074%22%2C%2231349195650%22%2C%2231576899712%22%2C%2231591499830%22%2C%2232385180272%22%2C%223296832824%22%2C%2233049905842%22%2C%223308836336%22%2C%2233269227364%22%2C%2233544164420%22%2C%2233663789818%22%2C%2233779853124%22%2C%2233779985123%22%2C%223512752660%22%2C%223513951463%22%2C%223588284587%22%2C%223631312996%22%2C%223645170418%22%2C%2237626413608%22%2C%223773716567%22%2C%223788376389%22%2C%223788551051%22%2C%223790844645%22%2C%223833230503%22%2C%2238611762212%22%2C%2238660748322%22%2C%2238689468673%22%2C%223907682045%22%2C%223937466277%22%2C%223949920978%22%2C%2239540618731%22%2C%223994337380%22%2C%224006748353%22%2C%224068088366%22%2C%224079680017%22%2C%224094078022%22%2C%224094501608%22%2C%224127236696%22%2C%224140858954%22%2C%224152247000%22%2C%224152861452%22%2C%224153108523%22%2C%224154686065%22%2C%224185377684%22%2C%2241933255298%22%2C%2242002712851%22%2C%2242108919642%22%2C%224254761989%22%2C%224255432378%22%2C%224312742466%22%2C%224326699742%22%2C%224326818082%22%2C%224327955860%22%2C%224370590371%22%2C%224372430258%22%2C%224372868243%22%2C%224474214654%22%2C%224475484255%22%2C%224475995296%22%2C%224489268853%22%2C%224500948443%22%2C%224501838736%22%2C%224503782000%22%2C%224504145716%22%2C%224516965446%22%2C%224519199538%22%2C%224519243274%22%2C%224530384028%22%2C%224573881259%22%2C%224575925341%22%2C%224617509729%22%2C%224619654531%22%2C%224619873240%22%2C%224723890949%22%2C%224735542348%22%2C%224766773877%22%2C%224780076410%22%2C%224809949027%22%2C%224823076755%22%2C%224839473227%22%2C%224852629019%22%2C%224896065848%22%2C%224924801658%22%2C%224926903194%22%2C%224938804262%22%2C%224955754739%22%2C%224970736617%22%2C%224997163340%22%2C%225028934840%22%2C%225042588326%22%2C%225055801374%22%2C%225103080167%22%2C%225114905708%22%2C%225115534039%22%2C%225115869424%22%2C%225144808371%22%2C%225159205830%22%2C%225174375994%22%2C%225231832117%22%2C%225247730833%22%2C%225248446458%22%2C%225291856456%22%2C%225317129594%22%2C%225348623756%22%2C%225364977088%22%2C%225376877616%22%2C%225377446229%22%2C%225377927964%22%2C%225406487849%22%2C%225480120932%22%2C%225492969654%22%2C%225565128350%22%2C%225595249249%22%2C%225623693160%22%2C%225624832585%22%2C%225682402703%22%2C%225845146472%22%2C%225855979281%22%2C%225887240031%22%2C%225900396223%22%2C%225902484088%22%2C%225942899024%22%2C%225975984947%22%2C%225989857178%22%2C%226163710175%22%2C%226177990420%22%2C%226209498692%22%2C%226220712283%22%2C%226222230785%22%2C%226263276083%22%2C%226278138984%22%2C%226309603153%22%2C%226322687028%22%2C%22635743109%22%2C%226384842151%22%2C%226411635598%22%2C%226412233719%22%2C%226484377108%22%2C%226613785802%22%2C%226614928166%22%2C%226631059913%22%2C%226643164727%22%2C%226658406895%22%2C%226702705861%22%2C%226745384646%22%2C%226777258586%22%2C%226804898281%22%2C%226863842503%22%2C%227037463002%22%2C%227067117794%22%5D%2C%22colorSeed%22:4270253886%2C%22name%22:%22c3%20segmentation%22%7D%2C%7B%22type%22:%22annotation%22%2C%22source%22:%22precomputed://gs://h01-release/data/20210601/c3/synapses/precomputed%22%2C%22tab%22:%22rendering%22%2C%22ignoreNullSegmentFilter%22:false%2C%22shader%22:%22void%20main%28%29%20%7B%5Cn%20%20if%20%28prop_type%28%29%20==%20uint%281%29%29%20%7B%5Cn%20%20%20%20setColor%28vec3%280.%2C0.%2C1.%29%29%3B%5Cn%20%20%7D%20else%20%7B%5Cn%20%20%20%20setColor%28vec3%281.%2C1.%2C0.%29%29%3B%5Cn%20%20%7D%5Cn%20%20%5Cn%20%20setEndpointMarkerBorderWidth%280.0%29%3B%5Cn%20%20setEndpointMarkerSize%284.0%29%3B%5Cn%7D%5Cn%22%2C%22linkedSegmentationLayer%22:%7B%22post_synaptic_cell%22:%22c3%20segmentation%22%7D%2C%22filterBySegmentation%22:%5B%22post_synaptic_cell%22%5D%2C%22name%22:%22synapse%20annotations%22%7D%2C%7B%22type%22:%22annotation%22%2C%22source%22:%22precomputed://gs://h01-release/data/20210601/c3/subcompartments/annotations%22%2C%22tab%22:%22source%22%2C%22ignoreNullSegmentFilter%22:false%2C%22shader%22:%22void%20main%28%29%20%7B%5Cn%20%20switch%20%28prop_class_label%28%29%29%20%7B%5Cn%20%20case%200:%20%20//%20axon%5Cn%20%20%20%20setColor%28vec3%280%2C%200%2C%201%29%29%3B%5Cn%20%20%20%20break%3B%5Cn%20%20case%201:%20%20//%20dendrite%5Cn%20%20%20%20setColor%28vec3%281%2C%200%2C%200%29%29%3B%5Cn%20%20%20%20break%3B%5Cn%20%20case%202:%20%20//%20astrocyte%5Cn%20%20%20%20setColor%28vec3%280%2C%201%2C%200%29%29%3B%5Cn%20%20%20%20break%3B%5Cn%20%20case%203:%20%20//%20soma%5Cn%20%20%20%20setColor%28vec3%281%2C%201%2C%201%29%29%3B%5Cn%20%20%20%20break%3B%5Cn%20%20case%204:%20%20//%20cilium%5Cn%20%20%20%20setColor%28vec3%280.5%2C%200.5%2C%200%29%29%3B%5Cn%20%20%20%20break%3B%5Cn%20%20case%205:%20%20//%20AIS%5Cn%20%20%20%20setColor%28vec3%280.5%2C%200.5%2C%201%29%29%3B%5Cn%20%20%20%20break%3B%5Cn%20%20%20%20%5Cn%20%20case%201000:%20%20//%20myelinated%20axon%5Cn%20%20case%201001:%5Cn%20%20%20%20setColor%28vec3%281%2C%200.25%2C%200.75%29%29%3B%5Cn%20%20%20%20break%3B%5Cn%20%20case%201004:%20%20//%20fragments%5Cn%20%20case%201005:%5Cn%20%20default:%5Cn%20%20%20%20discard%3B%5Cn%20%20%7D%5Cn%7D%22%2C%22linkedSegmentationLayer%22:%7B%22skeleton_id%22:%22c3%20segmentation%22%7D%2C%22filterBySegmentation%22:%5B%22skeleton_id%22%5D%2C%22name%22:%22subcompartment%20annotations%22%2C%22visible%22:false%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22precomputed://gs://h01-release/data/20210601/c3/synapses/incoming_excitatory%22%2C%22tab%22:%22source%22%2C%22linkedSegmentationGroup%22:%22c3%20segmentation%22%2C%22linkedSegmentationColorGroup%22:false%2C%22colorSeed%22:2613304347%2C%22segmentDefaultColor%22:%22#ffff00%22%2C%22name%22:%22incoming%20excitatory%22%2C%22archived%22:true%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22precomputed://gs://h01-release/data/20210601/c3/synapses/incoming_inhibitory%22%2C%22tab%22:%22source%22%2C%22linkedSegmentationGroup%22:%22c3%20segmentation%22%2C%22linkedSegmentationColorGroup%22:false%2C%22colorSeed%22:679993271%2C%22segmentDefaultColor%22:%22#0000ff%22%2C%22name%22:%22incoming%20inhibitory%22%2C%22archived%22:true%7D%2C%7B%22type%22:%22annotation%22%2C%22source%22:%22precomputed://gs://h01-release/data/20210601/c3/embeddings/combined_umap%22%2C%22tab%22:%22source%22%2C%22shader%22:%22void%20main%28%29%20%7B%5Cn%20%20setColor%28vec3%28%5Cn%20%20%20%201.0%20-%20%28prop_ue0%28%29%20+%204.6017108%29%20/%2018.7%2C%20%5Cn%20%20%20%201.0%20-%20%28prop_ue1%28%29%20+%200.13594195%20%29/%209.28%2C%20%5Cn%20%20%20%20%28prop_ue2%28%29%20-%206.69197893%29%20/%207.59%29%29%3B%20%5Cn%20%20setPointMarkerBorderColor%28vec3%28%5Cn%20%20%20%201.0%20-%20%28prop_ue0%28%29%20+%204.6017108%29%20/%2018.7%2C%20%5Cn%20%20%20%201.0%20-%20%28prop_ue1%28%29%20+%200.13594195%20%29/%209.28%2C%20%5Cn%20%20%20%20%28prop_ue2%28%29%20-%206.69197893%29%20/%207.59%29%29%3B%20%5Cn%20%20setPointMarkerSize%285.0%29%3B%5Cn%20%20setPointMarkerBorderWidth%280.%29%3B%5Cn%7D%22%2C%22linkedSegmentationLayer%22:%7B%22skeleton_id%22:%22c3%20segmentation%22%7D%2C%22filterBySegmentation%22:%5B%22skeleton_id%22%5D%2C%22name%22:%22embeddings%22%2C%22archived%22:true%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22precomputed://gs://h01-release/data/20210601/c3/subcompartments%22%2C%22tab%22:%22rendering%22%2C%22segmentColors%22:%7B%22100%22:%22#0000ff%22%2C%22101%22:%22#ff0000%22%2C%22102%22:%22#00ff00%22%2C%22103%22:%22#ffffff%22%2C%22104%22:%22#7f7f00%22%2C%22105%22:%22#7f7fff%22%2C%221100%22:%22#ff3fbf%22%2C%221101%22:%22#ff3fbf%22%2C%221102%22:%22#000000%22%2C%221103%22:%22#000000%22%2C%221104%22:%22#ff3fbf%22%2C%221105%22:%22#ff3fbf%22%7D%2C%22name%22:%22subcompartments%20render%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22precomputed://gs://h01-release/data/20210601/layers%22%2C%22tab%22:%22source%22%2C%22selectedAlpha%22:0.3%2C%22segments%22:%5B%221%22%2C%222%22%2C%223%22%2C%224%22%2C%225%22%2C%226%22%2C%227%22%5D%2C%22segmentQuery%22:%221%2C2%2C3%2C4%2C5%2C6%2C7%22%2C%22name%22:%22cortical%20layers%22%2C%22archived%22:true%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22precomputed://gs://h01-release/data/20210601/masking%22%2C%22tab%22:%22source%22%2C%22name%22:%22tissue%20mask%22%2C%22visible%22:false%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22precomputed://gs://h01-release/data/20210601/blood_vessels_segmented%22%2C%22tab%22:%22segments%22%2C%22selectedAlpha%22:0.25%2C%22segmentDefaultColor%22:%22#ff0000%22%2C%22name%22:%22blood%20vessels%22%2C%22visible%22:false%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22precomputed://gs://h01-release/data/20210601/blood_vessels%22%2C%22tab%22:%22source%22%2C%22name%22:%22blood%20vessel%20cells%22%2C%22visible%22:false%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22precomputed://gs://h01-release/data/20210601/cell_bodies%22%2C%22tab%22:%22source%22%2C%22name%22:%22cell%20bodies%22%2C%22visible%22:false%7D%5D%2C%22showDefaultAnnotations%22:false%2C%22showSlices%22:false%2C%22prefetch%22:false%2C%22selectedLayer%22:%7B%22row%22:1%2C%22flex%22:0.65%2C%22visible%22:true%2C%22layer%22:%22subcompartments%20render%22%7D%2C%22layout%22:%7B%22type%22:%22xy-3d%22%2C%22orthographicProjection%22:true%7D%2C%22helpPanel%22:%7B%22flex%22:0.73%2C%22visible%22:true%7D%2C%22selection%22:%7B%22row%22:2%2C%22flex%22:0.45%2C%22size%22:309%2C%22visible%22:false%7D%2C%22layerListPanel%22:%7B%22flex%22:1.27%2C%22visible%22:true%7D%7D)]

### Open Organelle Nature 2021
- **Whole-cell organelle segmentation in volume electron microscopy**
[[Paper](https://www.nature.com/articles/s41586-021-03977-3)]
[[Dataset](https://openorganelle.janelia.org/)]

### FAFB Cell 2018
- **A Complete Electron Microscopy Volume of the Brain of Adult Drosophila melanogaster**
[[Paper](https://www.sciencedirect.com/science/article/pii/S0092867418307876)]
[[Dataset](https://temca2data.org/)]
[[Neuroglancer](https://fafb-dot-neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22x%22:%5B4e-9%2C%22m%22%5D%2C%22y%22:%5B4e-9%2C%22m%22%5D%2C%22z%22:%5B4e-8%2C%22m%22%5D%7D%2C%22position%22:%5B124024.3046875%2C58665.80859375%2C2292.3662109375%5D%2C%22crossSectionScale%22:4.779288037933938%2C%22projectionOrientation%22:%5B-0.5623587369918823%2C-0.446272075176239%2C-0.5405490398406982%2C0.438634991645813%5D%2C%22projectionScale%22:81567.93776427887%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%22precomputed://gs://neuroglancer-fafb-data/fafb_v14/fafb_v14_orig%22%2C%22name%22:%22fafb_v14%22%2C%22visible%22:false%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%22precomputed://gs://neuroglancer-fafb-data/fafb_v14/fafb_v14_clahe%22%2C%22name%22:%22fafb_v14_clahe%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22precomputed://gs://fafb-ffn1-20190805/segmentation%22%2C%22tab%22:%22segments%22%2C%22objectAlpha%22:0.23%2C%22segments%22:%5B%22710435991%22%5D%2C%22name%22:%22fafb-ffn1-20190805%22%7D%2C%7B%22type%22:%22annotation%22%2C%22source%22:%22precomputed://gs://neuroglancer-20191211_fafbv14_buhmann2019_li20190805%22%2C%22tab%22:%22rendering%22%2C%22annotationColor%22:%22#cecd11%22%2C%22shader%22:%22#uicontrol%20vec3%20preColor%20color%28default=%5C%22blue%5C%22%29%5Cn#uicontrol%20vec3%20postColor%20color%28default=%5C%22red%5C%22%29%5Cn#uicontrol%20float%20scorethr%20slider%28min=0%2C%20max=1000%29%5Cn#uicontrol%20int%20showautapse%20slider%28min=0%2C%20max=1%29%5Cn%5Cnvoid%20main%28%29%20%7B%5Cn%20%20setColor%28defaultColor%28%29%29%3B%5Cn%20%20setEndpointMarkerColor%28%5Cn%20%20%20%20vec4%28preColor%2C%200.5%29%2C%5Cn%20%20%20%20vec4%28postColor%2C%200.5%29%29%3B%5Cn%20%20setEndpointMarkerSize%285.0%2C%205.0%29%3B%5Cn%20%20setLineWidth%282.0%29%3B%5Cn%20%20if%20%28int%28prop_autapse%28%29%29%20%3E%20showautapse%29%20discard%3B%5Cn%20%20if%20%28prop_score%28%29%3Cscorethr%29%20discard%3B%5Cn%7D%5Cn%5Cn%22%2C%22shaderControls%22:%7B%22scorethr%22:80%7D%2C%22linkedSegmentationLayer%22:%7B%22pre_segment%22:%22fafb-ffn1-20190805%22%2C%22post_segment%22:%22fafb-ffn1-20190805%22%7D%2C%22filterBySegmentation%22:%5B%22post_segment%22%2C%22pre_segment%22%5D%2C%22name%22:%22synapses_buhmann2019%22%2C%22visible%22:false%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%22n5://gs://fafb-v14-synaptic-clefts-heinrich-et-al-2018-n5/synapses_dt_reblocked%22%2C%22opacity%22:0.73%2C%22shader%22:%22void%20main%28%29%20%7BemitRGBA%28vec4%280.0%2C0.0%2C1.0%2CtoNormalized%28getDataValue%28%29%29%29%29%3B%7D%22%2C%22name%22:%22clefts_Heinrich_etal%22%2C%22visible%22:false%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22precomputed://gs://neuroglancer-fafb-data/elmr-data/FAFBNP.surf/mesh#type=mesh%22%2C%22segments%22:%5B%221%22%2C%2210%22%2C%2211%22%2C%2212%22%2C%2213%22%2C%2214%22%2C%2215%22%2C%2216%22%2C%2217%22%2C%2218%22%2C%2219%22%2C%222%22%2C%2220%22%2C%2221%22%2C%2222%22%2C%2223%22%2C%2224%22%2C%2225%22%2C%2226%22%2C%2227%22%2C%2228%22%2C%2229%22%2C%223%22%2C%2230%22%2C%2231%22%2C%2232%22%2C%2233%22%2C%2234%22%2C%2235%22%2C%2236%22%2C%2237%22%2C%2238%22%2C%2239%22%2C%224%22%2C%2240%22%2C%2241%22%2C%2242%22%2C%2243%22%2C%2244%22%2C%2245%22%2C%2246%22%2C%2247%22%2C%2248%22%2C%2249%22%2C%225%22%2C%2250%22%2C%2251%22%2C%2252%22%2C%2253%22%2C%2254%22%2C%2255%22%2C%2256%22%2C%2257%22%2C%2258%22%2C%2259%22%2C%226%22%2C%2260%22%2C%2261%22%2C%2262%22%2C%2263%22%2C%2264%22%2C%2265%22%2C%2266%22%2C%2267%22%2C%2268%22%2C%2269%22%2C%227%22%2C%2270%22%2C%2271%22%2C%2272%22%2C%2273%22%2C%2274%22%2C%2275%22%2C%228%22%2C%229%22%5D%2C%22name%22:%22neuropil-regions-surface%22%2C%22visible%22:false%7D%2C%7B%22type%22:%22mesh%22%2C%22source%22:%22vtk://https://storage.googleapis.com/neuroglancer-fafb-data/elmr-data/FAFB.surf.vtk.gz%22%2C%22shader%22:%22void%20main%28%29%20%7BemitRGBA%28vec4%281.0%2C%200.0%2C%200.0%2C%200.5%29%29%3B%7D%22%2C%22name%22:%22neuropil-full-surface%22%2C%22visible%22:false%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%5B%7B%22url%22:%22precomputed://gs://fafb-ffn1-20190805/segmentation%22%2C%22subsources%22:%7B%22default%22:true%2C%22bounds%22:true%7D%2C%22enableDefaultSubsources%22:false%7D%2C%22precomputed://gs://fafb-ffn1-20190805/segmentation/skeletons_32nm%22%5D%2C%22tab%22:%22segments%22%2C%22selectedAlpha%22:0%2C%22segments%22:%5B%22710435991%22%5D%2C%22segmentQuery%22:%22710435991%22%2C%22name%22:%22skeletons_32nm%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22precomputed://gs://fafb-ffn1/fafb-public-skeletons%22%2C%22tab%22:%22segments%22%2C%22segments%22:%5B%22710435991%22%5D%2C%22segmentQuery%22:%22710435991%22%2C%22name%22:%22public_skeletons%22%2C%22visible%22:false%7D%5D%2C%22showAxisLines%22:false%2C%22showSlices%22:false%2C%22selectedLayer%22:%7B%22layer%22:%22public_skeletons%22%2C%22visible%22:true%7D%2C%22layout%22:%22xy-3d%22%7D)]

### FlyWire Nature method 2022
- **FlyWire: online community for whole-brain connectomics**
[[Paper](https://www.nature.com/articles/s41592-021-01330-0.pdf)]
[[Website](https://flywire.ai/)]

### Hemi Brain elife 2020
- **A connectome and analysis of the adult Drosophila central brain**
[[Paper](https://elifesciences.org/articles/57443)][[neuroglancer](https://fafb-dot-neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22x%22:%5B4e-9%2C%22m%22%5D%2C%22y%22:%5B4e-9%2C%22m%22%5D%2C%22z%22:%5B4e-8%2C%22m%22%5D%7D%2C%22position%22:%5B109421.8984375%2C41044.6796875%2C5417%5D%2C%22crossSectionScale%22:2.1875%2C%22projectionOrientation%22:%5B-0.08939177542924881%2C-0.9848012924194336%2C-0.07470247149467468%2C0.12882165610790253%5D%2C%22projectionScale%22:27773.019357116023%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%22precomputed://gs://neuroglancer-fafb-data/fafb_v14/fafb_v14_orig%22%2C%22name%22:%22fafb_v14%22%2C%22visible%22:false%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%22precomputed://gs://neuroglancer-fafb-data/fafb_v14/fafb_v14_clahe%22%2C%22name%22:%22fafb_v14_clahe%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22precomputed://gs://fafb-ffn1-20190805/segmentation%22%2C%22segments%22:%5B%22710435991%22%5D%2C%22name%22:%22fafb-ffn1-20190805%22%7D%2C%7B%22type%22:%22annotation%22%2C%22source%22:%22precomputed://gs://neuroglancer-20191211_fafbv14_buhmann2019_li20190805%22%2C%22tab%22:%22rendering%22%2C%22annotationColor%22:%22#cecd11%22%2C%22shader%22:%22#uicontrol%20vec3%20preColor%20color%28default=%5C%22blue%5C%22%29%5Cn#uicontrol%20vec3%20postColor%20color%28default=%5C%22red%5C%22%29%5Cn#uicontrol%20float%20scorethr%20slider%28min=0%2C%20max=1000%29%5Cn#uicontrol%20int%20showautapse%20slider%28min=0%2C%20max=1%29%5Cn%5Cnvoid%20main%28%29%20%7B%5Cn%20%20setColor%28defaultColor%28%29%29%3B%5Cn%20%20setEndpointMarkerColor%28%5Cn%20%20%20%20vec4%28preColor%2C%200.5%29%2C%5Cn%20%20%20%20vec4%28postColor%2C%200.5%29%29%3B%5Cn%20%20setEndpointMarkerSize%285.0%2C%205.0%29%3B%5Cn%20%20setLineWidth%282.0%29%3B%5Cn%20%20if%20%28int%28prop_autapse%28%29%29%20%3E%20showautapse%29%20discard%3B%5Cn%20%20if%20%28prop_score%28%29%3Cscorethr%29%20discard%3B%5Cn%7D%5Cn%5Cn%22%2C%22shaderControls%22:%7B%22scorethr%22:80%7D%2C%22linkedSegmentationLayer%22:%7B%22pre_segment%22:%22fafb-ffn1-20190805%22%2C%22post_segment%22:%22fafb-ffn1-20190805%22%7D%2C%22filterBySegmentation%22:%5B%22post_segment%22%2C%22pre_segment%22%5D%2C%22name%22:%22synapses_buhmann2019%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%22n5://gs://fafb-v14-synaptic-clefts-heinrich-et-al-2018-n5/synapses_dt_reblocked%22%2C%22opacity%22:0.73%2C%22shader%22:%22void%20main%28%29%20%7BemitRGBA%28vec4%280.0%2C0.0%2C1.0%2CtoNormalized%28getDataValue%28%29%29%29%29%3B%7D%22%2C%22name%22:%22clefts_Heinrich_etal%22%2C%22visible%22:false%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22precomputed://gs://neuroglancer-fafb-data/elmr-data/FAFBNP.surf/mesh#type=mesh%22%2C%22segments%22:%5B%221%22%2C%2210%22%2C%2211%22%2C%2212%22%2C%2213%22%2C%2214%22%2C%2215%22%2C%2216%22%2C%2217%22%2C%2218%22%2C%2219%22%2C%222%22%2C%2220%22%2C%2221%22%2C%2222%22%2C%2223%22%2C%2224%22%2C%2225%22%2C%2226%22%2C%2227%22%2C%2228%22%2C%2229%22%2C%223%22%2C%2230%22%2C%2231%22%2C%2232%22%2C%2233%22%2C%2234%22%2C%2235%22%2C%2236%22%2C%2237%22%2C%2238%22%2C%2239%22%2C%224%22%2C%2240%22%2C%2241%22%2C%2242%22%2C%2243%22%2C%2244%22%2C%2245%22%2C%2246%22%2C%2247%22%2C%2248%22%2C%2249%22%2C%225%22%2C%2250%22%2C%2251%22%2C%2252%22%2C%2253%22%2C%2254%22%2C%2255%22%2C%2256%22%2C%2257%22%2C%2258%22%2C%2259%22%2C%226%22%2C%2260%22%2C%2261%22%2C%2262%22%2C%2263%22%2C%2264%22%2C%2265%22%2C%2266%22%2C%2267%22%2C%2268%22%2C%2269%22%2C%227%22%2C%2270%22%2C%2271%22%2C%2272%22%2C%2273%22%2C%2274%22%2C%2275%22%2C%228%22%2C%229%22%5D%2C%22name%22:%22neuropil-regions-surface%22%2C%22visible%22:false%7D%2C%7B%22type%22:%22mesh%22%2C%22source%22:%22vtk://https://storage.googleapis.com/neuroglancer-fafb-data/elmr-data/FAFB.surf.vtk.gz%22%2C%22shader%22:%22void%20main%28%29%20%7BemitRGBA%28vec4%281.0%2C%200.0%2C%200.0%2C%200.5%29%29%3B%7D%22%2C%22name%22:%22neuropil-full-surface%22%2C%22visible%22:false%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%5B%7B%22url%22:%22precomputed://gs://fafb-ffn1-20190805/segmentation%22%2C%22subsources%22:%7B%22default%22:true%2C%22bounds%22:true%7D%2C%22enableDefaultSubsources%22:false%7D%2C%22precomputed://gs://fafb-ffn1-20190805/segmentation/skeletons_32nm%22%5D%2C%22selectedAlpha%22:0%2C%22segments%22:%5B%224613663523%22%5D%2C%22name%22:%22skeletons_32nm%22%2C%22visible%22:false%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22precomputed://gs://fafb-ffn1/fafb-public-skeletons%22%2C%22name%22:%22public_skeletons%22%2C%22visible%22:false%7D%5D%2C%22showAxisLines%22:false%2C%22showSlices%22:false%2C%22layout%22:%22xy-3d%22%7D)]

### Fly VNC Cell 2021
- **Reconstruction of motor control circuits in adult Drosophila using automated transmission electron microscopy** [[dataset(Larva)](https://github.com/unidesigner/groundtruth-drosophila-vnc)]

#### Learning cellular morphology Nature Communication 2019
- **Learning cellular morphology with neural networks** [[paper](https://www.nature.com/articles/s41467-019-10836-3)][[dataset](https://structuralneurobiologylab.github.io/SyConn/)]
## visualization 
If you want to use neuroglancer to visualize your own EM image and segmentation, please refer to my notes in [neuroglancer_EM&seg](https://github.com/Levishery/connectomic-paper-datasets/blob/main/neuroglancer/neuroglancer%E5%8F%AF%E8%A7%86%E5%8C%96%E6%9C%AC%E5%9C%B0EM%26segmentation.pdf)

## annotation process
The ids of the glia segments we annotated is in [annotation](https://github.com/Levishery/connectomic-paper-datasets/tree/main/annotation).
