const staffdetail_modal = document.querySelector(".staffdetail_modal")


$("#add_staff").on("click", function (e){
    e.preventDefault();
    console.log("Add opd....")
    toggleStaffDetailModal();
})
$(".modal_container_close").on("click", function (e){
    toggleStaffDetailModal();
    document.querySelector("#post_data").reset();
  })
function toggleStaffDetailModal(){

    if(staffdetail_modal.style.display === "flex"){
        staffdetail_modal.style.display = "none";
    }
    else{
        staffdetail_modal.style.display = "flex";
    }
}
