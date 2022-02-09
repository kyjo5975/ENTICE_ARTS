import xml.etree.ElementTree as et
import pandas as pd

xtree = et.parse("ICI_test.ybatch.xml")
xroot = xtree.getroot()
rows = []
df_cols = "11"

for node in xroot:
    res = []
    res.append(node.attrib.get(df_cols[0]))
    for el in df_cols[1:]:
        if node is not None and node.find(el) is not None:
            res.append(node.find(el).text)
        else:
            res.append(None)
    rows.append({df_cols[i]: res[i] for i, _ in enumerate(df_cols)})

out_df = pd.DataFrame(rows, columns=df_cols)

print(out_df)

ICI = pd.read_xml('ICI_test.ybatch.xml')