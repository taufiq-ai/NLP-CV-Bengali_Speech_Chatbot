navigator.mediaDevices.getUserMedia({ video: true })
.then(stream => {
    let video = document.getElementById('camera-stream');
    video.srcObject = stream;
    video.play();
})
.catch(error => {
    console.log(error);
});

$(document).ready(() => {
let canvas = document.getElementById('camera-canvas');
let context = canvas.getContext('2d');

$('#camera-capture').click(() => {
    let video = document.getElementById('camera-stream');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    let dataURL = canvas.toDataURL('image/jpeg');
    let formData = new FormData();
    formData.append('image', dataURL);
    $.ajax({
        url: '/upload',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: (response) => {
            console.log(response);
        },
        error: (error) => {
            console.log(error);
        }
    });
});
});