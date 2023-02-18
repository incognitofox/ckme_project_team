from django.shortcuts import render        
from django.http import HttpResponse
from django.http import HttpResponseRedirect
        
def index(request):    
    return render(request, "index.html")

def validate(request):
    if request.method == "POST":
        f = request.FILES['csv'] # gets the csv file from submit
        f.save(os.path.join(app.config['UPLOAD_FOLDER'] ,secure_filename(f.filename)))
        fname = f.filename.split(".")[0]
        print(fname)
        go(fname)
        return send_file(f"{fname}-cleaned.csv")
    return HttpResponse("this page does not exist")
