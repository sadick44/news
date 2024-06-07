    $(document).ready(function(){
        var deviceSize = document.documentElement.clientWidth
        if (deviceSize < 1280){
            $('#all_type').hide()
            $('#mobile_type').show()
        }

        else{
             $('#all_type').show()
            $('#mobile_type').hide()
        }


        if (deviceSize > 766){
            $("footer").addClass("fixed-bottom")
        }
    })

    })
