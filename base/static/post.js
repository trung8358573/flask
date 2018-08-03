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
        }
    },
    methods: {
        validate: function () {
            if (this.username && this.password && this.password_confirm == this.password && this.email) {
                return true;
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
                }
                return false;
            }
        },
        send: function () {
            if (this.validate()) {
                $.post('/post', {
                        username: this.username,
                        password: this.password,
                        email: this.email
                    },
                    function (data, status) {}
                );
            }
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
                user_pic: '',
            },
            channel: 'memes',
            vote: '',
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
                    user_pic: '',
                },
                channel: 'memes',
                vote: '',
                time: '',
                description: ''
            });
        }
    }
});

var sidebar = new Vue({
    el: '#sidebar',
    data: {
        channels: [{
                title: 'Funny',
                url: '#',
                pic: '',
            },
            {
                title: 'Animals',
                url: '#',
                pic: '',
            },
        ]
    },
    methods: {}
});