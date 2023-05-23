# flake8: noqa
import os
import urllib.request

url_template = "https://infoscience.epfl.ch/search?ln=fr&cc=Infoscience%2FResearch%2FENAC%2FIIE&p=&f=&jrec={start}&rm=&sf=&so=d&rg={stride}&c=Infoscience%2FResearch%2FENAC%2FIIE%2FAPRL&c=Infoscience%2FResearch%2FENAC%2FIIE%2FCHANGE&c=Infoscience%2FResearch%2FENAC%2FIIE%2FCRYOS&c=Infoscience%2FResearch%2FENAC%2FIIE%2FDISAL&c=Infoscience%2FResearch%2FENAC%2FIIE%2FECEO&c=Infoscience%2FResearch%2FENAC%2FIIE%2FECHO&c=Infoscience%2FResearch%2FENAC%2FIIE%2FECOL&c=Infoscience%2FResearch%2FENAC%2FIIE%2FECOTOX&c=Infoscience%2FResearch%2FENAC%2FIIE%2FEERL&c=Infoscience%2FResearch%2FENAC%2FIIE%2FEML&c=Infoscience%2FResearch%2FENAC%2FIIE%2FEPFL-PSI&c=Infoscience%2FResearch%2FENAC%2FIIE%2FGR-CEL&c=Infoscience%2FResearch%2FENAC%2FIIE%2FHERUS&c=Infoscience%2FResearch%2FENAC%2FIIE%2FLAPI&c=Infoscience%2FResearch%2FENAC%2FIIE%2FLASIG&c=Infoscience%2FResearch%2FENAC%2FIIE%2FLBE&c=Infoscience%2FResearch%2FENAC%2FIIE%2FLCE&c=Infoscience%2FResearch%2FENAC%2FIIE%2FLGB&c=Infoscience%2FResearch%2FENAC%2FIIE%2FLTE&c=Infoscience%2FResearch%2FENAC%2FIIE%2FLTQE&c=Infoscience%2FResearch%2FENAC%2FIIE%2FMACE&c=Infoscience%2FResearch%2FENAC%2FIIE%2FMICROBE&c=Infoscience%2FResearch%2FENAC%2FIIE%2FPERL&c=Infoscience%2FResearch%2FENAC%2FIIE%2FRIVER&c=Infoscience%2FResearch%2FENAC%2FIIE%2FSENSE&c=Infoscience%2FResearch%2FENAC%2FIIE%2FSLAB&c=Infoscience%2FResearch%2FENAC%2FIIE%2FSOIL&c=Infoscience%2FResearch%2FENAC%2FIIE%2FSSIE&c=Infoscience%2FResearch%2FENAC%2FIIE%2FTOPO&c=Infoscience%2FResearch%2FENAC%2FIIE%2FTOX&c=Infoscience%2FResearch%2FENAC%2FIIE%2FUNATTRIBUTED-IIE&c=Infoscience%2FResearch%2FENAC%2FIIE%2FUPHCE&c=Infoscience%2FResearch%2FENAC%2FIIE%2FWIRE&c=Infoscience%2FResearch%2FENAC%2FIIE%2FWR-LAB&c=&of=xm"

filename_template = "infoscience_{start}_{end}.xml"
stride = 1000
n = 8500
output_dir = "../data/scrapped/infoscience"
os.makedirs(output_dir, exist_ok=True)

for start in range(1, n, stride):
    end = start + stride - 1
    url = url_template.format(start=start, stride=stride)
    filename = filename_template.format(start=start, end=end)
    print("Downloading", filename)
    urllib.request.urlretrieve(url, os.path.join(output_dir, filename))
