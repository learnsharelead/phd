import pandas as pd
import streamlit as st

from utils.nav import show_top_nav
from utils.seo import inject_seo_meta
from utils.styles import apply_custom_css, show_footer


MASTER_SOURCES = [
    "Attached course book for official syllabus scope and unit boundaries.",
    "NCBI and NCBI Bookshelf resources for nucleic acids, protein structure, and BLAST fundamentals.",
    "Thermo Fisher Scientific learning resources for UV-Vis spectroscopy, qPCR, ELISA, and flow cytometry.",
    "Bio-Rad learning resources for western blotting workflow and protein analysis.",
    "Leica Science Lab articles for fluorescence and confocal microscopy foundations.",
    "EMBL-EBI training material for sequence alignment, homology, and phylogenetic use-cases.",
    "US EPA and ATSDR/CDC material for bioremediation, exposure, dose, and toxicology foundations.",
]


COURSES = [
    {
        "code": "PHDLS101",
        "title": "Bioanalytical Techniques",
        "credits": 4,
        "hours": "L:4 T:0 P:0",
        "focus": "A methods-heavy course that connects biochemical questions to the right analytical tool.",
        "why_it_matters": [
            "Modern life-science research depends on selecting the correct analytical technique before interpretation begins.",
            "This course links chemistry, instrumentation, biomolecules, and diagnostics into one practical workflow.",
            "The strongest answers in this subject compare principles, outputs, sensitivity, limitations, and use-cases.",
        ],
        "outcomes": [
            "Explain the chemistry behind buffers, pH control, and analytical sample preparation.",
            "Distinguish spectroscopy, centrifugation, chromatography, microscopy, and electrophoretic methods.",
            "Interpret why certain techniques are better for separation, imaging, quantification, or detection.",
            "Connect recombinant DNA and immunodiagnostic methods to clinical and research applications.",
        ],
        "unit_notes": [
            {
                "title": "Unit 1: Acids, Buffers, Spectrometry, and Centrifugation",
                "summary": "This unit establishes sample preparation and measurement fundamentals.",
                "deep_dive": [
                    "Buffers resist sudden pH change by pairing a weak acid with its conjugate base or a weak base with its conjugate acid. In biochemistry, pH control protects enzyme activity, protein conformation, and nucleic acid stability.",
                    "A good buffer is selected by matching its pKa near the working pH, minimizing interaction with the analyte, and maintaining ionic strength compatible with downstream assays.",
                    "UV-Vis spectrophotometry is built on absorbance. The Beer-Lambert relation lets concentration be estimated when extinction coefficient and path length are known.",
                    "Colorimetry is usually preferred when a colored product is formed, whereas direct UV absorbance is useful when the analyte itself absorbs strongly at a known wavelength.",
                    "Centrifugation separates particles by sedimentation behavior. Differential centrifugation is best for crude fractionation, while density-gradient centrifugation improves resolution and purity.",
                ],
                "example": "Example: A researcher quantifies purified protein by A280, then spins lysate fractions at increasing speeds to separate nuclei, mitochondria, and microsomes before downstream western blotting.",
                "exam_focus": [
                    "Prepare a clean comparison: colorimetry versus UV-Vis spectroscopy.",
                    "State the rationale for choosing differential versus density-gradient centrifugation.",
                    "Explain why pH control is part of analytical validity, not just sample storage.",
                ],
            },
            {
                "title": "Unit 2: Chromatography and Microscopy",
                "summary": "This unit is about separation logic and visualization logic.",
                "deep_dive": [
                    "Gel filtration separates molecules by size and is valuable when preserving native structure matters.",
                    "Ion-exchange chromatography resolves molecules by charge, so pH and salt concentration directly affect binding and elution.",
                    "Affinity chromatography is the most selective when a ligand-target interaction is known; it is often the best route for purifying tagged recombinant proteins.",
                    "Gas chromatography is suited to volatile compounds, while HPLC handles nonvolatile or thermally sensitive analytes with better control and reproducibility.",
                    "Light microscopy supports rapid observation, fluorescence microscopy adds molecular specificity, and confocal microscopy reduces out-of-focus light for optical sectioning.",
                    "TEM reveals ultrastructural internal detail, whereas SEM emphasizes surface morphology.",
                ],
                "example": "Example: A His-tagged recombinant protein can be captured by affinity chromatography, polished by gel filtration, then examined by fluorescence or confocal microscopy in a cell-based localization study.",
                "exam_focus": [
                    "Differentiate size-based, charge-based, and affinity-based separations.",
                    "Write one paragraph each on TEM versus SEM and fluorescence versus confocal microscopy.",
                    "Always link microscopy choice to the biological question being asked.",
                ],
            },
            {
                "title": "Unit 3: Characterization of Proteins and Nucleic Acids",
                "summary": "This unit shifts from isolation to validation, quantification, and molecular evidence.",
                "deep_dive": [
                    "SDS-PAGE separates proteins largely by size after denaturation, giving a first-pass purity and molecular-weight view.",
                    "Western blotting adds specificity by transferring separated proteins to a membrane and probing with antibodies. Its value lies in confirming identity, not merely band presence.",
                    "Flow cytometry analyzes single cells in suspension using light scatter and fluorescence, making it powerful for immunophenotyping and cell-state analysis.",
                    "Mass spectrometry supports high-resolution molecular identification and is central to modern proteomics.",
                    "DNA and RNA quality assessment must go beyond concentration; integrity, contamination, and suitability for downstream amplification matter.",
                    "Real-time PCR tracks amplification during cycling, enabling relative or absolute quantification depending on assay design.",
                ],
                "example": "Example: RNA isolated from stressed cells is checked for purity and integrity before cDNA synthesis and qPCR; protein from the same cells is profiled by SDS-PAGE and validated by western blot.",
                "exam_focus": [
                    "Explain why SDS-PAGE and western blot are complementary rather than interchangeable.",
                    "Be ready to justify qPCR over endpoint PCR for expression studies.",
                    "Write answers using the sequence: principle, steps, output, applications, limitations.",
                ],
            },
            {
                "title": "Unit 4: Recombinant DNA Technology and Diagnostic Techniques",
                "summary": "This unit connects molecular manipulation with applied testing.",
                "deep_dive": [
                    "Recombinant DNA technology combines DNA fragments from different sources to study genes, produce proteins, or create diagnostic systems.",
                    "Bacterial systems are fast and economical, yeast adds some eukaryotic processing, insect cells improve folding for some complex proteins, and mammalian cells are preferred when authentic post-translational modification matters.",
                    "Protein-DNA or protein-RNA interaction studies help establish regulation, binding specificity, and mechanism.",
                    "ELISA is excellent for sensitive plate-based antigen or antibody detection, while RIA and CLIA emphasize signal generation through different detection chemistries.",
                    "PET and other advanced diagnostic platforms extend analytics from molecular recognition into functional imaging and clinical decision support.",
                ],
                "example": "Example: A cytokine biomarker pipeline may involve recombinant antigen production, affinity purification, ELISA-based validation, and later clinical diagnostic deployment.",
                "exam_focus": [
                    "Compare expression systems using speed, cost, folding quality, and application.",
                    "Differentiate ELISA, RIA, and CLIA by detection principle and lab practicality.",
                    "Use one applied example in every long answer to raise answer quality.",
                ],
            },
        ],
        "applications": [
            "Clinical biochemistry laboratories use UV-Vis, immunoassays, and chromatography for diagnostic measurement.",
            "Proteomics and cell biology depend on electrophoresis, blotting, microscopy, and flow cytometry to validate biological claims.",
            "Biopharma and molecular diagnostics rely on recombinant expression, purification, and analytical quality control.",
        ],
        "worked_examples": [
            {
                "title": "Worked Example 1: Choosing a protein quantification route",
                "body": "If the sample is relatively pure, A280 can be fast and non-destructive. If contaminants or low concentration are likely, a colorimetric assay with a standard curve is usually more defensible.",
            },
            {
                "title": "Worked Example 2: Protein confirmation workflow",
                "body": "Use affinity chromatography to enrich the target, SDS-PAGE to inspect purity, western blot to confirm identity, and mass spectrometry if peptide-level confirmation is required.",
            },
        ],
        "question_paper": {
            "Section A: Short answers": [
                {
                    "q": "Define buffer and explain why buffers are essential in biochemical experiments.",
                    "a": "A buffer is a solution that resists sudden change in pH when small amounts of acid or base are added. Buffers are essential because enzyme activity, protein charge, membrane stability, and nucleic acid integrity are all strongly influenced by pH.",
                },
                {
                    "q": "State the principle of UV-Vis spectroscopy.",
                    "a": "UV-Vis spectroscopy measures how much ultraviolet or visible light a sample absorbs at specific wavelengths. Absorbance is related to concentration through the Beer-Lambert relationship when path length and extinction coefficient are known.",
                },
                {
                    "q": "Differentiate TEM and SEM in one sentence each.",
                    "a": "TEM passes electrons through thin specimens to reveal internal ultrastructure. SEM scans the specimen surface to produce detailed surface topography images.",
                },
                {
                    "q": "Why is western blot more specific than SDS-PAGE?",
                    "a": "SDS-PAGE separates many proteins by size, while western blot uses antibodies to identify a specific target protein after separation.",
                },
            ],
            "Section B: Medium answers": [
                {
                    "q": "Compare differential centrifugation and density-gradient centrifugation.",
                    "a": "Differential centrifugation separates particles in stages according to sedimentation rate and is useful for crude fractionation. Density-gradient centrifugation provides better resolution because particles migrate according to density and form more distinct bands, so it is preferred when higher purity is required.",
                },
                {
                    "q": "Explain the role of HPLC in biomolecular analysis.",
                    "a": "HPLC gives high-resolution separation under controlled pressure using specialized stationary and mobile phases. It is used for purity analysis, quantification, compound isolation, and method standardization because it is reproducible, sensitive, and adaptable to many biological molecules.",
                },
                {
                    "q": "Write a note on flow cytometry in biology and medicine.",
                    "a": "Flow cytometry analyzes single cells in suspension using light scatter and fluorescence signals. It supports immunophenotyping, cell-cycle analysis, apoptosis studies, stem-cell analysis, and clinical applications such as leukemia classification and immune monitoring.",
                },
            ],
            "Section C: Long answers": [
                {
                    "q": "Describe the complete workflow of western blotting and discuss its advantages and limitations.",
                    "a": "A strong answer should cover sample lysis, protein denaturation, SDS-PAGE separation, transfer to membrane, blocking, antibody probing, detection, imaging, and band interpretation. Advantages include specificity, relative quantification, and compatibility with complex lysates. Limitations include antibody dependence, background noise, semiquantitative interpretation, and the need for careful normalization.",
                },
                {
                    "q": "Discuss recombinant DNA technology and the expression of recombinant proteins in different host systems.",
                    "a": "Recombinant DNA technology involves combining DNA segments for cloning, expression, mutation, or diagnostic use. Bacteria are rapid and cost-effective but limited in complex post-translational modification. Yeast offers easier culture with some eukaryotic processing. Insect cells handle many complex proteins better. Mammalian cells are slower and costlier but give the most authentic folding and modification for therapeutic or receptor studies.",
                },
            ],
        },
        "source_labels": [
            "Thermo Fisher UV-Vis and qPCR learning resources",
            "Bio-Rad western blotting resource center",
            "Leica microscopy learning content",
            "Thermo Fisher ELISA and flow cytometry learning material",
        ],
    },
    {
        "code": "PHDLS102",
        "title": "Biomolecules: Structure, Function in Health and Diseases",
        "credits": 3,
        "hours": "L:3 T:0 P:0",
        "focus": "A concept-rich paper on how chemical structure controls biological function and disease relevance.",
        "why_it_matters": [
            "The subject gives the language needed to understand proteins, genes, membranes, metabolism, and disease at molecular level.",
            "High-quality answers in this paper move from structure to interaction to function to pathology.",
            "The course is strongest when students can compare classes of biomolecules rather than memorizing isolated definitions.",
        ],
        "outcomes": [
            "Explain bonds, water, pH, and buffer behavior in biological systems.",
            "Relate amino-acid chemistry to protein folding, stability, and function.",
            "Describe DNA, RNA, lipids, and carbohydrates as dynamic biomolecular systems.",
            "Link biomolecular abnormalities to disease, signaling, and systems biology.",
        ],
        "unit_notes": [
            {
                "title": "Unit 1: Interactions, Acids, and Buffers",
                "summary": "Biochemistry begins with the behavior of molecules in water.",
                "deep_dive": [
                    "Covalent bonds provide core molecular architecture, while hydrogen bonding, ionic interaction, van der Waals forces, and hydrophobic effects shape biomolecular behavior in solution.",
                    "Water is not just a solvent; its polarity, hydrogen bonding network, and dielectric properties influence folding, solubility, and reactivity.",
                    "Acid-base behavior determines ionization state. That means pH alters enzyme active sites, charge interactions, ligand binding, and transport.",
                    "The Henderson-Hasselbalch equation becomes useful only when interpreted: it predicts dominant species and helps explain why a buffer performs best around its pKa.",
                ],
                "example": "Example: Histidine side chains can shift protonation state near physiological pH, which is why they often participate in catalytic sites and buffer-sensitive interactions.",
                "exam_focus": [
                    "Never state the Henderson-Hasselbalch equation without interpreting it biologically.",
                    "Explain how water drives both solubility and hydrophobic collapse.",
                ],
            },
            {
                "title": "Unit 2: Amino Acids and Proteins",
                "summary": "Protein function begins with amino-acid sequence and ends with higher-order structure.",
                "deep_dive": [
                    "Amino acids differ through side chains, and those side chains determine charge, polarity, reactivity, and structural preference.",
                    "Primary structure defines sequence, secondary structure reflects local folding, tertiary structure reflects full three-dimensional arrangement, and quaternary structure describes multimeric assembly.",
                    "Fibrous proteins emphasize structural roles, whereas globular proteins often support catalysis, transport, and regulation.",
                    "Ramachandran plots help explain why not every bond angle is sterically allowed.",
                    "Protein structure is central to health and disease because even single substitutions can alter folding, stability, or ligand interaction.",
                ],
                "example": "Example: Hemoglobin illustrates quaternary structure and cooperative binding, while myoglobin demonstrates a simpler oxygen-binding system with a different physiological role.",
                "exam_focus": [
                    "Use sequence to structure to function as the core answer pattern.",
                    "Bring in one disease example such as misfolding, mutation, or abnormal oxygen binding.",
                ],
            },
            {
                "title": "Unit 3: Nucleic Acids",
                "summary": "DNA and RNA are chemical polymers with distinct roles and structural logic.",
                "deep_dive": [
                    "DNA is a double-stranded information-storage molecule with complementary pairing and a sugar-phosphate backbone.",
                    "RNA is more diverse in structure and function; messenger, transfer, and ribosomal RNAs form the core translation system, while regulatory RNAs expand functional complexity.",
                    "Supercoiling and circular DNA matter because topology affects packaging, replication, and transcriptional accessibility.",
                    "DNA-protein interactions are essential in transcription, replication, repair, and chromatin organization.",
                ],
                "example": "Example: Plasmid DNA is circular, can exist in supercoiled forms, and is central in cloning because topology affects migration and transformation efficiency.",
                "exam_focus": [
                    "Differentiate DNA and RNA by sugar, bases, strand behavior, stability, and function.",
                    "If asked about polymorphism, connect it to variation, markers, and biological consequence.",
                ],
            },
            {
                "title": "Unit 4: Carbohydrates and Lipids",
                "summary": "These biomolecules link energy, structure, signaling, and membrane biology.",
                "deep_dive": [
                    "Carbohydrates range from monosaccharides to polysaccharides and serve structural, storage, and recognition roles.",
                    "Fatty acids vary by chain length and saturation, which changes membrane fluidity and metabolic handling.",
                    "Phospholipids and cholesterol are central to membrane architecture, permeability, and signaling platform formation.",
                    "Glycoproteins and proteoglycans support cell recognition, extracellular matrix biology, and tissue organization.",
                    "Liposomes demonstrate how lipid self-assembly can be translated into drug delivery and experimental models.",
                ],
                "example": "Example: Cholesterol helps modulate membrane fluidity and microdomain behavior, which affects receptor signaling and disease-related transport events.",
                "exam_focus": [
                    "Compare storage carbohydrates with structural carbohydrates.",
                    "Use membranes as the unifying theme when writing on lipids.",
                ],
            },
        ],
        "applications": [
            "Drug design and structural biology depend on understanding protein shape and binding behavior.",
            "Molecular diagnostics, cloning, and genomics all build on nucleic-acid chemistry and organization.",
            "Membrane biology, lipid disorders, metabolic disease, and signaling research all sit on the biomolecule foundation.",
        ],
        "worked_examples": [
            {
                "title": "Worked Example 1: Why one mutation can cause disease",
                "body": "A substitution that changes side-chain chemistry can disrupt folding, active-site geometry, ligand binding, or intermolecular interaction. The disease consequence follows from structural disturbance, not from sequence change alone.",
            },
            {
                "title": "Worked Example 2: Why RNA is chemically less stable than DNA",
                "body": "RNA carries ribose with a 2-prime hydroxyl group, which makes hydrolysis more likely and contributes to lower stability than DNA under many conditions.",
            },
        ],
        "question_paper": {
            "Section A: Short answers": [
                {
                    "q": "What is a peptide bond?",
                    "a": "A peptide bond is the amide linkage formed when the carboxyl group of one amino acid reacts with the amino group of another, releasing water.",
                },
                {
                    "q": "Name the four levels of protein structure.",
                    "a": "Primary, secondary, tertiary, and quaternary structure.",
                },
                {
                    "q": "Differentiate deoxyribose and ribose.",
                    "a": "Deoxyribose lacks the hydroxyl group at the 2-prime carbon that ribose contains.",
                },
                {
                    "q": "State one function of cholesterol in membranes.",
                    "a": "Cholesterol helps regulate membrane fluidity and contributes to membrane organization.",
                },
            ],
            "Section B: Medium answers": [
                {
                    "q": "Explain the Ramachandran plot and its significance.",
                    "a": "A Ramachandran plot maps allowable phi and psi backbone angles of amino-acid residues. It is significant because it explains conformational constraints and helps assess whether a protein model adopts stereochemically reasonable geometry.",
                },
                {
                    "q": "Write a note on DNA-protein interactions.",
                    "a": "DNA-protein interactions drive replication, transcription, repair, recombination, and chromatin organization. Specific recognition depends on sequence, groove geometry, electrostatics, and higher-order chromatin context.",
                },
                {
                    "q": "How do saturated and unsaturated fatty acids differ biologically?",
                    "a": "Saturated fatty acids lack double bonds and tend to support tighter packing, while unsaturated fatty acids contain one or more double bonds that increase fluidity and alter membrane behavior and metabolism.",
                },
            ],
            "Section C: Long answers": [
                {
                    "q": "Discuss protein structure-function relationships with suitable examples.",
                    "a": "An excellent answer should show how amino-acid sequence determines folding, how local secondary structures support stability, how tertiary packing creates binding pockets, and how quaternary organization can enable cooperativity. Examples such as hemoglobin, myoglobin, collagen, or enzyme active sites strengthen the answer.",
                },
                {
                    "q": "Describe carbohydrates and lipids as biomolecules involved in health and disease.",
                    "a": "Carbohydrates support energy metabolism, storage, structural roles, and cell recognition. Lipids build membranes, store energy, and act in signaling. Disease links include dyslipidemia, membrane instability, glycosylation defects, metabolic syndrome, and inflammatory signaling imbalance.",
                },
            ],
        },
        "source_labels": [
            "NCBI Bookshelf chapters on protein and DNA structure",
            "RCSB PDB educational resources on hierarchical protein structure",
            "NCBI resources on RNA fundamentals",
        ],
    },
    {
        "code": "PHDLS103",
        "title": "Bioinformatics: Algorithms and Application",
        "credits": 3,
        "hours": "L:3 T:0 P:0",
        "focus": "A bridge between biological questions and computational reasoning.",
        "why_it_matters": [
            "This subject trains students to move from raw biological sequence or structural data to inference.",
            "It rewards understanding of why a tool is used, what its assumptions are, and how its output should be interpreted.",
            "Strong answers compare algorithms, databases, scoring systems, and biological meaning.",
        ],
        "outcomes": [
            "Use database logic and sequence searching to identify biological relationships.",
            "Explain pairwise and multiple alignment in functional and evolutionary analysis.",
            "Interpret phylogeny, structure prediction, and structural databases.",
            "Connect docking, QSAR, machine learning, and algorithm design to real applications.",
        ],
        "unit_notes": [
            {
                "title": "Unit 1: Sequence Analysis Foundations",
                "summary": "This unit introduces data resources and alignment logic.",
                "deep_dive": [
                    "DNA and protein databases are useful only when the user understands annotation quality, redundancy, and search purpose.",
                    "Global alignment is better when sequences are comparable across full length, whereas local alignment is better when searching for conserved regions inside otherwise different sequences.",
                    "Substitution matrices such as PAM help score biologically plausible amino-acid changes rather than treating every mismatch equally.",
                    "BLAST is one of the most widely used similarity-search tools because it balances speed with biologically meaningful local alignment discovery.",
                ],
                "example": "Example: A newly sequenced bacterial gene with unknown function can be searched against protein databases with BLAST to find homologs and infer likely function.",
                "exam_focus": [
                    "Differentiate alignment from database search.",
                    "Define homology carefully: sequences are homologous or not; they are not 'more homologous' based on score alone.",
                ],
            },
            {
                "title": "Unit 2: Multiple Alignment and Structural Context",
                "summary": "This unit turns one comparison into family-level interpretation.",
                "deep_dive": [
                    "Multiple sequence alignment highlights conserved motifs, family-level variation, and candidate functional residues.",
                    "Conservation scores matter because highly conserved positions often suggest structural or catalytic importance.",
                    "Hydrophobicity profiles and secondary-structure prediction provide low-cost structural clues when experimental structures are absent.",
                    "Protein Data Bank resources and visualization tools make structure-function interpretation far more concrete than sequence inspection alone.",
                ],
                "example": "Example: Conserved glycine or catalytic serine residues seen across a family can guide mutagenesis or annotation decisions.",
                "exam_focus": [
                    "Explain why multiple alignment often precedes phylogenetic analysis.",
                    "Use structure vocabulary such as motif, domain, fold, and contact map carefully.",
                ],
            },
            {
                "title": "Unit 3: Protein Structural Analysis",
                "summary": "This unit focuses on what structure can reveal about function and stability.",
                "deep_dive": [
                    "Protein structure prediction is most useful when interpreted as a hypothesis to test, not as automatic proof.",
                    "Stability depends on hydrophobic packing, hydrogen bonding, salt bridges, flexibility, and solvent exposure.",
                    "Mutation analysis asks whether a residue supports catalysis, core packing, interface formation, or allosteric communication.",
                    "Binding-site residues often cluster in pockets or interfaces and can be inferred from conservation, structure, or docking studies.",
                ],
                "example": "Example: A mutation from a buried hydrophobic residue to a charged residue can destabilize the protein core and lower functional activity.",
                "exam_focus": [
                    "Always connect mutation effect to structure and then to phenotype.",
                    "Do not confuse stability prediction with complete functional explanation.",
                ],
            },
            {
                "title": "Unit 4: Drug Design, Algorithms, and Machine Learning",
                "summary": "This unit applies computational reasoning to discovery and prediction.",
                "deep_dive": [
                    "Docking estimates how a ligand can fit into a target binding site and is commonly used for ranking hypotheses rather than replacing experiments.",
                    "QSAR links molecular descriptors to biological activity and is most useful when model assumptions and training data are appropriate.",
                    "Algorithm development in bioinformatics emphasizes speed, scalability, scoring logic, and biological relevance.",
                    "Machine learning can support classification, prediction, and prioritization, but the output quality still depends on training data quality and validation design.",
                ],
                "example": "Example: A docking-first screen can narrow a chemical library, but biochemical assays are still needed to confirm actual binding and inhibition.",
                "exam_focus": [
                    "Distinguish in silico prioritization from experimental validation.",
                    "If asked about WEKA or machine learning, mention preprocessing, features, training, testing, and evaluation.",
                ],
            },
        ],
        "applications": [
            "Genome annotation, pathogen tracking, and variant interpretation use database and alignment logic daily.",
            "Structure-based drug discovery and mutational analysis depend on computational prioritization before wet-lab validation.",
            "Comparative genomics and phylogeny help reveal function, origin, and family relationships across species.",
        ],
        "worked_examples": [
            {
                "title": "Worked Example 1: Which alignment should you choose?",
                "body": "Use global alignment when two full-length orthologous proteins are being compared. Use local alignment when searching a domain or short conserved motif in a large database.",
            },
            {
                "title": "Worked Example 2: How to interpret a BLAST hit responsibly",
                "body": "Do not stop at the top hit. Check query coverage, identity, conserved domain context, organism relevance, and whether the annotation is experimentally supported or only predicted.",
            },
        ],
        "question_paper": {
            "Section A: Short answers": [
                {
                    "q": "What does BLAST do?",
                    "a": "BLAST searches sequence databases for local similarity matches and reports statistically meaningful alignments that help infer function or relationship.",
                },
                {
                    "q": "Differentiate global and local alignment.",
                    "a": "Global alignment compares sequences across their full lengths, while local alignment finds the best matching regions within sequences.",
                },
                {
                    "q": "What is a conservation score?",
                    "a": "A conservation score measures how strongly a residue or position is preserved across aligned sequences, often indicating functional or structural importance.",
                },
                {
                    "q": "What is QSAR?",
                    "a": "QSAR is quantitative structure-activity relationship analysis, which relates molecular properties to biological activity using mathematical or statistical models.",
                },
            ],
            "Section B: Medium answers": [
                {
                    "q": "Write a note on multiple sequence alignment.",
                    "a": "Multiple sequence alignment places three or more related sequences into a common framework so that conserved motifs, insertions, deletions, and functionally important residues can be recognized. It is often the basis for phylogeny, motif analysis, and domain interpretation.",
                },
                {
                    "q": "Why is the Protein Data Bank important in bioinformatics?",
                    "a": "The Protein Data Bank stores experimentally determined three-dimensional structures that help researchers interpret function, binding, domain architecture, conformational change, and mutation effects.",
                },
                {
                    "q": "Discuss the limitations of docking studies.",
                    "a": "Docking simplifies dynamic biology into a computational model. Scoring functions, protein flexibility, solvent effects, and incomplete structural knowledge can all limit prediction quality. Docking is therefore best used for prioritization rather than final proof.",
                },
            ],
            "Section C: Long answers": [
                {
                    "q": "Discuss sequence databases, alignment methods, and BLAST as core tools of bioinformatics.",
                    "a": "A full answer should cover database types, sequence search purpose, local versus global alignment, scoring matrices, significance, and biological interpretation. The strongest answers explain not just what BLAST does, but how its output must be judged using coverage, identity, and context.",
                },
                {
                    "q": "Explain how bioinformatics supports protein structure prediction and computer-aided drug design.",
                    "a": "Bioinformatics supports protein structure prediction through sequence analysis, template comparison, domain recognition, and structural modeling. In drug design it supports target analysis, binding-site discovery, docking, virtual screening, and activity prediction, all of which help prioritize experimental work.",
                },
            ],
        },
        "source_labels": [
            "NCBI BLAST documentation and handbook material",
            "EMBL-EBI training on sequence alignment and phylogeny",
            "RCSB PDB structural data and educational resources",
        ],
    },
    {
        "code": "PHDLS104",
        "title": "Applied Environmental Microbiology",
        "credits": 3,
        "hours": "L:3 T:0 P:0",
        "focus": "An application-oriented paper on microbes in ecosystems, waste systems, and environmental monitoring.",
        "why_it_matters": [
            "Microbes drive nutrient cycling, degradation, ecological balance, and many water and waste processes central to public health.",
            "This paper rewards answers that connect microbial physiology to environmental function.",
            "The best responses use systems thinking: organism, environment, process, and outcome.",
        ],
        "outcomes": [
            "Explain microbial cell structure, energetics, and metabolism in ecological context.",
            "Describe environmental effects on microbial growth and community behavior.",
            "Interpret wastewater, drinking water, and bioremediation microbiology.",
            "Connect biosensors and introductory bioinformatics to environmental problem-solving.",
        ],
        "unit_notes": [
            {
                "title": "Unit 1: Cell Structure, Energetics, and Metabolism",
                "summary": "This unit builds the metabolic language of environmental microbiology.",
                "deep_dive": [
                    "Environmental microbiology begins by understanding how microbes obtain energy, carbon, and electrons under real-world constraints.",
                    "Aerobic and anaerobic pathways shape where microbes can live and what ecological service they can provide.",
                    "Phototrophy, chemolithotrophy, nitrate reduction, sulfate reduction, acetogenesis, and methanogenesis reflect environmental adaptation rather than textbook trivia.",
                    "Microscopy helps connect invisible processes to observable morphology and community organization.",
                ],
                "example": "Example: Methanogenic consortia in anaerobic digesters convert complex organic inputs into methane through linked microbial metabolisms.",
                "exam_focus": [
                    "Relate metabolism to habitat and not as a disconnected list.",
                    "Define redox relevance when writing about environmental energetics.",
                ],
            },
            {
                "title": "Unit 2: Ecology, Genetics, and Mutation",
                "summary": "This unit explains how microbial communities change, adapt, and exchange information.",
                "deep_dive": [
                    "Microbial populations exist within communities, guilds, and microenvironments, so local conditions often matter more than bulk averages.",
                    "Horizontal gene transfer accelerates adaptation in environmental settings and can spread catabolic traits or resistance traits.",
                    "Mutation and recombination create diversity, but selection determines persistence under specific environmental pressure.",
                    "Symbiosis, viral influence, and niche partitioning all shape community composition and function.",
                ],
                "example": "Example: Pollutant-rich environments may select for microbes carrying plasmid-borne degradation pathways, increasing remediation capacity over time.",
                "exam_focus": [
                    "When asked about ecology, mention surfaces, gradients, and microenvironments.",
                    "Do not discuss mutation without linking it to selection and outcome.",
                ],
            },
            {
                "title": "Unit 3: Environmental Microbiology and Wastewater Treatment",
                "summary": "This unit brings microbial ecology into environmental engineering and public health.",
                "deep_dive": [
                    "Sampling strategy strongly affects interpretation because environmental microbial communities are spatially and temporally variable.",
                    "Culture-based tools are useful but incomplete because many environmentally relevant microbes are not easily cultured.",
                    "Bioremediation uses microorganisms to transform or reduce contaminants and works best when environmental conditions support microbial activity.",
                    "Wastewater microbiology depends on microbial consortia that degrade organics, transform nitrogen species, and influence sludge behavior.",
                    "Drinking water microbiology adds another layer by focusing on pathogen control, instability, and distribution-system safety.",
                ],
                "example": "Example: Nitrifying communities convert ammonia to nitrite and nitrate in treatment systems, but process efficiency can collapse if oxygen, pH, or toxicity shifts beyond acceptable range.",
                "exam_focus": [
                    "Differentiate wastewater treatment from drinking-water monitoring.",
                    "Use one process example such as nitrification, anaerobic digestion, or bioremediation.",
                ],
            },
            {
                "title": "Unit 4: Waste Microbiology, Biosensors, and Bioinformatics",
                "summary": "The final unit moves from ecology into surveillance and applied monitoring.",
                "deep_dive": [
                    "Solid waste systems host dynamic microbial succession, gas production, leachate generation, and antimicrobial-resistance concerns.",
                    "Biosensors translate biological recognition into a measurable signal and are increasingly useful in pollutant, pathogen, and exposure monitoring.",
                    "Environmental bioinformatics supports sequence annotation, diversity analysis, and functional prediction from environmental datasets.",
                    "The built environment and exposome perspective broaden microbiology from waste sites into everyday human surroundings.",
                ],
                "example": "Example: A biosensor can be used to detect heavy metal exposure or microbial contamination faster than a full classical culture workflow in some monitoring contexts.",
                "exam_focus": [
                    "Define biosensor using recognition element plus signal transduction.",
                    "Treat antimicrobial resistance as an ecological and public-health issue.",
                ],
            },
        ],
        "applications": [
            "Wastewater treatment, solid-waste management, and industrial remediation all depend on environmental microbial processes.",
            "Water-quality surveillance, biosensor development, and environmental genomics are core modern applications.",
            "Environmental microbiology also informs climate, agriculture, and public-health interventions.",
        ],
        "worked_examples": [
            {
                "title": "Worked Example 1: Why culture-independent tools matter",
                "body": "Many environmental organisms are unculturable under standard lab conditions. Sequencing-based approaches reveal hidden diversity and functional capacity that classical plating alone would miss.",
            },
            {
                "title": "Worked Example 2: Bioremediation logic",
                "body": "If contaminants are present but oxygen, nutrients, moisture, or suitable microbes are lacking, remediation may fail. The process is biological, but it still depends on engineering control of conditions.",
            },
        ],
        "question_paper": {
            "Section A: Short answers": [
                {
                    "q": "What is bioremediation?",
                    "a": "Bioremediation is the use of microorganisms to reduce, transform, contain, or remove contaminants in soil, water, sediments, or air.",
                },
                {
                    "q": "Why are culture-independent methods important?",
                    "a": "They detect and characterize microbes that are difficult or impossible to grow under routine laboratory conditions.",
                },
                {
                    "q": "Define microenvironment in microbial ecology.",
                    "a": "A microenvironment is a small local habitat with its own chemical and physical conditions that can differ from the surrounding bulk environment.",
                },
                {
                    "q": "What is a biosensor?",
                    "a": "A biosensor is a device that combines a biological recognition element with a transducer to convert biological interaction into a measurable signal.",
                },
            ],
            "Section B: Medium answers": [
                {
                    "q": "Write a note on horizontal gene transfer in environmental microbiology.",
                    "a": "Horizontal gene transfer moves genetic material between organisms outside parent-offspring inheritance. In the environment it supports rapid adaptation, biodegradation capacity, virulence spread, and antimicrobial-resistance dissemination through transformation, transduction, and conjugation-related processes.",
                },
                {
                    "q": "Discuss microbial roles in wastewater treatment.",
                    "a": "Microbial communities degrade organic matter, transform nitrogen and sulfur compounds, contribute to floc formation, and stabilize sludge. Their activity determines treatment efficiency, odor, gas production, and final effluent quality.",
                },
                {
                    "q": "Explain microbial instability in drinking water systems.",
                    "a": "Instability arises when community composition shifts because of disinfectant decay, nutrient availability, pipe surface biofilms, hydraulic conditions, or contamination events. These shifts can affect safety, taste, and pathogen risk.",
                },
            ],
            "Section C: Long answers": [
                {
                    "q": "Describe environmental microbiology approaches used for sampling, detection, isolation, and analysis.",
                    "a": "A high-quality answer should integrate field sampling design, culture-based methods, microscopy, molecular detection, sequencing, annotation, quantification, and interpretation limits. The best answers note that method choice depends on whether the goal is detection, diversity mapping, or functional inference.",
                },
                {
                    "q": "Discuss the role of microbes in bioremediation and environmental sustainability.",
                    "a": "Microbes transform contaminants by metabolism or co-metabolism and can support removal of metals, hydrocarbons, and other pollutants. Sustainability depends on ecological compatibility, monitoring, and maintaining the environmental conditions that allow the relevant microbial processes to continue effectively.",
                },
            ],
        },
        "source_labels": [
            "US EPA bioremediation resources",
            "EPA water and wastewater information",
            "Environmental microbiology references from the attached syllabus",
        ],
    },
    {
        "code": "PHDLS105",
        "title": "Advanced Enzymology",
        "credits": 2,
        "hours": "L:2 T:0 P:0",
        "focus": "A compact but high-value subject on catalysis, kinetics, regulation, and industrial deployment.",
        "why_it_matters": [
            "Enzymology sits at the core of metabolism, diagnostics, biotechnology, and industrial processing.",
            "Because the paper is only two credits, answers must be concise but conceptually sharp.",
            "The best answers link mechanism to measurable kinetics and then to application.",
        ],
        "outcomes": [
            "Explain enzyme characteristics, classification, assay logic, and purification.",
            "Interpret Michaelis-Menten behavior, inhibition, and catalytic mechanisms.",
            "Discuss allosteric regulation, covalent modification, and immobilization.",
            "Connect industrial enzyme use to food, dairy, textile, and processing sectors.",
        ],
        "unit_notes": [
            {
                "title": "Unit 1: Introduction, Classification, and Purification",
                "summary": "This unit defines the enzyme as both molecule and measurable catalyst.",
                "deep_dive": [
                    "Enzymes accelerate reactions by lowering activation barriers without being consumed in the net process.",
                    "Classification organizes enzymes by reaction type and helps students reason about biochemical role, not merely memorize code numbers.",
                    "Enzyme assays quantify activity, and activity matters more than protein amount alone when judging functional preparation quality.",
                    "Purification logic depends on differences in solubility, charge, affinity, size, or localization.",
                    "Isoenzymes, ribozymes, abzymes, and multifunctional enzymes expand the classical picture of catalysis.",
                ],
                "example": "Example: A purified enzyme fraction may show less total protein than a crude extract but higher specific activity, indicating enrichment of catalytic function.",
                "exam_focus": [
                    "Differentiate enzyme amount from enzyme activity.",
                    "Always define specific activity when writing on purification.",
                ],
            },
            {
                "title": "Unit 2: Kinetics, Inhibition, and Catalytic Mechanisms",
                "summary": "This is the mathematical and mechanistic core of the subject.",
                "deep_dive": [
                    "Michaelis-Menten kinetics describes how velocity changes with substrate concentration under defined assumptions.",
                    "Km is not simply a measure of enzyme speed; it is often used as a practical indicator of substrate concentration at half-maximal velocity and can reflect effective binding behavior in context.",
                    "Vmax reflects the maximum rate under saturating substrate conditions.",
                    "Competitive inhibition raises apparent substrate requirement, while noncompetitive and related allosteric effects change the catalytic picture differently.",
                    "Lineweaver-Burk and related plots help estimate kinetic parameters, but conceptual interpretation is more important than memorizing graph shapes alone.",
                ],
                "example": "Example: If two inhibitors produce different changes in apparent kinetics, that difference suggests whether the inhibitor blocks the active site or acts through a distinct regulatory site.",
                "exam_focus": [
                    "State assumptions before using the Michaelis-Menten equation.",
                    "Explain inhibition using both binding logic and kinetic consequence.",
                ],
            },
            {
                "title": "Unit 3: Regulation and Immobilized Enzymes",
                "summary": "This unit explains how cells and industries control catalytic performance.",
                "deep_dive": [
                    "Allosteric regulation allows enzyme activity to respond rapidly to metabolic conditions.",
                    "Covalent modification and proteolytic activation provide switch-like control in many pathways.",
                    "Feedback inhibition is efficient because end products can throttle earlier committed steps.",
                    "Immobilization improves reusability, process control, and separation, though it may reduce flexibility or activity depending on method.",
                ],
                "example": "Example: An immobilized enzyme reactor can be reused repeatedly in industry, lowering downstream contamination and simplifying continuous processing.",
                "exam_focus": [
                    "Define allostery through conformational change, not only through the word 'inhibitor'.",
                    "Mention both benefits and tradeoffs of immobilization.",
                ],
            },
            {
                "title": "Unit 4: Commercial Enzyme Production and Processing",
                "summary": "The paper ends by showing why enzyme science matters beyond the classroom.",
                "deep_dive": [
                    "Industrial enzymes are chosen for specificity, mild operating conditions, and process efficiency.",
                    "Food and beverage applications include juice clarification, baking optimization, flavor development, and fermentation support.",
                    "Dairy enzymes support coagulation, ripening, and product standardization.",
                    "Textile and detergent applications use enzymes for stain breakdown, fabric treatment, and energy-efficient processing.",
                ],
                "example": "Example: Proteases in detergents help remove protein-based stains at lower temperatures, making the process more energy-efficient than harsher chemical alternatives alone.",
                "exam_focus": [
                    "Industrial answers must include why enzymes are preferred operationally.",
                    "Use industry examples rather than generic statements about 'commercial importance'.",
                ],
            },
        ],
        "applications": [
            "Clinical diagnostics, metabolic studies, and drug discovery all use enzyme kinetics and inhibition logic.",
            "Immobilized enzymes are important in biosensors, bioreactors, and industrial processing.",
            "Food technology, textiles, detergents, and biotechnology all depend on commercial enzyme optimization.",
        ],
        "worked_examples": [
            {
                "title": "Worked Example 1: Specific activity as a purification indicator",
                "body": "If total protein falls after purification but activity per milligram rises, the preparation is likely enriched for the enzyme of interest.",
            },
            {
                "title": "Worked Example 2: Why industrial enzymes need stability",
                "body": "An industrial enzyme must tolerate the process environment. A highly active enzyme with poor pH or temperature stability can be less useful than a slightly slower but robust catalyst.",
            },
        ],
        "question_paper": {
            "Section A: Short answers": [
                {
                    "q": "What is specific activity?",
                    "a": "Specific activity is enzyme activity per unit mass of total protein and is commonly used to judge purification progress.",
                },
                {
                    "q": "Define Km.",
                    "a": "Km is the substrate concentration at which reaction velocity reaches half of Vmax under Michaelis-Menten conditions.",
                },
                {
                    "q": "What is feedback inhibition?",
                    "a": "Feedback inhibition is regulation in which a pathway end product inhibits an earlier enzyme step to control pathway output.",
                },
                {
                    "q": "What is enzyme immobilization?",
                    "a": "It is the attachment or confinement of enzymes to a solid support or matrix so they can be reused or better controlled.",
                },
            ],
            "Section B: Medium answers": [
                {
                    "q": "Differentiate competitive and noncompetitive inhibition.",
                    "a": "Competitive inhibition involves binding at or near the active site and can often be overcome by raising substrate concentration. Noncompetitive inhibition involves binding at a distinct site and alters catalytic behavior without being displaced simply by more substrate.",
                },
                {
                    "q": "Write a note on allosteric enzymes.",
                    "a": "Allosteric enzymes respond to effector binding at regulatory sites separate from the active site. This causes conformational change and often produces cooperative or sigmoidal behavior, making them useful control points in metabolism.",
                },
                {
                    "q": "Discuss industrial uses of enzymes in food processing.",
                    "a": "Enzymes improve yield, texture, flavor, clarity, and efficiency in industries such as juice processing, baking, brewing, dairy processing, and cheese ripening. Their selectivity reduces unnecessary side reactions.",
                },
            ],
            "Section C: Long answers": [
                {
                    "q": "Explain Michaelis-Menten kinetics, enzyme inhibition, and the importance of kinetic parameters.",
                    "a": "A strong answer should define the steady-state view, describe the hyperbolic relationship between substrate concentration and velocity, explain Km and Vmax, and then show how inhibitors alter apparent kinetics. The discussion becomes stronger when kinetic behavior is tied to mechanism and application.",
                },
                {
                    "q": "Discuss enzyme regulation and immobilization with applications.",
                    "a": "Enzyme regulation includes allostery, product inhibition, feedback inhibition, covalent modification, and proteolytic activation. Immobilization adds process control, reuse, and easy separation in biotechnology and industry, although mass-transfer issues or conformational restriction can lower activity.",
                },
            ],
        },
        "source_labels": [
            "NCBI Bookshelf material on enzyme inhibition",
            "Thermo Fisher application material on enzyme kinetics",
            "Attached syllabus references for industrial enzymes",
        ],
    },
    {
        "code": "PHDLS106",
        "title": "Applied Zoology and Toxicology",
        "credits": 3,
        "hours": "L:3 T:0 P:0",
        "focus": "A hybrid paper covering applied zoological relevance and toxicological reasoning.",
        "why_it_matters": [
            "The zoology component translates animal diversity into economic, medical, and public-health importance.",
            "The toxicology component trains students to think in terms of exposure, dose, response, mechanism, and risk.",
            "This paper rewards structured answers and careful terminology.",
        ],
        "outcomes": [
            "Explain host-parasite and vector-related terminology and significance.",
            "Discuss economically useful insects and their applied value.",
            "Interpret medical zoology examples and control measures.",
            "Explain toxicity, dose-response logic, and mechanisms of toxic action.",
        ],
        "unit_notes": [
            {
                "title": "Unit 1: Introduction to Applied Zoology",
                "summary": "This unit builds the conceptual language of parasite-host relationships.",
                "deep_dive": [
                    "Applied zoology studies animals and animal-associated organisms in relation to economy, agriculture, medicine, and human welfare.",
                    "Terms such as host, definitive host, intermediate host, vector, carrier, reservoir, parasitism, commensalism, and zoonosis must be used precisely because they describe different epidemiological roles.",
                    "Vectors and carriers are not interchangeable in every context; the answer improves when the mode of transmission is clear.",
                ],
                "example": "Example: A mosquito can act as a vector because it transmits a pathogen between hosts, while a reservoir host maintains the pathogen in nature.",
                "exam_focus": [
                    "Define the terms cleanly before giving examples.",
                    "Do not mix host categories or ecological relationships.",
                ],
            },
            {
                "title": "Unit 2: Economic Zoology",
                "summary": "This unit connects life cycles and husbandry with livelihoods, materials, and ecosystem services.",
                "deep_dive": [
                    "Sericulture links the biology of silkworms with cocoon production, fibre quality, disease management, and rural livelihoods. A strong answer connects the organism's life cycle to the product rather than only naming silk.",
                    "Apiculture contributes honey, wax, and pollination services. Its applied significance therefore includes crop productivity and ecological function, not only harvested products.",
                    "Lac-culture uses scale insects for natural resin production, while vermiculture uses earthworms to transform biodegradable organic material into a stable nutrient-rich amendment.",
                    "Economic zoology is evaluated by productivity, biological constraints, product quality, environmental effects, and the feasibility of management practices.",
                ],
                "example": "Example: In vermiculture, excessive heat, unsuitable moisture, or poor feedstock can lower worm activity and reduce compost quality; biology directly determines process output.",
                "exam_focus": [
                    "Use the chain organism, life cycle, product or service, management, and economic value.",
                    "Do not write economic importance as a disconnected list of products.",
                ],
            },
            {
                "title": "Unit 3: Medical Zoology",
                "summary": "This unit requires biology-led control: identify the pest, understand its ecology, then interrupt the relevant stage.",
                "deep_dive": [
                    "Medical zoology examines organisms that cause direct harm, act as vectors, or create conditions that increase disease transmission. The answer should distinguish direct infestation from pathogen transmission.",
                    "Pediculus humanus capitis and P. humanus corporis differ in ecology and public-health relevance; accurate identification changes the control approach.",
                    "Anopheles, Aedes, and Culex are compared most usefully by breeding site, feeding and resting behavior, disease association, and control implication. Memorized names without ecology do not create a usable public-health answer.",
                    "Xenopsylla cheopis illustrates why flea control may require attention to hosts, housing, sanitation, and reservoir dynamics, rather than a single chemical intervention.",
                ],
                "example": "Example: Aedes control strategies focus heavily on source reduction of container-breeding sites because its ecology differs from Anopheles or Culex systems.",
                "exam_focus": [
                    "Use one table mentally: organism, importance, damage or transmission, and control.",
                    "Applied answers are stronger when prevention is described alongside biology.",
                ],
            },
            {
                "title": "Unit 4: Introduction to Toxicology",
                "summary": "This unit introduces how harmful effects are studied and interpreted.",
                "deep_dive": [
                    "Toxicity depends on exposure route, dose, duration, frequency, and the biological handling of the substance.",
                    "A substance must first contact the body through an exposure pathway before toxic effect can occur.",
                    "Acute and chronic exposure are different both in duration and in the types of outcomes they may produce.",
                    "Tolerance, addiction, and interactions among xenobiotics complicate simple one-agent explanations.",
                ],
                "example": "Example: The same chemical may produce different outcomes if inhaled repeatedly at low dose versus ingested once at high dose.",
                "exam_focus": [
                    "Use the order route, dose, duration, effect whenever you write toxicology answers.",
                    "Mention xenobiotic interaction when asked about real-world toxic risk.",
                ],
            },
            {
                "title": "Unit 5: Evaluation of Toxicity",
                "summary": "This unit asks how toxic effects are measured, compared, and interpreted without overclaiming what one number means.",
                "deep_dive": [
                    "Dose-response relationships help estimate how biological effect changes with exposure level.",
                    "Graded responses describe changing intensity in an individual system, while quantal responses describe the proportion of a population showing a defined endpoint. The distinction matters when reading dose-response graphs.",
                    "LD50, LC50, TD50, and therapeutic index summarize defined experimental outcomes. They are comparative hazard measures, not complete statements of human safety or environmental risk.",
                    "Assumptions behind a curve - exposure accuracy, endpoint definition, population relevance, and model selection - should be stated when interpreting toxicity data.",
                ],
                "example": "Example: Two compounds with the same LD50 may differ substantially in chronic effects, exposure route, persistence, or susceptible populations; their real-world risk can therefore differ.",
                "exam_focus": [
                    "Do not treat LD50 as a complete statement of safety.",
                    "Define the endpoint and conditions before interpreting any toxicity metric.",
                ],
            },
            {
                "title": "Unit 6: Mechanism of Toxicity",
                "summary": "Mechanistic toxicology traces the journey from external agent to molecular injury and possible detoxification.",
                "deep_dive": [
                    "Mechanism of toxicity includes absorption, distribution, metabolic activation or detoxification, target interaction, cellular disturbance, tissue injury, and observable outcome.",
                    "The ultimate toxicant idea is important because the administered compound may not be the chemically active damaging form. Metabolism can detoxify an agent or create a more reactive intermediate.",
                    "Mechanistic claims become stronger when they distinguish correlation from causation and identify measurable biomarkers at more than one stage of the pathway.",
                    "Host genetics, nutritional state, co-exposures, and organ function can alter both toxicant handling and susceptibility.",
                ],
                "example": "Example: A parent xenobiotic may become more toxic after biotransformation if reactive metabolites are produced faster than detoxification pathways can neutralize them.",
                "exam_focus": [
                    "Mechanism answers should show movement from exposure to damage.",
                    "Include a detoxification or susceptibility factor; do not write a one-direction story.",
                ],
            },
        ],
        "applications": [
            "Vector control, parasitology, public health, and rural economic systems all use applied zoology knowledge.",
            "Toxicology supports risk assessment, poison management, occupational health, and environmental safety.",
            "Dose-response and mechanism concepts are essential for interpreting chemical hazard logically rather than emotionally.",
        ],
        "worked_examples": [
            {
                "title": "Worked Example 1: Why route of exposure matters",
                "body": "An ingested compound may undergo first-pass metabolism, while an inhaled compound may reach systemic circulation or lung tissue more directly. That difference can change both potency and target organ effects.",
            },
            {
                "title": "Worked Example 2: Why therapeutic index matters",
                "body": "A compound with beneficial effect at one dose but serious toxicity near that dose has a narrow safety margin. Therapeutic index gives a quick conceptual handle on that margin.",
            },
        ],
        "question_paper": {
            "Section A: Short answers": [
                {
                    "q": "Define zoonosis.",
                    "a": "Zoonosis is a disease or infection that is naturally transmissible between vertebrate animals and humans.",
                },
                {
                    "q": "What is LD50?",
                    "a": "LD50 is the dose of a substance expected to cause death in 50 percent of a test population under defined conditions.",
                },
                {
                    "q": "Differentiate vector and reservoir.",
                    "a": "A vector transmits the pathogen between hosts, while a reservoir maintains the pathogen in nature over time.",
                },
                {
                    "q": "What is a xenobiotic?",
                    "a": "A xenobiotic is a foreign chemical substance not normally produced or expected to be present in the organism.",
                },
            ],
            "Section B: Medium answers": [
                {
                    "q": "Write a note on economic insects.",
                    "a": "Economic insects are insects with practical value in production systems or livelihoods. Sericulture, apiculture, lac-culture, and related practices provide silk, honey, wax, resin, pollination support, and rural economic value.",
                },
                {
                    "q": "Explain acute and chronic exposure in toxicology.",
                    "a": "Acute exposure occurs over a short period, often within 24 hours, and may cause rapid effects. Chronic exposure occurs over weeks, months, or years and may produce cumulative or delayed outcomes depending on the toxicant and target tissue.",
                },
                {
                    "q": "Discuss dose-response relationship.",
                    "a": "Dose-response relationship describes how biological effect changes as dose changes. It helps identify thresholds, potency, comparative hazard, and the conditions under which a substance becomes significantly harmful.",
                },
            ],
            "Section C: Long answers": [
                {
                    "q": "Discuss applied zoology with special reference to host-parasite relationships, vectors, and economically important insects.",
                    "a": "A complete answer should define major host-parasite terms, explain why vectors matter in disease transmission, and then move into economic zoology examples such as sericulture, apiculture, lac-culture, and vermiculture. Applied significance should be emphasized throughout.",
                },
                {
                    "q": "Explain modern toxicology, evaluation of toxicity, and mechanisms of toxic action.",
                    "a": "A full answer should define toxicology, explain route and duration of exposure, describe dose-response logic and measures such as LD50 or therapeutic index, and then trace the progression from toxicant entry to activation, target interaction, tissue damage, and detoxification.",
                },
            ],
        },
        "source_labels": [
            "ATSDR/CDC toxicology curriculum resources",
            "Occupational safety references on LD50 concepts",
            "Attached syllabus toxicology reference list",
        ],
    },
]


# These layers turn a topic list into a study sequence: intuition, mechanism,
# evidence, and exam expression. They complement the official syllabus units.
MASTERCLASS_LAYERS = {
    "PHDLS101": {
        "thesis": "Analytical science is a chain of decisions: preserve the sample, separate what matters, detect it reliably, and interpret the signal within its limits.",
        "analogy": "Think of a complex biological sample as a crowded railway station. Centrifugation sorts passengers by how quickly they settle, chromatography sends them through different gates based on a property, and detection identifies the right passenger after separation.",
        "reasoning": [
            "Start with the biological question: amount, identity, location, interaction, or activity.",
            "Choose a separation principle that matches the molecular difference: size, charge, affinity, volatility, or density.",
            "Choose a detector that supplies the needed evidence: absorbance, fluorescence, antibody specificity, mass, or image.",
            "Use controls and standards so the signal can be trusted rather than merely observed.",
            "Report both what the technique supports and what it cannot prove alone.",
        ],
        "case": {
            "title": "Research case: Is a stress-response protein genuinely increased?",
            "prompt": "A cell line appears to produce more of a protein after oxidative stress. Design an evidence chain that distinguishes increased abundance from a loading or antibody artifact.",
            "answer": "Extract equal amounts of protein under matched conditions, quantify total protein with a compatible assay, separate samples by SDS-PAGE, and probe by western blot using a validated primary antibody. Include a loading control or total-protein normalization, biological replicates, and a no-primary-antibody control. Densitometry may support a relative increase, but it does not by itself establish altered transcription, direct causation, or cell-to-cell heterogeneity. qPCR, microscopy, or flow cytometry can answer those different questions.",
        },
        "blueprint": ["Define the technique and its governing principle.", "Draw or describe the instrument/workflow in ordered steps.", "State the nature of the output and how it is interpreted.", "Give one research or clinical application.", "Close with one limitation and a control or complementary method."],
        "viva": [("Why is an A280 value not automatically a pure-protein measurement?", "Nucleic acids and some contaminants can absorb near UV wavelengths, so absorbance must be interpreted with purity checks and appropriate blanks."), ("Why is a western blot more specific than SDS-PAGE?", "SDS-PAGE resolves proteins mainly by apparent size, whereas western blotting adds antibody-based recognition of a target."), ("When would you choose density-gradient centrifugation?", "When a crude pellet is insufficient and components need higher-resolution separation by sedimentation behavior or buoyant density.")],
        "sources": [("NCBI: cell fractionation and protein separation", "https://www.ncbi.nlm.nih.gov/books/NBK26936/"), ("NCBI: chromatography principles", "https://www.ncbi.nlm.nih.gov/books/NBK599545/")],
    },
    "PHDLS102": {
        "thesis": "Biomolecular function is not contained in a name or formula alone: it emerges from chemical groups, three-dimensional arrangement, environment, and molecular partners.",
        "analogy": "A protein is like a precision-folded key made from amino-acid letters. Changing one letter, the pH, or the folding conditions can reshape the key enough that it no longer fits its molecular lock.",
        "reasoning": [
            "Identify the building blocks and the covalent bonds that make the polymer.",
            "Explain the noncovalent forces that organize the molecule in water.",
            "Connect structure at the active or binding site to a measurable function.",
            "Show how mutation, misfolding, altered pH, or abnormal modification disrupts that function.",
            "Use an experimental method that can test the proposed structure-function link.",
        ],
        "case": {
            "title": "Research case: From amino-acid substitution to disease phenotype",
            "prompt": "Explain how one amino-acid substitution can cause disease without claiming that every mutation has the same effect.",
            "answer": "A substitution may alter charge, size, hydrophobicity, flexibility, or a chemically essential side chain. If it occurs in a buried core, binding interface, active site, or regulatory region, it can change folding, stability, localization, ligand affinity, or activity. The consequence must be tested rather than assumed: compare wild-type and variant protein abundance, structure or stability, biochemical activity, and cellular phenotype. The same substitution class can be benign in one position and severe in another because protein context matters.",
        },
        "blueprint": ["Name the biomolecule and define the structural level under discussion.", "Describe the key bonds and stabilizing interactions.", "Trace the structure-to-function relationship with a named example.", "Add a health or disease consequence.", "End with a method used to study or validate the relationship."],
        "viva": [("Why does primary sequence matter after a protein has folded?", "The sequence encodes side-chain chemistry and constrains the interactions that create and maintain the folded state."), ("Why are hydrophobic residues often buried in soluble proteins?", "Burying nonpolar groups reduces unfavorable ordering of surrounding water and helps stabilize a compact fold."), ("What does a Ramachandran plot tell you?", "It displays sterically allowed backbone dihedral-angle combinations and is used to assess conformational plausibility in protein structures.")],
        "sources": [("NCBI: molecular composition of cells", "https://www.ncbi.nlm.nih.gov/books/NBK9879/"), ("NCBI: tertiary protein structure", "https://www.ncbi.nlm.nih.gov/books/NBK470269/")],
    },
    "PHDLS103": {
        "thesis": "Bioinformatics converts biological sequences and structures into testable hypotheses; a high score is evidence to investigate, not a final biological conclusion.",
        "analogy": "Sequence alignment is like comparing several edited copies of an old manuscript. Matching passages can reveal common ancestry or conserved meaning, but a few shared words do not prove the manuscripts have the same purpose.",
        "reasoning": [
            "Start with a well-curated query sequence and state the biological question.",
            "Select the right database and comparison method for nucleotide, protein, domain, or structure evidence.",
            "Inspect coverage, alignment quality, conserved residues, and statistical significance together.",
            "Use multiple sequence alignment before interpreting conserved positions or inferring phylogeny.",
            "Convert computational evidence into a hypothesis that can be checked experimentally.",
        ],
        "case": {
            "title": "Research case: Annotating an unknown bacterial protein",
            "prompt": "A 310-residue bacterial protein returns a BLAST hit with a low E-value but only 28 percent query coverage. What is a defensible interpretation?",
            "answer": "The hit suggests that part of the sequence may be homologous to a known protein or domain, but 28 percent coverage does not justify assigning the entire protein that function. Inspect the aligned region, run a domain search, compare multiple homologues, assess catalytic-residue conservation, and check genomic context if available. The correct conclusion is a qualified hypothesis such as 'contains a region consistent with a candidate domain', followed by an experiment to test activity or binding.",
        },
        "blueprint": ["Define the algorithm or resource and the biological input.", "Explain what is compared and what the score represents.", "State the interpretation criteria, including coverage and significance.", "Give a workflow example from sequence to hypothesis.", "Name an important limitation and an experimental validation step."],
        "viva": [("Why is local alignment useful for domain discovery?", "It can detect a shared high-similarity region even when the rest of two sequences differs."), ("Why should phylogenetic analysis start with a careful multiple alignment?", "The tree inherits the homology assumptions encoded by the alignment; poorly aligned positions can create misleading relationships."), ("What is the danger of annotation transfer?", "A database label can be propagated without direct evidence, so similarity should be checked against domains, residues, coverage, and biology.")],
        "sources": [("EMBL-EBI: guide to sequence analysis", "https://www.ebi.ac.uk/training/online/courses/guide-to-sequence-analysis-tools/introduction/"), ("EMBL-EBI: phylogenetics fundamentals", "https://www.ebi.ac.uk/training/online/courses/introduction-to-phylogenetics/what-is-phylogenetics/")],
    },
    "PHDLS104": {
        "thesis": "Environmental microbiology explains how microbial metabolism transforms matter and energy, and how that capability can be managed for water quality, waste treatment, and remediation.",
        "analogy": "A wastewater reactor is a microbial city. Different populations do different jobs, but the city fails if oxygen, food supply, pH, temperature, or toxic load makes one essential group stop working.",
        "reasoning": [
            "Identify the substrate, electron donor, electron acceptor, and environmental constraints.",
            "Map the microbial metabolism to products, energy yield, and growth.",
            "Relate reactor or ecosystem conditions to which populations can dominate.",
            "Measure a process-relevant output such as oxygen demand, nutrient form, gas, biomass, or sensor signal.",
            "Propose an intervention and predict both benefit and trade-off.",
        ],
        "case": {
            "title": "Research case: Nitrification failure in a treatment system",
            "prompt": "Ammonia rises in the effluent of an aerated biological treatment plant. Build a diagnosis before recommending a fix.",
            "answer": "First verify the ammonia result and review influent loading, dissolved oxygen, pH, temperature, alkalinity, toxic shocks, sludge age, and mixing. Nitrification depends on specialized aerobic organisms and can fail when oxygen is limited, inhibitory compounds enter the system, or growth conditions become unsuitable. A defensible recommendation links each suspected cause to a measurement, then changes one controllable variable while monitoring ammonia, nitrite, nitrate, oxygen, and biomass response. Adding microbes without correcting the operating condition is not automatically a solution.",
        },
        "blueprint": ["Define the environmental process and the organisms involved.", "Describe the relevant metabolic pathway using donor, acceptor, and products.", "State the controlling environmental variables.", "Use a treatment, remediation, or monitoring example.", "End with a measurable performance indicator and limitation."],
        "viva": [("Why is oxygen not simply 'good' for every microbial process?", "Oxygen supports aerobic metabolism but inhibits or changes processes performed by anaerobes; the needed condition depends on the pathway."), ("What does a biosensor contribute beyond a culture test?", "It can provide a rapid, targeted signal, but it requires calibration, validation, and awareness of matrix interference."), ("Why are microbial consortia important in degradation?", "One organism's product may be another's substrate, allowing complex pollutants or waste streams to be transformed through linked metabolisms.")],
        "sources": [("US EPA: bioremediation", "https://www.epa.gov/emergency-response-research/bioremediation"), ("US EPA: wastewater technology fact sheets", "https://www.epa.gov/npdes/wastewater-technology-fact-sheets")],
    },
    "PHDLS105": {
        "thesis": "Enzymology is the quantitative study of biological catalysts: the rate is the observable, but mechanism, regulation, and process design explain the rate.",
        "analogy": "An enzyme is not merely a lock and substrate a key. It is closer to a flexible workstation whose shape, chemistry, cofactor supply, and traffic conditions determine how quickly useful work is completed.",
        "reasoning": [
            "Define the reaction, assay signal, and controlled conditions.",
            "Measure initial rates so substrate depletion and product effects are minimized.",
            "Interpret Km and Vmax as model-derived parameters, not universal labels of enzyme quality.",
            "Compare inhibitor patterns by their effect on apparent kinetic behavior and binding logic.",
            "Connect regulation or immobilization to a real production or diagnostic objective.",
        ],
        "case": {
            "title": "Research case: Identifying a candidate inhibitor",
            "prompt": "An inhibitor lowers product formation. How do you distinguish a competitive inhibitor from an irreversible or noncompetitive effect?",
            "answer": "Measure initial velocity across a substrate range with multiple inhibitor concentrations, keeping enzyme amount and assay time controlled. A competitive pattern can be overcome by sufficiently high substrate and typically changes apparent affinity while leaving the limiting rate unchanged in the ideal model. A pure noncompetitive pattern lowers the limiting rate without changing apparent affinity; irreversible inhibition may persist after inhibitor removal or preincubation. The conclusion should be supported by appropriate kinetic fitting and, when needed, dilution, time-dependence, or binding experiments rather than one graph alone.",
        },
        "blueprint": ["Define the enzyme concept or parameter precisely.", "State the reaction scheme or assay logic.", "Explain the expected kinetic or regulatory effect.", "Use an industrial, clinical, or drug-discovery example.", "Mention assumptions, assay controls, and one limitation."],
        "viva": [("Why use initial velocity in enzyme kinetics?", "It minimizes complications from substrate depletion, reverse reaction, product inhibition, and enzyme instability during the run."), ("Can a low Km alone prove a better enzyme?", "No. It is model- and condition-dependent and must be considered with Vmax, kcat, stability, specificity, and the intended application."), ("What is the main benefit of immobilization?", "It enables catalyst recovery and reuse, but potential diffusion limits and altered conformation must be evaluated.")],
        "sources": [("NCBI: enzyme inhibition", "https://www.ncbi.nlm.nih.gov/books/NBK554481/"), ("NCBI: noncompetitive inhibition", "https://www.ncbi.nlm.nih.gov/books/NBK545242/")],
    },
    "PHDLS106": {
        "thesis": "Applied zoology and toxicology link organism biology to human outcomes: disease transmission, livelihoods, exposure pathways, dose-response, and prevention.",
        "analogy": "Toxicology is a detective story. The chemical is only one suspect; the route, dose, duration, metabolism, target tissue, and host susceptibility determine what actually happens.",
        "reasoning": [
            "Define the organism, agent, or toxicant using correct terminology.",
            "Trace the relevant route: host-vector cycle, exposure pathway, or biological uptake.",
            "Identify the conditions that change risk: behavior, ecology, dose, duration, or susceptibility.",
            "Distinguish hazard from real-world risk using exposure evidence.",
            "Propose prevention or control at the most effective stage of the chain.",
        ],
        "case": {
            "title": "Research case: Same chemical, different outcome",
            "prompt": "Two workers encounter the same solvent, but one develops symptoms after repeated inhalation while the other has no symptoms after a one-time, lower exposure. Explain the comparison scientifically.",
            "answer": "The comparison requires exposure concentration, duration, frequency, route, ventilation, protective equipment, metabolism, health status, and timing of assessment. Repeated inhalation can produce a different absorbed dose and target-organ burden than a single lower event. Symptoms alone do not establish causality, and absence of immediate symptoms does not establish safety. A rigorous assessment combines exposure reconstruction, clinical evaluation, dose-response knowledge, and a search for alternative causes.",
        },
        "blueprint": ["Define the zoological or toxicological term accurately.", "Describe the biological chain from source to host or target tissue.", "Explain factors that modify outcome.", "Give a public-health, occupational, or economic example.", "Conclude with a proportionate prevention or risk-control measure."],
        "viva": [("What is the difference between hazard and risk?", "Hazard is the inherent capacity to cause harm; risk depends on hazard together with the likelihood and magnitude of actual exposure."), ("Why is LD50 not a complete safety assessment?", "It is a defined experimental lethality measure and does not capture all endpoints, exposure routes, species differences, or real-world exposure conditions."), ("Why does vector ecology matter for control?", "Control succeeds when it interrupts the vector's actual breeding, feeding, resting, or transmission behavior rather than applying a generic measure.")],
        "sources": [("ATSDR/CDC: toxicology learning module", "https://www.atsdr.cdc.gov/land-reuse-health-program/media/pdfs/toxicology-508.pdf"), ("WHO: vector-control resources", "https://www.who.int/teams/control-of-neglected-tropical-diseases/vector-ecology-and-management")],
    },
}


ADVANCED_QUESTION_BANK = {
    "PHDLS101": [("A protein preparation gives a clean A280 value but multiple SDS-PAGE bands. Reconcile the observations.", "A280 reports bulk absorbance by chromophores and can estimate total protein under defined assumptions; it does not establish molecular homogeneity. Multiple gel bands indicate proteins of different apparent masses or subunits. The next step is to check blanking and nucleic-acid contamination, quantify purity by densitometry, then select a separation based on a distinct property such as charge, size, or affinity."), ("Compare fluorescence microscopy and confocal microscopy as evidence-generating tools.", "Both use fluorophores to provide molecular specificity. Conventional fluorescence collects light from a broader depth of field, whereas confocal optical sectioning rejects much out-of-focus light and is therefore advantageous for thicker specimens and three-dimensional localization. Neither automatically proves function: controls for fluorophore specificity, bleed-through, photobleaching, and expression artifacts remain essential.")],
    "PHDLS102": [("Use hemoglobin and myoglobin to explain why quaternary structure can change physiological function.", "Myoglobin is a single-chain oxygen-binding protein suited to local storage or facilitated diffusion, while hemoglobin's multiple subunits allow cooperative interactions. Binding at one subunit can alter the conformation and affinity of others, producing a response appropriate for loading and unloading oxygen across changing physiological environments. The comparison shows that subunit arrangement, not only amino-acid composition, shapes function."), ("Explain why a buffer can affect both protein stability and experimental interpretation.", "pH influences ionization of amino-acid side chains, salt bridges, ligand binding, enzyme catalysis, and solubility. A buffer chosen near its useful range stabilizes pH during an assay, but its composition may also bind metals, alter ionic strength, absorb light, or interfere with downstream measurements. Therefore buffer selection is both a biochemical and analytical design choice.")],
    "PHDLS103": [("Why can a statistically impressive BLAST result still be biologically misleading?", "A low E-value supports non-random similarity under the search conditions, but the aligned region may cover only one common domain, the database annotation may be weak, or the sequences may have diverged in function. A responsible interpretation checks query coverage, conserved functional residues, domain architecture, taxonomic context, and independent evidence before transferring a specific function."), ("Outline a defensible workflow from a set of protein sequences to a phylogenetic claim.", "Collect homologous sequences with documented provenance, remove poor or nonhomologous regions, build and inspect a multiple alignment, choose an evolutionary model and tree method appropriate to the data, assess branch support, and state the inference as a hypothesis. The final tree should be interpreted with gene duplication, horizontal transfer, alignment uncertainty, and sampling bias in mind.")],
    "PHDLS104": [("Explain why bioremediation is a managed ecological process rather than simply adding microbes to pollution.", "Bioremediation depends on whether organisms can access the contaminant, obtain suitable electron donors or acceptors, tolerate toxicity, and function under the site's pH, temperature, moisture, and nutrient conditions. Indigenous communities may already have relevant capacity. Good design characterizes the site, selects biostimulation or bioaugmentation only when justified, monitors contaminant transformation and toxicity, and considers incomplete degradation products."), ("Link microbial growth mathematics to wastewater-process control.", "Growth rate, yield, substrate loading, residence time, and decay determine whether functional biomass remains in a reactor. If loading rises faster than the community can process it, oxygen demand and unwanted intermediates can increase. Measurements such as biomass, dissolved oxygen, nutrient species, and effluent quality connect mathematical expectations to operational decisions.")],
    "PHDLS105": [("Explain why a Lineweaver-Burk plot should not be treated as the final authority for kinetic parameters.", "Reciprocal transformation magnifies error at low substrate concentration and can distort visual weighting of data. It remains historically useful for illustrating patterns, but parameter estimates are better supported by fitting the untransformed rate data with an appropriate model, replicates, residual inspection, and clearly stated assay conditions."), ("Design an enzyme-purification strategy and explain how you would judge success.", "Begin with a stable extraction buffer and a specific activity assay. Use an inexpensive bulk step to remove major contaminants, then apply orthogonal separation principles such as ion exchange followed by size exclusion or affinity capture. At every step calculate total activity, total protein, specific activity, yield, and purification fold. A final electrophoretic or mass-based check assesses homogeneity, while activity and stability verify that purification did not destroy function.")],
    "PHDLS106": [("Distinguish an exposure assessment from a toxicity test.", "Exposure assessment estimates who contacted what agent, by which route, at what concentration, frequency, and duration. A toxicity test characterizes biological effects under defined conditions. Risk interpretation requires both: a hazardous agent with negligible exposure may pose low practical risk, while a moderately hazardous agent with repeated high exposure may require urgent control."), ("Develop an integrated vector-control answer for a container-breeding mosquito.", "Begin with surveillance and species-appropriate ecology. Prioritize source reduction by removing or managing water-holding containers, support this with community participation, targeted larval control where needed, protection from bites, and evidence-guided adult control during outbreaks. Monitor breeding indices and disease indicators, and account for insecticide resistance and unintended environmental effects.")],
}


# Every graphic below is instructional: it makes a process, relationship, or
# quantitative pattern visible. None are stock decoration.
VISUAL_LABS = {
    "PHDLS101": {
        "diagram_title": "From biological sample to defensible result",
        "diagram": '''digraph { rankdir=LR; bgcolor="transparent"; node [shape=box style="rounded,filled" fontname="Arial" margin="0.15,0.10"]; sample [label="Biological\nsample" fillcolor="#dbeafe"]; prep [label="Buffer +\npreparation" fillcolor="#fef3c7"]; split [label="Separate\ncentrifuge / column" fillcolor="#dcfce7"]; detect [label="Detect\nUV, antibody, MS" fillcolor="#fce7f3"]; infer [label="Interpret with\nstandards + controls" fillcolor="#ede9fe"]; sample -> prep -> split -> detect -> infer; }''',
        "chart_title": "Beer-Lambert intuition: absorbance rises with concentration",
        "chart_caption": "Illustrative linear standard curve. A calibration line permits concentration estimation only within the validated range.",
        "chart": {"Concentration (ug/mL)": [0, 20, 40, 60, 80, 100], "Absorbance": [0.00, 0.16, 0.32, 0.48, 0.64, 0.80]},
        "chart_y": "Absorbance",
    },
    "PHDLS102": {
        "diagram_title": "Protein structure: sequence becomes function",
        "diagram": '''digraph { rankdir=LR; bgcolor="transparent"; node [shape=box style="rounded,filled" fontname="Arial" margin="0.15,0.10"]; p [label="Primary\namino-acid sequence" fillcolor="#dbeafe"]; s [label="Secondary\nhelix / sheet" fillcolor="#dcfce7"]; t [label="Tertiary\n3D fold" fillcolor="#fef3c7"]; q [label="Quaternary\nsubunit assembly" fillcolor="#fce7f3"]; f [label="Binding, catalysis,\nmotion, signalling" fillcolor="#ede9fe"]; p -> s -> t -> q -> f; }''',
        "chart_title": "A buffer works best near its pKa",
        "chart_caption": "Conceptual titration curve: the flatter middle region is the useful buffering region, where acid and conjugate base coexist in meaningful amounts.",
        "chart": {"Base added (relative units)": [0, 1, 2, 3, 4, 5, 6], "pH": [2.1, 3.0, 3.8, 4.2, 4.6, 6.3, 9.1]},
        "chart_y": "pH",
    },
    "PHDLS103": {
        "diagram_title": "A responsible sequence-to-function workflow",
        "diagram": '''digraph { rankdir=LR; bgcolor="transparent"; node [shape=box style="rounded,filled" fontname="Arial" margin="0.15,0.10"]; seq [label="Query\nsequence" fillcolor="#dbeafe"]; search [label="Database search\nBLAST / domains" fillcolor="#dcfce7"]; align [label="Alignment +\nconserved residues" fillcolor="#fef3c7"]; model [label="Structure /\nphylogeny" fillcolor="#fce7f3"]; test [label="Testable biological\nhypothesis" fillcolor="#ede9fe"]; seq -> search -> align -> model -> test; }''',
        "chart_title": "Alignment coverage changes the strength of an inference",
        "chart_caption": "Illustrative comparison: a striking score over a short segment should not be interpreted like broad, well-supported similarity across a protein.",
        "chart": {"Candidate hit": ["Hit A", "Hit B", "Hit C", "Hit D"], "Query coverage (%)": [92, 74, 41, 18]},
        "chart_y": "Query coverage (%)",
    },
    "PHDLS104": {
        "diagram_title": "Wastewater microbiology as a connected ecosystem",
        "diagram": '''digraph { rankdir=LR; bgcolor="transparent"; node [shape=box style="rounded,filled" fontname="Arial" margin="0.15,0.10"]; waste [label="Organic waste +\nammonia" fillcolor="#dbeafe"]; hetero [label="Heterotrophs\ncarbon removal" fillcolor="#dcfce7"]; nit [label="Nitrifiers\nNH4 -> NO2 -> NO3" fillcolor="#fef3c7"]; anox [label="Anoxic microbes\ndenitrification" fillcolor="#fce7f3"]; water [label="Treated water +\nmanaged sludge" fillcolor="#ede9fe"]; waste -> hetero -> nit -> anox -> water; }''',
        "chart_title": "Microbial growth curve and the meaning of each phase",
        "chart_caption": "Illustrative biomass trajectory. Reactor performance depends on conditions that keep the desired community active rather than merely present.",
        "chart": {"Time": [0, 1, 2, 3, 4, 5, 6, 7], "Relative biomass": [0.10, 0.12, 0.25, 0.58, 0.88, 0.95, 0.91, 0.65]},
        "chart_y": "Relative biomass",
    },
    "PHDLS105": {
        "diagram_title": "How enzyme data becomes a mechanistic claim",
        "diagram": '''digraph { rankdir=LR; bgcolor="transparent"; node [shape=box style="rounded,filled" fontname="Arial" margin="0.15,0.10"]; assay [label="Controlled\nenzyme assay" fillcolor="#dbeafe"]; rates [label="Initial rates at\nseveral [S]" fillcolor="#dcfce7"]; fit [label="Fit kinetic\nmodel" fillcolor="#fef3c7"]; compare [label="Compare +/-\ninhibitor" fillcolor="#fce7f3"]; claim [label="Mechanism with\nlimits stated" fillcolor="#ede9fe"]; assay -> rates -> fit -> compare -> claim; }''',
        "chart_title": "Saturation kinetics: more substrate eventually adds little rate",
        "chart_caption": "Illustrative Michaelis-Menten-shaped curve. The plateau represents approach to Vmax; it is not proof that every enzyme system follows this model.",
        "chart": {"Substrate concentration": [0, 1, 2, 4, 8, 16, 32], "Initial velocity": [0, 0.24, 0.39, 0.56, 0.70, 0.82, 0.90]},
        "chart_y": "Initial velocity",
    },
    "PHDLS106": {
        "diagram_title": "From exposure to health outcome",
        "diagram": '''digraph { rankdir=LR; bgcolor="transparent"; node [shape=box style="rounded,filled" fontname="Arial" margin="0.15,0.10"]; source [label="Source\nchemical / vector" fillcolor="#dbeafe"]; route [label="Route\ninhalation, ingestion, bite" fillcolor="#dcfce7"]; dose [label="Absorbed dose +\nduration" fillcolor="#fef3c7"]; body [label="Metabolism +\ntarget tissue" fillcolor="#fce7f3"]; outcome [label="Response +\nprevention" fillcolor="#ede9fe"]; source -> route -> dose -> body -> outcome; }''',
        "chart_title": "Dose-response: risk interpretation needs exposure information",
        "chart_caption": "Illustrative sigmoid response. It demonstrates a relationship, not a universal safe threshold or a substitute for real exposure assessment.",
        "chart": {"Relative dose": [0, 1, 2, 3, 4, 5, 6], "Response (%)": [0, 3, 10, 31, 62, 86, 96]},
        "chart_y": "Response (%)",
    },
}


RAPID_RECALL_BANK = {
    "PHDLS101": [("What is isopycnic centrifugation?", "A density-gradient method in which particles migrate until they reach the region with the same buoyant density."), ("What does a blank correct in spectrophotometry?", "It subtracts absorbance caused by solvent, cuvette, buffer, and reagents rather than the analyte."), ("Why do larger molecules elute first in gel filtration?", "They enter fewer pores and therefore travel through a shorter effective path in the column."), ("What property drives ion-exchange chromatography?", "Reversible attraction between charged analytes and oppositely charged groups on the stationary phase."), ("What does confocal microscopy reduce?", "Out-of-focus light, enabling optical sectioning and clearer images in thicker specimens."), ("What is an internal loading control?", "A stable reference used to distinguish a true target difference from unequal sample loading or transfer."), ("Why is RNA integrity important before qPCR?", "Degraded RNA can create biased or false expression estimates even when concentration appears adequate."), ("What is a standard curve?", "A relationship between known analyte concentrations and measured signal used to estimate unknowns."), ("What is the key output of mass spectrometry?", "Ions measured by mass-to-charge ratio, often used with fragmentation information for identification."), ("What does ELISA detect?", "Specific antigen or antibody through enzyme-linked recognition and a measurable signal.")],
    "PHDLS102": [("What is a zwitterion?", "A molecule carrying both positive and negative charges while having an overall net charge of zero."), ("Why is glycine unusual?", "Its side chain is hydrogen, making it achiral and unusually flexible in polypeptide structures."), ("What stabilizes an alpha helix?", "Regular hydrogen bonds between backbone carbonyl oxygen and amide hydrogen groups."), ("What is a protein domain?", "A compact structural and often functional unit within a protein that can fold semi-independently."), ("Why can disulfide bonds matter?", "Covalent links between cysteine residues can stabilize extracellular or secreted proteins."), ("What is supercoiling?", "Additional twisting of circular or constrained DNA that alters its topology and biological behavior."), ("What is the main structural role of phospholipids?", "They form bilayers because their hydrophilic heads and hydrophobic tails self-organize in water."), ("Why is cholesterol important in membranes?", "It modulates fluidity, permeability, and membrane-domain behavior depending on temperature and composition."), ("What is a liposome?", "A vesicle made of lipid bilayers used as a model membrane and sometimes for drug delivery."), ("What do glycoproteins contribute to?", "Cell recognition, adhesion, signaling, and protein stability through attached carbohydrate groups.")],
    "PHDLS103": [("What is the difference between global and local alignment?", "Global alignment compares sequences end-to-end; local alignment finds the strongest matching subsections."), ("What does a substitution matrix represent?", "It scores replacement of one residue by another using an evolutionary or similarity model."), ("What is a low E-value evidence for?", "That a match of the observed quality is unlikely to occur by chance in the searched database, given the model."), ("Why use a nonredundant dataset?", "To reduce overrepresentation of near-identical sequences that can bias analysis."), ("What is a conservation score?", "A measure of how consistently a position is preserved across an alignment."), ("What is a contact map?", "A two-dimensional representation of residue pairs that are close in a three-dimensional structure."), ("What does the Protein Data Bank store?", "Experimentally determined and computationally derived three-dimensional macromolecular structure data."), ("What is docking used for?", "To generate hypotheses about how a ligand may fit and interact with a molecular target."), ("What is QSAR?", "Quantitative structure-activity relationship modeling that relates molecular descriptors to measured activity."), ("Why validate a machine-learning model?", "To check that apparent performance generalizes beyond training data and is not just overfitting.")],
    "PHDLS104": [("What is chemolithotrophy?", "Energy generation from oxidation of inorganic compounds, rather than organic carbon alone."), ("What is a microbial guild?", "A group of organisms that perform similar ecological functions, even if they are not closely related."), ("Why are biofilms important environmentally?", "Surface-associated communities can alter nutrient cycling, contaminant transformation, and resistance to stress."), ("What is transformation in microbial genetics?", "Uptake and incorporation of free DNA from the environment."), ("What is transduction?", "Transfer of genetic material between bacteria through a bacteriophage."), ("Why use culture-independent methods?", "Many environmental organisms are difficult to grow in laboratory conditions, so molecular methods reveal more diversity."), ("What is biostimulation?", "Changing site conditions, such as nutrient or electron-acceptor supply, to stimulate existing degraders."), ("What is leachate?", "Contaminated liquid that drains through waste material, particularly in landfill systems."), ("What makes a biosensor selective?", "A recognition element designed to respond preferentially to a target analyte, plus suitable signal processing."), ("What is an exposome?", "The cumulative set of environmental exposures and associated biological responses across a lifetime.")],
    "PHDLS105": [("What is one enzyme unit?", "The amount of enzyme that catalyzes conversion of one micromole of substrate per minute under defined conditions."), ("What is specific activity?", "Enzyme activity per amount of total protein; it is commonly used to track purification."), ("What is a coenzyme?", "A small organic nonprotein molecule that assists enzyme catalysis, often derived from vitamins."), ("What is the induced-fit model?", "A model in which substrate binding promotes a conformational adjustment that improves catalytic alignment."), ("What does Km represent in the Michaelis-Menten model?", "The substrate concentration at which velocity is half Vmax, under the model's assumptions."), ("What happens to ideal competitive inhibition at very high substrate?", "The inhibition can be overcome because substrate outcompetes inhibitor at the active site."), ("What is a suicide inhibitor?", "A mechanism-based inhibitor converted by the enzyme into a reactive species that inactivates it."), ("What is feedback inhibition?", "End-product control of an earlier pathway enzyme to prevent unnecessary overproduction."), ("What is proteolytic activation?", "Activation of an inactive precursor by cleavage, as in many zymogen systems."), ("What is a major immobilization limitation?", "Mass-transfer resistance can slow substrate access or product release around the immobilized enzyme.")],
    "PHDLS106": [("What is a definitive host?", "The host in which a parasite reaches sexual maturity or carries out sexual reproduction."), ("What is an intermediate host?", "A host that supports larval, asexual, or developmental stages of a parasite."), ("What is a reservoir?", "A population or environment in which an infectious agent is normally maintained over time."), ("What is commensalism?", "A relationship in which one organism benefits and the other is neither clearly helped nor harmed."), ("What is the economic value of apiculture?", "It produces honey, wax and other products while supporting pollination services."), ("Why is source reduction central to container-breeding mosquito control?", "Removing breeding water prevents larval development and reduces adult emergence upstream."), ("What is a xenobiotic?", "A chemical foreign to the normal biological system of an organism."), ("What is acute exposure?", "Exposure occurring over a short period, often associated with rapid effects."), ("What does LC50 describe?", "A concentration expected to cause death in 50 percent of a defined test population under stated conditions."), ("What is detoxification?", "Biotransformation or elimination processes that reduce the persistence or harmful reactivity of a toxicant.")],
}


SOLVED_LONG_ANSWERS = {
    "PHDLS101": [
        ("Explain how chromatography separates biomolecules and justify the choice of gel filtration, ion exchange, and affinity chromatography in a protein-purification workflow.", "Chromatography separates components because each component distributes differently between a stationary phase and a moving phase. In protein work, the choice of method follows the property that most clearly distinguishes the target from contaminants. Gel filtration, also called size-exclusion chromatography, separates by hydrodynamic size: larger molecules enter fewer matrix pores and therefore elute earlier. It is useful as a polishing step and for buffer exchange because it can preserve native protein structure. Ion-exchange chromatography separates by net charge. At a chosen pH, a protein binds to an oppositely charged resin and is eluted by changing salt concentration or pH. It provides high capacity and is useful early in purification. Affinity chromatography exploits a specific interaction, such as a His-tag binding immobilized nickel, and can yield a highly enriched target in one step. A defensible workflow may use ion exchange for bulk fractionation, affinity capture for selectivity, and gel filtration to remove aggregates and obtain a monodisperse final preparation. Success is judged using total activity, total protein, specific activity, electrophoretic purity, and controls for loss of function."),
        ("Describe a defensible workflow for quantitative gene-expression analysis using RNA quality control and real-time PCR.", "A quantitative expression study begins with a precise comparison, such as treated versus untreated cells, and biological replicates rather than repeated measurement of one sample. RNA must be isolated under RNase-controlled conditions and assessed for quantity, purity, and integrity; a high concentration alone cannot rescue degraded or contaminated RNA. Equal RNA inputs are reverse transcribed using consistent conditions, then target and reference genes are amplified by real-time PCR with validated primers. Controls should include no-template and no-reverse-transcriptase reactions, and amplification efficiency should be checked when using comparative quantification. The cycle threshold is interpreted relative to a stable reference gene and the experimental design, commonly through delta-delta Ct logic when its assumptions are met. The result supports a relative difference in transcript abundance, not automatically protein abundance or causal mechanism. A strong study therefore reports primer details, normalization method, replicate number, uncertainty, and complementary protein-level validation when the biological claim requires it."),
    ],
    "PHDLS102": [
        ("Discuss the relationship between amino-acid sequence, protein structure, and disease using a molecular explanation.", "Proteins are linear polymers of amino acids joined by peptide bonds, but their biological roles arise when the sequence folds into a specific three-dimensional arrangement. Each side chain contributes chemical possibilities: nonpolar residues tend to form a protected core in soluble proteins, polar and charged residues often participate in hydrogen bonds or salt bridges, and cysteines can form disulfide bonds. These interactions organize secondary structures such as alpha helices and beta sheets, which pack into domains and sometimes multimeric quaternary assemblies. A sequence change can therefore cause disease when it disrupts stability, a catalytic residue, a binding surface, trafficking signal, or regulated conformational switch. For example, replacing a residue in a hydrophobic core with a charged one may expose nonpolar surface, promote misfolding, and reduce function. The effect cannot be predicted solely from the mutation name: its position, structural context, expression level, and cellular environment matter. A complete investigation compares wild-type and variant protein abundance, localization, conformation or stability, molecular activity, and relevant cellular phenotype. This structure-to-function framework explains why molecular defects can lead to system-level disease without treating all variants as equivalent."),
        ("Explain the fluid-mosaic model and show how membrane composition influences biological function and disease relevance.", "The fluid-mosaic model describes membranes as dynamic lipid bilayers containing proteins, carbohydrates, and sterols rather than rigid barriers. Amphipathic phospholipids orient their polar heads toward water and hydrophobic tails inward, creating selective permeability. Membrane proteins act as channels, transporters, receptors, enzymes, and adhesion molecules; carbohydrate-bearing lipids and proteins contribute recognition and signaling. Fluidity depends on temperature, fatty-acid chain length, degree of unsaturation, and cholesterol. Unsaturated chains create packing disorder and generally increase fluidity, while cholesterol buffers extremes by limiting excessive movement at high temperature and preventing overly tight packing at low temperature. This physical environment influences receptor clustering, vesicle formation, ion transport, and cell communication. Altered lipid composition can affect signaling and metabolic disease, while liposomes exploit bilayer architecture to package and deliver drugs. Thus, a membrane answer should connect composition to material properties, then to a protein- or cell-level function, and finally to an applied or disease example rather than describing lipids as a static list."),
    ],
    "PHDLS103": [
        ("Explain BLAST interpretation using score, E-value, alignment coverage, and biological validation.", "BLAST is a sequence-similarity search method used to identify database sequences that share local similarity with a query. The output is not a direct declaration of gene function. A bit score summarizes alignment quality under a scoring scheme, while the E-value estimates how many matches of similar quality might be expected by chance in a database of that size. A low E-value strengthens the evidence for non-random similarity, but it must be interpreted alongside query coverage, percent identity, alignment length, gaps, database quality, and the biological context of both sequences. A high-quality local match over a small domain may show that the query contains that domain, not that the entire query has the same function as the database record. A responsible workflow inspects the alignment, checks conserved catalytic or binding residues, searches domain resources, compares multiple homologues, and examines organismal or genomic context. The resulting statement should be appropriately qualified, such as 'candidate member of a protein family' rather than a definitive function assignment. Experimental evidence - activity assay, binding study, knockout phenotype, or localization - is needed to test the computational hypothesis."),
        ("Describe how a phylogenetic tree should be constructed and interpreted from protein sequences.", "Phylogenetic analysis begins by defining an evolutionary question and assembling a curated set of homologous protein sequences. Sequences should be checked for quality, domain architecture, and inappropriate fragments before alignment. A multiple sequence alignment is critical because every subsequent inference assumes that aligned positions share common ancestry. Ambiguous or poorly aligned regions may need trimming rather than forced interpretation. A tree-building method and evolutionary model are then selected to fit the data, and branch support is assessed using an appropriate resampling or statistical approach. The final tree is a model-based hypothesis of evolutionary relationship, not a literal historical photograph. A clade may be well supported while its deeper placement remains uncertain. Interpretation should consider gene duplication, gene loss, horizontal transfer, uneven taxonomic sampling, and the possibility that a gene tree differs from a species tree. When discussing function, combine tree position with domain composition, conserved residues, expression, and experiment. This prevents the common error of treating visual proximity on a tree as proof of identical molecular function."),
    ],
    "PHDLS104": [
        ("Explain wastewater treatment as a microbial process, including the role of environmental controls and monitoring.", "Biological wastewater treatment uses microbial metabolism to transform organic matter and nutrients into less problematic forms. Heterotrophic organisms consume biodegradable organic carbon, often reducing oxygen demand; nitrifying organisms oxidize ammonia through nitrite toward nitrate under suitable aerobic conditions; and denitrifying organisms can reduce nitrate under anoxic conditions when an electron donor is available. These functions are performed by communities, not an isolated species, so treatment performance depends on the reactor environment. Dissolved oxygen, pH, temperature, alkalinity, nutrient ratio, toxic influent shocks, mixing, hydraulic retention, and sludge age determine which populations survive and how quickly they act. Monitoring should therefore track both process conditions and outcomes: influent and effluent organic load, ammonia, nitrite, nitrate, dissolved oxygen, biomass, settling properties, and relevant microbial indicators. If ammonia rises, a good diagnosis verifies the measurement and investigates oxygen transfer, loading, inhibition, and community retention before recommending changes. This approach treats a treatment plant as a managed ecosystem and ties microbial theory to observable water-quality evidence."),
        ("Discuss bioremediation and explain why site characterization is essential before choosing bioaugmentation or biostimulation.", "Bioremediation uses biological activity to reduce contaminant concentration, mobility, or toxicity. It is not simply the addition of microbes. Whether degradation occurs depends on contaminant accessibility, the presence of competent organisms, electron donors and acceptors, nutrient balance, pH, temperature, moisture, competing reactions, and toxicity to the community. Site characterization establishes the contaminant type and distribution, hydrogeology, geochemistry, oxygen status, indigenous microbial capacity, and potential transformation products. Biostimulation modifies conditions - for example by adding nutrients or an electron acceptor - to encourage organisms already present. Bioaugmentation introduces selected organisms when a required function is absent or insufficient, but introduced organisms may fail to compete or survive if the underlying environment remains unsuitable. A rigorous design includes baseline sampling, a conceptual site model, measurable treatment endpoints, and monitoring for parent contaminant decline as well as harmful intermediates. The conclusion should compare expected benefit, time scale, uncertainty, and the need for physical or chemical controls alongside microbial treatment."),
    ],
    "PHDLS105": [
        ("Explain Michaelis-Menten kinetics and show how enzyme inhibition supports mechanistic reasoning.", "Michaelis-Menten kinetics describes the initial rate of many enzyme-catalyzed reactions as substrate concentration increases toward saturation. The model is based on the formation and breakdown of an enzyme-substrate complex under defined assumptions, including initial-rate measurement and an approximately steady concentration of that complex. Vmax is the limiting rate approached when active sites are saturated, while Km is the substrate concentration at half Vmax within the model; it is often informative about apparent substrate behavior but is not a universal measure of affinity. Inhibition studies add mechanistic evidence. A competitive inhibitor binds at or near the substrate site and, in the ideal case, increases apparent Km without changing Vmax because excess substrate can compete it away. Pure noncompetitive inhibition lowers Vmax without changing apparent Km, consistent with loss of catalytic capacity through a distinct site. Uncompetitive inhibition binds the enzyme-substrate complex and lowers both apparent parameters. Real data may show mixed behavior, so claims should be supported by replicated initial-rate measurements, suitable fitting, residual checks, and additional binding or time-dependence experiments. A graph is evidence for a model, not a substitute for controls."),
        ("Discuss enzyme immobilization, including methods, advantages, limitations, and industrial relevance.", "Enzyme immobilization confines a catalyst to a support or defined phase while allowing substrate conversion. Common approaches include adsorption to a carrier, covalent attachment, entrapment in a gel, encapsulation, and cross-linking. The main industrial advantage is operational control: the enzyme can be recovered, reused, separated from product more easily, and sometimes used in continuous reactors. Immobilization can also improve stability under selected temperature, pH, or solvent conditions. However, the support can restrict conformational motion, block the active site, or create diffusion barriers so that substrate reaches the catalyst slowly and product leaves slowly. Each method therefore needs optimization of loading, particle size, flow, substrate concentration, and retained activity. Applications include food processing, dairy and beverage manufacture, biosensors, pharmaceutical synthesis, and detergent enzymes. A strong evaluation compares free and immobilized enzyme using activity, stability, operational lifetime, product quality, and cost per useful conversion. The best support is not the one with the most enzyme attached; it is the one that delivers reliable conversion under the real process conditions."),
    ],
    "PHDLS106": [
        ("Explain dose-response relationships and evaluate the limits of LD50, LC50, TD50, and therapeutic index.", "A dose-response relationship links increasing exposure to a measured biological effect. In a graded response, the magnitude of response changes in an individual system; in a quantal response, the outcome is recorded as the proportion of a population that reaches a defined endpoint. LD50 and LC50 are dose or concentration estimates associated with death in 50 percent of a defined test population under stated conditions. TD50 refers to a toxic effect in 50 percent of a population, while therapeutic index compares toxic and effective doses to give a conceptual safety margin. These values are useful for comparing hazard under controlled conditions, but they do not provide a complete risk assessment. Their meaning depends on species, route, duration, formulation, endpoint, age, health status, and the statistical model. They may not capture chronic toxicity, developmental effects, mixtures, susceptible groups, or real occupational and environmental exposure. A correct conclusion therefore separates hazard from risk: the practical risk depends on whether people or ecosystems actually encounter a dose through a plausible route for sufficient duration. Good toxicology uses dose-response data together with exposure assessment and mechanistic evidence."),
        ("Discuss an integrated approach to vector control using vector biology and public-health reasoning.", "Integrated vector control begins with surveillance: identify the vector, map breeding and resting sites, understand feeding behavior, and determine the disease or nuisance burden. Control measures should interrupt the most vulnerable point in that organism's life cycle. For a container-breeding mosquito, source reduction is central because removing or managing water-holding containers prevents larval development before adults emerge. Targeted larval control, personal protection, housing improvements, community education, and outbreak-responsive adult control may complement this foundation. The programme should not assume that one insecticide solves the problem. Repeated chemical use can select resistance and create environmental costs, while poor community participation allows habitats to reappear. Monitoring of breeding indices, adult density, resistance markers, and disease indicators shows whether the intervention is working. The same biological reasoning distinguishes Anopheles, Aedes, Culex, lice, and fleas: ecology changes the control strategy. A good answer connects organism biology, transmission chain, intervention, measurement, and limitation rather than listing generic prevention measures."),
    ],
}


def render_bullets(items: list[str]) -> None:
    for item in items:
        st.markdown(f"- {item}")


def render_question_paper(question_paper: dict) -> None:
    for section, qa_items in question_paper.items():
        st.markdown(f"### {section}")
        for idx, item in enumerate(qa_items, 1):
            with st.expander(f"Q{idx}. {item['q']}", expanded=False):
                st.markdown("**Model answer**")
                st.write(item["a"])


def render_viva_drill(items: list[tuple[str, str]]) -> None:
    st.markdown("### Viva drill: answer in 30 seconds")
    for idx, (question, answer) in enumerate(items, 1):
        with st.expander(f"V{idx}. {question}", expanded=False):
            st.markdown(f"**Strong answer:** {answer}")


def render_visual_lab(course_code: str) -> None:
    lab = VISUAL_LABS[course_code]
    st.markdown("### Visual learning lab")
    st.caption("Diagrams and charts are conceptual teaching models. Read the labels, then explain the relationship in your own words.")
    left, right = st.columns(2)
    with left:
        st.markdown(f"#### {lab['diagram_title']}")
        st.graphviz_chart(lab["diagram"], use_container_width=True)
    with right:
        st.markdown(f"#### {lab['chart_title']}")
        chart_x = next(iter(lab["chart"]))
        chart_data = pd.DataFrame(lab["chart"]).set_index(chart_x)
        st.line_chart(chart_data, y=lab["chart_y"], use_container_width=True)
    st.info(lab["chart_caption"])


def render_rapid_recall(course_code: str) -> None:
    st.markdown("### 10-question rapid recall bank")
    st.caption("Use this as a closed-book drill. Reveal an answer only after you have attempted it aloud or in writing.")
    questions = RAPID_RECALL_BANK[course_code]
    col1, col2 = st.columns(2)
    for index, (question, answer) in enumerate(questions):
        with (col1 if index % 2 == 0 else col2):
            with st.expander(f"Recall {index + 1}. {question}", expanded=False):
                st.markdown(f"**Answer:** {answer}")


def render_unit_cards(units: list[dict], course_code: str) -> None:
    for unit in units:
        with st.expander(unit["title"], expanded=False):
            st.markdown(f"**Why this unit matters:** {unit['summary']}")
            st.markdown("**Deep notes**")
            render_bullets(unit["deep_dive"])
            st.markdown(f"**Example text:** {unit['example']}")
            st.markdown(
                f"**Masterclass lens:** {MASTERCLASS_LAYERS[course_code]['thesis']}"
            )
            st.markdown("**Exam focus**")
            render_bullets(unit["exam_focus"])


def render_course(course: dict) -> None:
    masterclass = MASTERCLASS_LAYERS[course["code"]]
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #ecfeff 0%, #f8fafc 100%); padding: 14px; border-radius: 12px; border: 1px solid #bae6fd; margin-bottom: 14px;">
            <h3 style="margin: 0 !important; color: #0f172a;">{course["code"]}: {course["title"]}</h3>
            <p style="margin: 6px 0 0 0 !important; color: #475569;">{course["hours"]} | Credits: {course["credits"]}</p>
            <p style="margin: 8px 0 0 0 !important; color: #155e75;"><strong>Course focus:</strong> {course["focus"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    visual_tab, overview_tab, roadmap_tab, notes_tab, examples_tab, paper_tab = st.tabs(
        [
            "Visual Lab",
            "Overview",
            "Study Guide",
            "Deep Notes",
            "Research Cases",
            "Exam Bank",
        ]
    )

    with overview_tab:
        col1, col2 = st.columns([1.25, 1])
        with col1:
            st.markdown("### Why this course matters")
            render_bullets(course["why_it_matters"])
            st.markdown("### Learning outcomes")
            render_bullets(course["outcomes"])
        with col2:
            st.markdown("### Quick academic view")
            st.table(
                {
                    "Field": ["Course code", "Credits", "Teaching load", "Assessment", "Mode"],
                    "Details": [
                        course["code"],
                        str(course["credits"]),
                        course["hours"],
                        "IA 20 | MTE 30 | ETE 50 | Total 100",
                        "Theory",
                    ],
                }
            )
            st.markdown("### Research-enrichment sources")
            for source, url in masterclass["sources"]:
                st.markdown(f"- [{source}]({url})")

    with roadmap_tab:
        st.markdown("### The big idea")
        st.info(masterclass["thesis"])
        st.markdown("### Analogy that makes the course memorable")
        st.markdown(
            f"""
            <div style="background: linear-gradient(135deg, #fff7ed 0%, #fffbeb 100%); padding: 16px; border-radius: 12px; border-left: 5px solid #f97316; color: #431407;">
                {masterclass["analogy"]}
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("### Research reasoning chain")
        for step, item in enumerate(masterclass["reasoning"], 1):
            st.markdown(f"**{step}.** {item}")
        st.markdown("### How to build a high-scoring long answer")
        for step, item in enumerate(masterclass["blueprint"], 1):
            st.markdown(f"{step}. {item}")
        render_viva_drill(masterclass["viva"])

    with visual_tab:
        render_visual_lab(course["code"])

    with notes_tab:
        st.markdown("### Detailed unit-wise content")
        st.caption("Open one unit at a time. Each combines syllabus content with interpretation and an exam-useful example.")
        render_unit_cards(course["unit_notes"], course["code"])

    with examples_tab:
        st.markdown("### Applications")
        render_bullets(course["applications"])
        st.markdown("### Research case: think like an investigator")
        st.markdown(
            f"""
            <div style="background: #f0fdf4; padding: 16px; border-radius: 12px; border: 1px solid #86efac; margin-bottom: 12px;">
                <div style="font-weight: 700; color: #166534; margin-bottom: 7px;">{masterclass["case"]["title"]}</div>
                <div style="color: #14532d;"><strong>Challenge:</strong> {masterclass["case"]["prompt"]}</div>
                <div style="color: #14532d; margin-top: 9px;"><strong>Model reasoning:</strong> {masterclass["case"]["answer"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("### Additional worked examples")
        for item in course["worked_examples"]:
            st.markdown(
                f"""
                <div style="background: #ffffff; padding: 12px; border-radius: 10px; border: 1px solid #dbeafe; margin-bottom: 10px;">
                    <div style="font-weight: 700; color: #1e3a8a; margin-bottom: 4px;">{item["title"]}</div>
                    <div style="color: #475569;">{item["body"]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with paper_tab:
        st.markdown("### Sample question paper with model answers")
        st.caption("Suggested practice pattern: Section A 5 x 2 marks, Section B 3 x 5 marks, Section C 2 x 10 marks. Write first, then compare your answer with the model reasoning.")
        render_question_paper(course["question_paper"])
        st.markdown("### Fully solved 10-mark answers")
        st.caption("These are complete answer models. Notice how each one defines the concept, explains the mechanism, applies it, and states a limitation or control.")
        for idx, (question, answer) in enumerate(SOLVED_LONG_ANSWERS[course["code"]], 1):
            with st.expander(f"Solved 10-mark answer {idx}. {question}", expanded=False):
                st.markdown("**Model answer**")
                st.write(answer)
        st.markdown("### Advanced doctoral question bank")
        st.caption("These questions test interpretation, method choice, uncertainty, and argument quality rather than recall alone.")
        for idx, (question, answer) in enumerate(ADVANCED_QUESTION_BANK[course["code"]], 1):
            with st.expander(f"Advanced Q{idx}. {question}", expanded=False):
                st.markdown("**Model answer**")
                st.write(answer)
        render_rapid_recall(course["code"])


inject_seo_meta(
    title="Life Sciences Domain Specific Masterclass | Ph.D. Coursework Companion",
    description="Deep research-backed study portal for Life Sciences Ph.D. domain-specific courses with detailed notes, examples, and sample question papers with answers.",
    keywords=[
        "phd life sciences syllabus",
        "bioanalytical techniques notes",
        "biomolecules structure function notes",
        "bioinformatics algorithms applications notes",
        "environmental microbiology phd notes",
        "advanced enzymology question paper",
        "applied zoology toxicology answers",
    ],
    schema_type="Course",
    canonical_url="https://phd-research-hub.dev/life-sciences-domain-specific",
    reading_time=90,
    breadcrumbs=[
        {"name": "Home", "url": "https://phd-research-hub.dev"},
        {"name": "Life Sciences Domain Specific", "url": "https://phd-research-hub.dev/life-sciences-domain-specific"},
    ],
    course_info={
        "name": "Life Sciences Domain Specific Masterclass",
        "description": "A detailed study portal for School of Biological and Life Sciences Ph.D. domain-specific courses.",
        "level": "Doctoral",
        "prerequisites": "Postgraduate degree in a relevant Life Science discipline with minimum 50 percent or equivalent CGPA.",
        "teaches": [course["title"] for course in COURSES],
        "workload": "PT150H",
        "rating": "4.9",
        "rating_count": 242,
    },
)

apply_custom_css()
show_top_nav(current_page="Life Sciences Domain Specific")

st.markdown(
    """
<div style="text-align: center; padding: 16px; background: linear-gradient(135deg, #ecfeff 0%, #eef2ff 100%); border-radius: 12px; margin-bottom: 12px; border: 1px solid #bfdbfe;">
    <h2 style="margin: 0 !important; font-size: 1.45rem !important;">Life Sciences Domain Specific Masterclass</h2>
    <p style="margin: 6px 0 0 0 !important; font-size: 14px; color: #334155;">
        School of Biological and Life Sciences | Detailed notes, examples, and answer-backed practice
    </p>
</div>
""",
    unsafe_allow_html=True,
)

st.info(
    "Source handling: the attached PDF defines the syllabus scope. It was treated as source material, not as task instructions. "
    "This page expands those topics into study-ready content using web research and current workspace patterns."
)

metric1, metric2, metric3, metric4 = st.columns(4)
with metric1:
    st.metric("Courses Covered", len(COURSES))
with metric2:
    st.metric("Total Credits", sum(course["credits"] for course in COURSES))
with metric3:
    st.metric("Answer-Backed Questions", sum(len(section) for course in COURSES for section in course["question_paper"].values()) + sum(len(items) for items in ADVANCED_QUESTION_BANK.values()) + sum(len(items) for items in RAPID_RECALL_BANK.values()) + sum(len(items) for items in SOLVED_LONG_ANSWERS.values()))
with metric4:
    st.metric("Teaching Visuals", f"{len(VISUAL_LABS) * 2}+")

st.markdown("### Choose your subject")
st.caption("PHDLS101 Bioanalytical Techniques | PHDLS102 Biomolecules | PHDLS103 Bioinformatics | PHDLS104 Environmental Microbiology | PHDLS105 Enzymology | PHDLS106 Zoology and Toxicology")
course_tabs = st.tabs([course["code"] for course in COURSES])
for course_tab, course in zip(course_tabs, COURSES):
    with course_tab:
        render_course(course)

st.markdown("---")
st.markdown("### Study it like a scientist")
st.markdown(
    "Each course follows the same learning arc: **concept -> visual model -> research reasoning -> worked case -> exam answer -> rapid recall**. "
    "Use the Visual Lab before memorizing notes; it shows what changes, flows, separates, binds, grows, or responds."
)

with st.expander("Research and content map", expanded=True):
    st.markdown("### Master sources used for deep enrichment")
    render_bullets(MASTER_SOURCES)
    st.markdown("### Best way to study from this page")
    render_bullets(
        [
            "Read the Overview tab first to understand the logic of the course.",
            "Use Visual Lab to see the core process or quantitative relationship before reading detail.",
            "Use Deep Notes and Cases and Analogies to build long-answer content and concept clarity.",
            "Use Question Papers and Answers for full answers, advanced reasoning, and 10-question rapid recall drills.",
        ]
    )

catalog_data = {
    "Course Code": [course["code"] for course in COURSES],
    "Title": [course["title"] for course in COURSES],
    "Credits": [course["credits"] for course in COURSES],
    "Best Revision Lens": [
        "Technique comparison and workflow design",
        "Structure to function to disease",
        "Algorithm to inference to application",
        "Microbe to environment to outcome",
        "Kinetics to regulation to industry",
        "Exposure to response to mechanism",
    ],
}

with st.expander("Comparative course map", expanded=False):
    st.table(catalog_data)

show_footer()
