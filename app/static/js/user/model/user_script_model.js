
const modal = document.querySelector(".user_modal");
const edit_user_modal = document.querySelector(".edit_user_modal");

$("#add_user").on("click", function (e){
    e.preventDefault();
    console.log("Add User....")
    toggleUserModal();
})


$(".modal_container_close").on("click", function (e){
  toggleUserModal();
  document.querySelector("#post_user").reset();
  $(".form-group").removeClass("has-error");
  $("#post_user").validate().resetForm();

})

$(modal).on("click", function(event){
     if(event.currentTarget === event.target){
        toggleUserModal();
    }
})

function toggleUserModal(){
    if(modal.style.display === "flex"){
        modal.style.display = "none"
    }
    else{
        modal.style.display = "flex"
    }
}



$(".edit_modal_container_close").on("click", function (e){
    toggleUserEditModal();
    document.querySelector("#edit_user").reset();
    $(".form-group").removeClass("has-error");
     $("#edit_user").validate().resetForm();
  })
  
  $(edit_user_modal).on("click", function(event){
       if(event.currentTarget === event.target){
          toggleUserEditModal();
      }
  });
  
function toggleUserEditModal(data){
    if(edit_user_modal.style.display === "flex"){
        edit_user_modal.style.display = "none"
    }
    else{
        edit_user_modal.querySelector("#userId").value = data.id;
        edit_user_modal.querySelector("#edit_user_name").value = data.user_name;
        edit_user_modal.querySelector("#edit_full_name").value = data.full_name;
        edit_user_modal.querySelector("#edit_email").value = data.email;
        edit_user_modal.querySelector("#edit_phone_number").value = data.phone_number;
        edit_user_modal.querySelector("#edit_specilist").value = data.specilist;
        // edit_user_modal.querySelector("#edit_role").value = data.role;
        edit_user_modal.querySelector("#edit_district").value = data.district;
        edit_user_modal.querySelector("#edit_city").value = data.city;
        edit_user_modal.querySelector("#edit_ward").value = data.ward;
        console.log($("input[name=is_superuser]:checked").value);
        const is_superuser = data.is_superuser.toString()[0].toUpperCase() + data.is_superuser.toString().slice(1)
        const is_active = data.is_active.toString()[0].toUpperCase() + data.is_active.toString().slice(1)
        $("input[name='is_superuser'][value="+is_superuser+"]").prop('checked', true);
        $("input[name='is_active'][value="+is_active+"]").prop('checked', true)
        edit_user_modal.style.display = "flex"
    }
}
