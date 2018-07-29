/*
$('#send_post').click(function(event){
    $.post('/post', {
        title: $('#inputTitle').val(),
        url: $('#inputTitle').val(),
        description: $('#inputTitle').val(),
    });
    event.preventDefault();
});
*/
var post_form = new Vue({
    el: '#post_form',
    data:{
        title: '',
        subtitle: '',
        url :'',
        description:'',
        invalid:{
            title:false,
            subtitle:false,
            url:false,
            description:false
        }
    },
    methods:{
        validate: function(e){
            if(this.title && this.url){
                return true;
            }
            if(!this.title){
                this.invalid.title = true;
            }
            if(!this.url){
                this.invalid.url = true;
            }
        },
        send: function(){
            $.post('/post',{
                title: this.title,
                subtitle: this.subtitle,
                url: this.url,
                description: this.description
            },
                function(data,status){

                }
            )

        }

    }

})