#Lisa Wu - ACM Coding Challenge Question 1


from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO
record = SeqIO.read("Genome.gb", "genbank")


gd_diagram = GenomeDiagram.Diagram("Tomato Curly Stunt Virus")
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()


for feature in record.features:
    if feature.type != "gene":
        #Exclude this feature
        continue
    if len(gd_feature_set) % 2 == 0:
        color = colors.blue
    else:
        color = colors.lightblue
    gd_feature_set.add_feature(feature, color=color, label=True, label_size = 15, label_color= color)
    


gd_diagram.draw(format="circular", circular=True, pagesize=(25*cm,25*cm),
                start=0, end=len(record), circle_core=0.7)
gd_diagram.write("TCSV.png", "PNG")