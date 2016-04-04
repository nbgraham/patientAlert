$(document).ready(function(){
	$.ajax({
		url: 'http://localhost:8000/patient/doctors/?format=jsonp',
		dataType: 'jsonp',
		success: function(dataWeGotViaJsonp){
			for (i = 0, len = dataWeGotViaJsonp.length; i < len; ++i)
			{
				id = dataWeGotViaJsonp[i].doctorid;
				url = 'http://localhost:8000/patient/appointments/?doctorid=' + id + "&format=jsonp";
				console.log(url);
				$.ajax({
					url: url,
					dataType: 'jsonp',
					success: function(appointments){
					    if (appointments.length > 0) {
					        $("#charts").append("<h1>Doctor" + appointments[0].doctorid + "</h1>")
					            .append("Push Back")
					            .append("<button onClick=\"test()\">Test</button>")
					            .append("<button onClick=\"pushBack(" + appointments + "," + 15 + ")\">15 minutes</button>")
					            .append("<button onClick=\"pushBack(" + appointments + "," + 30 + ")\">30 minutes</button>")
					            .append("<table id=doctor" + appointments[0].doctorid + "><tr><th>Time</th><th>Patient</th></table>");

					    }
						for (i = 0, len = appointments.length; i < len; ++i)
						{
						    $("#doctor"+appointments[i].doctorid).append("<tr><td>"+new Date(appointments[i].time).toString()+"</td><td>"+appointments[i].patientid+"</td></tr>");
							console.log(appointments[i]);
						}
					}
				});
			}
		}
	});
})

function test() {
    $.ajax({
            url: 'http://localhost:8000/patient/appointments/'+1
                + "?" + $.param({"id":1,"time":"2015-11-14T19:35:00Z","doctorid":1, "patientid":1}),
            type: 'PUT',
            success: console.log("Success"),
            error: console.log("Error")
        });
}

function pushBack(appointments, minutes) {
    for(i = 0; i < appointments.length; i++){
        $.ajax({
            url: 'http://localhost:8000/patient/appointments/'+appointments[i].id
                + "?" + $.param({"id":appointments[i].id,"time":addMinutes(appointments[i].time,minutes),"doctorid":appointments[i].doctorid, "patientid":appointments[i].patientid}),
            type: 'PUT',
            success: console.log("Success"),
            error: console.log("Error")
        });
    }
}

function addMinutes(stringDate, minutes)
{
    oldDateObj = new Date(stringDate);
    return new Date(oldDateObj.getTime() + minutes*60000).toString();
}