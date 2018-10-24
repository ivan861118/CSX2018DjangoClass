document.getElementById('fileinput').addEventListener('change', function(){
    var fileList = this.files;
    var length = fileList.length; 

    var dataPath = "../data/";
    var dataFile = "exp3,4.csv";
    var dataURL = dataPath + dataFile;

    d3.csv(fileList[2],function(data) {
        console.log(data);
    });

    }, false);
    