// add role
const add_role_modal = document.querySelector(".add_role_modal")
const edit_role_modal = document.querySelector(".edit_role_modal");


$("#add_role").on("click", function (e){
    e.preventDefault();
    console.log("Add bill....")
    toggleRoleModal();
})
$(".modal_container_close").on("click", function (e){
    toggleRoleModal();
    document.querySelector("#post_role").reset();
  })
function toggleRoleModal(){

    if(add_role_modal.style.display === "flex"){
        add_role_modal.style.display = "none";
    }
    else{
        add_role_modal.style.display = "flex";
    }
}


$(".edit_modal_container_close").on("click", function (e){
    toggleEditRoleModal();
    document.querySelector("#edit_name").reset();
  })
  
  
  function toggleEditRoleModal(data){
      if(edit_role_modal.style.display === "flex"){
          edit_role_modal.style.display = "none";
      }
      else{
          edit_role_modal.querySelector("#roleId").value = data.id;
          edit_role_modal.querySelector("#edit_name").value = data.name;
          edit_role_modal.style.display = "flex";
      }
  }
