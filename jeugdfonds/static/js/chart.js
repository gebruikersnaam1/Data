
function SetChartValues(applicantsList) {
    var arr = [];
    for(i=0; i <=applicantsList.length-1; i++){
       r = { y: applicantsList[i]['applicants'],  label: applicantsList[i]['deelgemeente'] }
       arr.push(r)
    }
    window.dps = arr
    LoadCanvas(arr,"Areas of Rotterdam","Amount Applicants")
}

function LoadCanvas(content,txtTitle,yTile){
    var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        theme: "light1", // "light1", "light2", "dark1", "dark2"
        title:{
            text: txtTitle
        },
        axisY: {
            title: yTile
        },
        data: [{        
            type: "column",  
            showInLegend: true, 
            legendMarkerColor: "grey",
            legendText: " ",
            dataPoints: content
        }]
    });
    chart.render();
}

