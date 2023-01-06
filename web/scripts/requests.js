async function get_records(user_id){
    const response = await fetch(`http://localhost:8000/api/diary/records/1`);
    return await response.json();
}

async function get_mapping(url){
    let response = await fetch(url);
    let emotions = await response.json();
    return Object.fromEntries(emotions.map(e => [e.id, e.name]));
}

async function fill_record_table(user_id){
    let records = await get_records(user_id);
    let emotion_dict = await get_mapping(`http://localhost:8000/api/diary/emotions`);
    let distortion_dict = await get_mapping('http://localhost:8000/api/diary/distortions');
    for (const record of records) {
        let emotion_record_resp = await fetch('http://localhost:8000/api/diary/emotion_record?' +
            new URLSearchParams({record_id: record.id}));
        let emotion_record = await emotion_record_resp.json();
        var emotions_str = "";
        for (const emotion of emotion_record){
            emotions_str += emotion_dict[emotion.emotion_id] + "\n";
        }

        let distortion_record_resp = await fetch('http://localhost:8000/api/diary/distortion_record?' +
            new URLSearchParams({record_id: record.id}));
        let distortion_record = await distortion_record_resp.json();
        var distortion_str = "";
        for (const distortion of distortion_record){
            distortion_str += distortion_dict[distortion.distortion_id] + "\n";
        }
        $(`<tr onclick="window.location='http://localhost:8000/app/diary/record/${record.id}';">\n` +
            `<td style="display: none">${record.id}</td>\n` +
            `<td>${record.trigger_event}</td>\n` +
            `<td>${record.automated_thought}</td>\n` +
            `<td>${emotions_str}</td>\n` +
            `<td>${distortion_str}</td>\n` +
            `<td>${record.date_time}</td>\n` +
            `</tr>`).appendTo('#record_table');
    }
}

async function fill_emotion_selector(){
    const response = await fetch(`http://localhost:8000/api/diary/emotions`);
    let emotions = await response.json();
    for (const emotion of emotions) {
        $(`<option value=${emotion.id}>${emotion.name}</option>\n`).appendTo('#select_emotion');
    }
    for (const emotion of emotions) {
        $(`<option value=${emotion.id}>${emotion.name}</option>\n`).appendTo('#emotion_selector');
    }
    for (const emotion of emotions) {
        $(`<option value=${emotion.id}>${emotion.name}</option>\n`).appendTo('#emotion_id');
    }
}

async function fill_distortion_selector(){
    const response = await fetch(`http://localhost:8000/api/diary/distortions`);
    let distortions = await response.json();
    for (const distortion of distortions) {
        $(`<option value=${distortion.id}>${distortion.name}</option>\n`).appendTo('#distortion_selector');
    }
    for (const distortion of distortions) {
        $(`<option value=${distortion.id}>${distortion.name}</option>\n`).appendTo('#distortion_id');
    }
}

function on_load(user_id){
    document.addEventListener("DOMContentLoaded", fill_record_table.bind(user_id))
    document.addEventListener("DOMContentLoaded", fill_emotion_selector)
    document.addEventListener("DOMContentLoaded", fill_distortion_selector)
}

async function add_new_record(user_id){
    const currentdate = new Date();
    const datetime = currentdate.getFullYear() + "-"
                + (currentdate.getMonth()+1)  + "-"
                + currentdate.getDate() + " "
                + currentdate.getHours() + ":"
                + currentdate.getMinutes() + ":"
                + currentdate.getSeconds();
    const record_obj = {
        trigger_event: $('#event').val(),
        automated_thought: $('#auto_thought').val(),
        trust_level: $('#trust_lvl').val(),
        body_sens: $('#body_reaction').val(),
        behaviour: $('#behaviour_reaction').val(),
        rational_answer: $('#rational_answear').val(),
        conclusion: $('#conclusion').val(),
        date_time: datetime,
    };
    console.log(record_obj)
    const rawResponse = await fetch('http://localhost:8000/api/diary/add_record?' +
        new URLSearchParams({user_id: user_id}), {
            method: 'POST',
            headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(record_obj)
        });

    const created_record = await rawResponse.json();
    const emotion_obj = [{
        emotion_id: $('#emotion_selector').val(),
        intensity: $('#intensity_lvl').val(),
        record_id: created_record.id
    }];
    const emotionResponse = await fetch('http://localhost:8000/api/diary/add_record/emotion',
    {
            method: 'POST',
            headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(emotion_obj)
        });

    const distortion_obj = [{
        distortion_id: $('#distortion_selector').val(),
        record_id: created_record.id
    }];
    const distortionResponse = await fetch('http://localhost:8000/api/diary/add_record/distortion',
    {
            method: 'POST',
            headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(distortion_obj)
        });
    $("#record_table").empty();
    await fill_record_table(user_id);
    document.getElementById("adder_form").reset();
    console.log("success")
}

function setup_button_to_add(user_id){
    let button = document.getElementById("record_adder");
    button.addEventListener("click", function() {add_new_record(user_id);});
}

/*--------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------*/
/*----------------------------------RECORD HTML-----------------------------------------------*/
/*--------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------*/



function parse_url(){
    const url = window.location.href;
    return url.split('/').at(-1);
}

async function get_specific_record(){
    const record_id = parse_url()
    const response = await fetch(`http://localhost:8000/api/diary/records/1/${record_id}`);
    return await response.json();
}

async function get_emotion_record(){
    const record_id = parse_url()
    const response = await fetch('http://localhost:8000/api/diary/emotion_record?' +
            new URLSearchParams({record_id: record_id}));
    return await response.json();
}

async function get_distortion_record(){
    const record_id = parse_url()
    const response = await fetch('http://localhost:8000/api/diary/distortion_record?' +
            new URLSearchParams({record_id: record_id}));
    return await response.json();
}

async function fill_form(){
    const record_obj = await get_specific_record();
    const record_id = record_obj.id;
    const user_id = record_obj.user_id;
    delete record_obj.id;
    delete record_obj.user_id;
    delete record_obj.date_time;
    console.log(record_obj);
    for (const [key, value] of Object.entries(record_obj)){
        document.getElementById(key).setAttribute('value',value);
    }

    const emotion_record_obj = await get_emotion_record();
    const specific_emotion_record_obj = emotion_record_obj[0];
    console.log(specific_emotion_record_obj)
    delete specific_emotion_record_obj.record_id
    for (const [key, value] of Object.entries(specific_emotion_record_obj)){
        if (key==="intensity"){
            document.getElementById(key).setAttribute('value',value);
        }
        else{
            document.getElementById(key)[value].selected = true;
            document.getElementById(key).setAttribute('value',value);
        }
    }

    const distortion_record_obj = await get_distortion_record();
    const specific_distortion_record_obj = distortion_record_obj[0];
    delete specific_distortion_record_obj.record_id
    for (const [key, value] of Object.entries(specific_distortion_record_obj)){
        document.getElementById(key)[value].selected = true;
        document.getElementById(key).setAttribute('value',value);
    }
}

async function delete_record(){
    const record_id = parse_url();
    const user_id = 1;
    await fetch('http://localhost:8000/api/diary/delete_record?'+
        new URLSearchParams({
            user_id: user_id,
            record_id: record_id
        }),
    {
            method: 'DELETE',
            headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            },
        });
    window.location.replace("http://localhost:8000/app/diary/1")
}
