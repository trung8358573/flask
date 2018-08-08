function validate_email(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

var head = new Vue({
    el: 'head',
    data: {
        dark: false
    },
    methods: {}
});

var post_form = new Vue({
    el: '#post_form',
    data: {
        title: '',
        subtitle: '',
        url: '',
        description: '',
        invalid: {
            title: false,
            subtitle: false,
            url: false,
            description: false
        }
    },
    methods: {
        validate: function (e) {
            if (this.title && this.url) {
                return true;
            }
            if (!this.title) {
                this.invalid.title = true;
            }
            if (!this.url) {
                this.invalid.url = true;
            }
        },
        send: function () {
            $.post('/post', {
                    title: this.title,
                    subtitle: this.subtitle,
                    url: this.url,
                    description: this.description
                },
                function (data, status) {

                }
            )

        }

    }

});

var signup_form = new Vue({
    el: '#signup_modal',
    data: {
        username: '',
        password: '',
        password_confirm: '',
        email: '',
        invalid: {
            username: false,
            password: false,
            password_confirm: false,
            email: false
        },
        validation_msg: {
            username: '',
            password: '',
            password_confirm: '',
            email: ''
        }
    },
    methods: {
        validate: function () {
            if (this.username && this.password && this.password_confirm == this.password && this.email) {
                if (this.username.length < 6 | this.username.length > 20) {
                    this.invalid.username = true;
                    this.validation_msg.username = 'Username has to be at least 6 characters and no longer than 20 characters';
                }
                if (this.password.length < 6 | this.password.length > 20) {
                    this.invalid.password = true;
                    this.validation_msg.password = 'Password has to be at least 6 characters and no longer than 20 characters';
                }
                if (validate_email(this.email)) {
                    this.invalid.email = true;
                    this.validation_msg.email = 'Please provide a valid email';
                }
                if (!this.invalid.email && !this.invalid.username && !this.invalid.password) {
                    return true;
                } else {
                    return false;
                }
            } else {
                if (!this.username) {
                    this.invalid.username = true;
                }
                if (!this.password) {
                    this.invalid.password = true;
                }
                if (!this.password_confirm) {
                    this.invalid.password_confirm = true;
                }
                if (!this.email) {
                    this.invalid.email = true;
                }
                if (this.password_confirm != this.password) {
                    this.invalid.password = true;
                    this.invalid.password_confirm = true;
                    this.validation_msg.password = 'Password does not match';
                }
                return false;
            }
        },
        send: function () {
            if (this.validate()) {
                $.post('/post', {
                        username: this.username,
                        password: this.password,
                        email: this.password_confirm
                    },
                    function (data, status) {
                        response = $.parseJSON(data);
                    }
                );
            }
        },
        clear: function () {
            this.invalid.username = false;
            this.invalid.password = false;
            this.invalid.password_confirm = false;
            this.invalid.email = false;
        }
    }
});

var feed = new Vue({
    el: '#feed',
    data: {
        posts: [{
            title: 'LPT: How to Wake Up in the Morning',
            url: '../static/post2.jpg',
            user: {
                name: 'tim tran',
                pic: '../static/user.jpg',
            },
            channel: {
                name: 'memes',
                pic: '../static/channel.png'
            },
            vote: 100,
            time: '',
            description: ''
        }]
    },
    methods: {
        load_more: function () {
            this.posts.push({
                title: 'LPT: How to Wake Up in the Morning',
                url: '../static/post2.jpg',
                user: {
                    name: 'tim tran',
                    pic: '../static/user.jpg',
                },
                channel: {
                    name: 'memes',
                    pic: '../static/channel.png'
                },
                vote: 100,
                time: '',
                description: ''
            });
        },
        check_dark: function () {
            if ($('#dark_switch').is(":checked")) {
                return true;
            } else {
                return false;
            }
        }
    }
});

var sidebar = new Vue({
    el: '#sidebar',
    data: {
        channels: [{
                title: 'Funny',
                url: '#',
                pic: '../static/channel.png',
            },
            {
                title: 'Animals',
                url: '#',
                pic: '../static/channel.png',
            },
        ]
    },
    methods: {}
});

function dark() {
    var style = $('#style');
    if (style.attr("href") == '../static/theme.css') {
        style.attr("href", '../static/dark.css');
        $('body').removeClass('bg-light');
        $('#feed .card').addClass('border-dark');
        $('#left_col .card').addClass('border-dark');
        $('#top_bar').addClass('border-bottom border-dark');
    } else {
        style.attr("href", '../static/theme.css');
        $('body').addClass('bg-light');
        $('#feed .card').removeClass('border-dark');
        $('#left_col .card').removeClass('border-dark');
        $('#top_bar').removeClass('border-bottom border-dark');
    }

}