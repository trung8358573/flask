function validate_email(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

if ($('#post_modal')) {
    var post_modal = new Vue({
        el: '#post_modal',
        data: {
            title: '',
            subtitle: '',
            url: '',
            description: '',
            photo: '',
            votes: 1,
            invalid: {
                title: false,
                subtitle: false,
                url: false,
                description: false
            }
        },
        methods: {
            process_file: function(event) {
                this.photo = event.target.files[0]
            },
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
                        description: this.description,
                        photo: this.photo,
                        votes: this.votes
                    },
                    function (data, status) {
                        response = $.parseJSON(data);
                        if (response.status == 'success') {
                            signup_form.alert_success = true;
                            signup_form.alert_msg = response.msg;
                            signup_form.loading = false;
                        } else {
                            signup_form.alert_failed = true;
                            signup_form.alert_msg = 'failed';
                            signup_form.alert_msg = response.msg;
                            signup_form.loading = false;
                        }
                    }
                )
            }
        }
    });
}

if ($('#channel_modal')) {
    var channel_modal = new Vue({
        el: '#channel_modal',
        data: {
            title: '',
            description: '',
            private: false,
            invalid: {
                title: false
            },
            validation_msg: {
                title: '',
            },
            loading: false,
            alert_failed: false,
            alert_success: false,
            alert_msg: ''
        },
        methods: {
            validate: function (e) {
                if (this.title) {
                    if (this.title.length < 6 | this.title.length > 20) {
                        this.invalid.title = true;
                        this.validation_msg.title = 'Title has to be at least 6 characters and no longer than 20 characters';
                    }
                    if (!this.invalid.title) {
                        return true;
                    }
                    if (!this.title) {
                        this.invalid.title = true;
                    }
                }
            },
            clear_alerts: function () {
                this.alert_failed = false;
                this.alert_success = false;
                this.alert_msg = '';
            },
            send: function () {
                if (this.validate()) {
                    this.loading = true;
                    this.clear_alerts();
                    $.post('/create_channel', {
                            title: this.title,
                            description: this.description,
                            private: this.private
                        },
                        function (data, status) {
                            response = $.parseJSON(data);
                            if (response.status == 'success') {
                                signup_form.alert_success = true;
                                signup_form.alert_msg = response.msg;
                                signup_form.loading = false;
                            } else {
                                signup_form.alert_failed = true;
                                signup_form.alert_msg = 'failed';
                                signup_form.alert_msg = response.msg;
                                signup_form.loading = false;
                            }
                        }
                    );
                }
            }
        }
    });
}

var signup_form = new Vue({
    el: '#signup_modal',
    data: {
        username: '',
        password: '',
        password_confirm: '',
        email: '',
        username_login: '',
        password_login: '',
        remember: true,
        invalid: {
            username: false,
            password: false,
            password_confirm: false,
            email: false,
            username_login: false,
            password_login: false
        },
        validation_msg: {
            username: '',
            password: '',
            password_confirm: '',
            email: '',
            username_login: '',
            password_login: ''
        },
        loading: false,
        alert_failed: false,
        alert_success: false,
        alert_msg: ''
    },
    methods: {
        clear_alerts: function () {
            this.alert_failed = false;
            this.alert_success = false;
            this.alert_msg = '';
        },
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
                if (!validate_email(this.email)) {
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
        validate_login: function () {
            if (this.username_login && this.password_login) {
                if (this.username_login.length < 6 | this.username_login.length > 20) {
                    this.invalid.username_login = true;
                    this.validation_msg.username_login = 'Username has to be at least 6 characters and no longer than 20 characters';
                }
                if (this.password_login.length < 6 | this.password_login.length > 20) {
                    this.invalid.password_login = true;
                    this.validation_msg.password_login = 'Password has to be at least 6 characters and no longer than 20 characters';
                }
                if (!this.invalid.username_login && !this.invalid.password_login) {
                    return true;
                } else {
                    return false;
                }
            } else {
                if (!this.username) {
                    this.invalid.username_login = true;
                }
                if (!this.password) {
                    this.invalid.password_login = true;
                }
                return false;
            }
        },
        send: function () {
            if (this.validate()) {
                this.loading = true;
                this.clear_alerts();
                $.post('/signup', {
                        username: this.username,
                        password: this.password,
                        email: this.email
                    },
                    function (data, status) {
                        response = $.parseJSON(data);
                        if (response.status == 'success') {
                            signup_form.alert_success = true;
                            signup_form.alert_msg = response.msg;
                            signup_form.loading = false;
                        } else {
                            signup_form.alert_failed = true;
                            signup_form.alert_msg = 'failed';
                            signup_form.alert_msg = response.msg;
                            signup_form.loading = false;
                        }
                    }
                );
            }
        },
        send_login: function () {
            if (this.validate_login()) {
                this.loading = true;
                this.clear_alerts();
                $.post('/login', {
                        username: this.username_login,
                        password: this.password_login,
                        remember: this.remember
                    },
                    function (data, status) {
                        response = $.parseJSON(data);
                        if (response.status == 'success') {
                            signup_form.alert_success = true;
                            signup_form.alert_msg = 'Login successful!';
                            signup_form.loading = false;
                            location.reload();
                        } else {
                            signup_form.alert_failed = true;
                            signup_form.alert_msg = 'failed';
                            signup_form.alert_msg = 'Login unsuccessful, please check your username and password';
                            signup_form.loading = false;
                        }
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
        posts: posts
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
                time: '2018-08-13 00:55:05.828713',
                description: ''
            });
        },
        check_dark: function () {
            if ($('#dark_switch').is(":checked")) {
                return true;
            } else {
                return false;
            }
        },
        time: function (post) {
            return moment(post.time).fromNow();
        }
    }
});

var sidebar = new Vue({
    el: '#sidebar',
    data: {
        channels: channels
    },
    methods: {}
});

function dark() {
    var style = $('#style');
    if (style.attr("href") === '../static/theme.css') {
        style.attr("href", '../static/dark.css');
        $('body').removeClass('bg-light');
        $('.card').addClass('border-dark');
        $('#top_bar').addClass('border-bottom border-dark');
    } else {
        style.attr("href", '../static/theme.css');
        $('body').addClass('bg-light');
        $('.card').removeClass('border-dark');
        $('#top_bar').removeClass('border-bottom border-dark');
    }

}