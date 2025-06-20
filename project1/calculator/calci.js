// script.js

var timeout;

function circleChaptaKaro(){
    var xscale=1;
    var yscale=1;

    var xprev=0;
    var yprev=0;

    window.addEventListener("mousemove", function(dets){
        clearTimeout(timeout)

        xscale=gsap.utils.clamp(.8,1.2,dets.clientX - xprev);
        yscale=gsap.utils.clamp(.8,1.2,dets.clientY - yprev);

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
// Sample water footprint data (replace with actual data)
const waterFootprintData = {
    item1: 50, // Water footprint of Item 1 in liters
    item2: 30,
    item3: 70,
    item4: 80 // Water footprint of Item 2 in liters
    // Add more items and their footprints
};

document.addEventListener('DOMContentLoaded', function () {
    const itemDropdown = document.getElementById('item');
    const quantityInput = document.getElementById('quantity');
    const calculateButton = document.getElementById('calculate-button');
    const resultValue = document.getElementById('footprint-value');

    calculateButton.addEventListener('click', function () {
        const selectedItem = itemDropdown.value;
        const quantity = parseFloat(quantityInput.value);
        const waterFootprint = waterFootprintData[selectedItem] * quantity;

        resultValue.textContent = `${waterFootprint.toFixed(2)} liters`;
    });
});
