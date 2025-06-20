var timeout;

function circleChaptaKaro(){
    var xscale=1;
    var yscale=1;

    var xprev=0;
    var yprev=0;

    window.addEventListener("mousemove", function(dets){
        clearTimeout(timeout)

        xscale=gsap.utils.clamp(0.8,1.2,dets.clientX - xprev);
        yscale=gsap.utils.clamp(0.8,1.2,dets.clientY - yprev);

          xprev=dets.clientX;
          yprev=dets.clientY;

        circleMouseFollower(xscale,yscale);
        timeout = setTimeout(function () {
            document.querySelector(
              "#minicircle"
            ).style.transform = `translate(${dets.clientX}px, ${dets.clientY}px) scale(1, 1)`;
          }, 100);
    })
}

circleChaptaKaro();

function circleMouseFollower(xscale, yscale) {
    window.addEventListener("mousemove", function (dets) {
      document.querySelector(
        "#minicircle"
      ).style.transform = `translate(${dets.clientX}px, ${dets.clientY}px) scale(${xscale}, ${yscale})`;
    });
  }
  
  circleMouseFollower();

function circleMouseFollower(xscale, yscale) {
  window.addEventListener("mousemove", function (dets) {
    document.querySelector(
      "#minicircle"
    ).style.transform = `translate(${dets.clientX}px, ${dets.clientY}px) scale(${xscale}, ${yscale})`;
  });
}

circleMouseFollower();