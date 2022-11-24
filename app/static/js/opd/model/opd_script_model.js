const modal = document.querySelector(".device_modal")


$("#add_opd").on("click", function (e){
    e.preventDefault();
    console.log("Add opd....")
    toggleOPDModal();
})
$(".modal_container_close").on("click", function (e){
    toggleOPDModal();
    document.querySelector("#post_data").reset();
  })
function toggleOPDModal(){

    if(modal.style.display === "flex"){
        modal.style.display = "none";
    }
    else{
        modal.style.display = "flex";
    }
}
