const bill_model = document.querySelector(".bill_model")

$("#generate").on("click", function (e){
    e.preventDefault();
    console.log("Add bill....")
    toggleBillModal();
})
$(".modal_container_close").on("click", function (e){
    toggleBillModal();
    document.querySelector("#post_data").reset();
  })
function toggleBillModal(){

    if(bill_model.style.display === "flex"){
        bill_model.style.display = "none";
    }
    else{
        bill_model.style.display = "flex";
    }
}


let generate=document.getElementById('generate')
generate.addEventListener('click',()=>{
    document.getElementsByClassName("addbillbtn")[0].classList.remove("d-none")
})



