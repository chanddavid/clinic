let datatables =
    $('#user_datatable').DataTable({
        pageLength: 10,
        fixedHeader: true,
        responsive: true,
        ajax: {
            url: "list/",
            type: "GET",
        },
        columns: [
            { "data": "id" },
            { "data": "user" },
            { "data": "roles" },
            {
                data: null,
                className: "center",
                defaultContent: '<a onclick="delete_user_roles(this)" class="text-muted font-16" style="margin-right: 10px" id="delete_btn"><i class="fas fa-trash-alt"></i></a> ' +
                    '<a onclick="get_user_role_edit_modal(this)" class="text-muted font-16" id="edit_btn"><i class="far fa-edit"></i></a>'
            }
        ],
        "sDom": 'rtip',
        columnDefs: [{
            targets: 'no-sort',
            orderable: false
        }],
    });


$("#post_user_roles").on("submit", function (e) {
    e.preventDefault();
    $.ajax({
        url: "create/",
        type: 'post',
        dataType: 'json',
        data: {
            user: $('#user').val(),
            role: $('#role').val(),
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
        },

        success: function (data) {
            toggleAddStaffRoleModal();
            Swal.fire({
                position: 'top-end',
                icon: 'success',
                title: `${data.user} role has been created`,
                showConfirmButton: false,
                timer: 1500
            })
            document.querySelector('#post_user_roles').reset();
            datatables.ajax.reload();
        }
    })
})
