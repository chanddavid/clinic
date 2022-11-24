
let all_invoice_modal=document.querySelector('.all_invoice_modal')
$("#viewinvoice").on("click", function (e){
    e.preventDefault();
    console.log("Add bill invoice....")
    toggleBillInvoiceModal();
})
$(".modal_container_close").on("click", function (e){
    toggleBillInvoiceModal();
    document.querySelector("#post_data").reset();
  })
function toggleBillInvoiceModal(){

    if(all_invoice_modal.style.display === "flex"){
        all_invoice_modal.style.display = "none";
    }
    else{
        all_invoice_modal.style.display = "flex";
    }
}