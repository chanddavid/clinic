
const add_staff_modal = document.querySelector(".add_staff_modal")

$("#add_staff_role").on("click", function (e) {
    e.preventDefault();
    console.log("Add role staff....")
    toggleAddStaffRoleModal();
})

$(".modal_container_close").on("click", function (e){
    toggleAddStaffRoleModal();
    document.querySelector("#post_user_roles").reset();
  })
function toggleAddStaffRoleModal() {
    if (add_staff_modal.style.display === "flex") {
        add_staff_modal.style.display = "none";
    }
    else {
        add_staff_modal.style.display = "flex";
    }
}
