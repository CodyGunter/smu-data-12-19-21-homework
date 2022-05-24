$(document).ready(function() {
    console.log("Page Loaded");
    doWork();

    
    $("#selDataset").on("change", function() {
        makeDashboard()
    });

});

var global_data;
var url = "static/data/samples.json";

function doWork() {
    
    requestAjax(url);
}

function makeDashboard() {
    let id = $("#selDataset").val();

    createMetadata(id);
    createHorizontal(id);
    createBubbleChart(id);
    createGauge(id);
}

function requestAjax(url) {
    $.ajax({
        type: "GET",
        url: url,
        contentType: "application/json; charset=utf-8",
        success: function(data) {
            console.log(data);
            global_data = data;
            createDropdown();
            makeDashboard();
        },
        error: function(textStatus, errorThrown) {
            console.log("FAILED to get data");
            console.log(textStatus);
            console.log(errorThrown);
        }
    });
}



function createDropdown() {
    var names = global_data.names;
    for (let i = 0; i < names.length; i++) {
        let name = names[i];
        let html = `<option>${name}</option>`;
        $("#selDataset").append(html);
    }
}


function createMetadata(id) {
    $("#sample-metadata").empty();
    let info = global_data.metadata.filter(x => x.id == id)[0];
    console.log(info);
    Object.entries(info).map(function(x) {
        let html = `<h6>${x[0]}: ${x[1]}</h6>`;
        $("#sample-metadata").append(html);
    });
}

// var label = sample.otu_labels.slice(0, 10).reverse()

function createHorizontal(id) {
    let sample = global_data.samples.filter(x => x.id == id)[0];

    let sample_data = sample.sample_values.slice(0, 10).reverse()
    let sample_id = sample.otu_ids.slice(0, 10).reverse()
    sample_id = sample_id.map(x => `OTU ${x}`)


    var trace1 = {
        type: 'bar',
        x: sample_data,
        y: sample_id,
        text: sample.otu_labels.slice(0, 10).reverse(),
        orientation: 'h'
    }

    var data1 = [trace1];
    // https://plotly.com/javascript/axes/
    var layout = {
        "title": "Bacteria Count vs Bacteria ID",
        xaxis: {
            title: "Bacteria Count"
        },
        yaxis: {
            title: "Bacteria ID"
        }
    }

    Plotly.newPlot('bar', data1, layout);

}

function createBubbleChart(id) {
    let sample = global_data.samples.filter(x => x.id == id)[0];

    var trace1 = {
        x: sample.otu_ids,
        y: sample.sample_values,
        text: sample.otu_labels.slice(0, 10).reverse(),
        mode: 'markers',
        marker: {
            size: sample.sample_values,
            color: sample.otu_ids,
            colorscale: "Portland"
        }
    }

    var data1 = [trace1];
    var layout = {
        "title": "Bacteria ID vs Bacteria Count",
        xaxis: {
            title: "OTU ID"
        },
        yaxis: {
            title: "Bacteria Count"
        },
    }

    Plotly.newPlot('bubble', data1, layout);
}

function createGauge(id) {
    let info = global_data.metadata.filter(x => x.id == id)[0];
    let avg = global_data["metadata"].map(x => x.wfreq).reduce((a, b) => a + b, 0) / global_data.metadata.length;

    var trace = {
        domain: { x: [0, 1], y: [0, 1] },
        value: info["wfreq"],
        title: { text: "Wash Frequency" },
        type: "indicator",
        mode: "gauge+number",
        delta: { reference: avg.toFixed(2) },
        gauge: {
            axis: { range: [null, 10] },
            steps: [
                { range: [0, 5], color: "lightgray" },
                { range: [5, 7], color: "gray" }
            ],
            threshold: {
                line: { color: "red", width: 4 },
                thickness: 0.75,
                value: 9.5
            }
        }
    };

    var data1 = [trace];

    var layout = {
        title: "Belly Button Wash Frequency"
    };
    Plotly.newPlot('gauge', data1, layout);
}