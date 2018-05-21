Vue.component('app-header', {
    template: `
        <header>
            <nav class="navbar navbar-expand-lg navbar-dark bg-nav fixed-top">
              <router-link class="nav-link" to=""><img src="/static/images/logo.png" height="48px" width="120px" alt="Logo"></router-link>
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                </ul>
                
                <ul class="navbar-nav">
                <li class="nav-item active">
                    <router-link class="nav-link" to="/" v-if = '!userLoggedIn'>Home<span class="sr-only">(current)</span></router-link>
                </li>
                <li class="nav-item active">
                    <router-link class="nav-link" :to="'/users/' + current_user" v-if = 'userLoggedIn'>My Profile<span class="sr-only">(current)</span></router-link>
                </li>
                <li class="nav-item active">
                    <router-link class="nav-link" to="/login" v-if  = '!userLoggedIn'>Login<span class="sr-only">(current)</span></router-link>
                </li>
                <li class="nav-item active">
                    <router-link class="nav-link" to="/register" v-if   = '!userLoggedIn'>Sign Up<span class="sr-only">(current)</span></router-link>
                </li>
                <li class="nav-item active">
                    <router-link class="nav-link" to="/logout" v-if = 'userLoggedIn'>Logout<span class="sr-only">(current)</span></router-link>
                </li>
                </ul>
              </div>
            </nav>
        </header>    
    `,
    data: function() {
            return {
                userLoggedIn:this.isLoggedIn()
            };
        },
        created:
            function(){
                let self =this;
                this.current_user = localStorage.getItem('current_user');
                console.log("Logged in: " + this.userLoggedIn);
                this.userLoggedIn = this.isLoggedIn();
      
            },
        methods:{
                isLoggedIn: function(){
                    return !(localStorage.getItem('jtoken')==null);
                }
        }
});
Vue.component('app-footer', {
    template: `
    <footer>
        <div class="container">
            <p>Created by Group4</p>
        </div>
    </footer>
    `
});

const Menu = Vue.component('app-sidepanel', {
    template: `
    <div id="contentLeft">


    <ul id="leftNavigation">
    {% for key in courselist %}
        {% for value in courselist[key] %}
      <li class="active" id="{{ key[0] }}>"> <a href=#><i class="fa fa-coffee leftNavIcon"></i>  {{ key[0] }} </a>
          <ul>
            {% for n in value %}
          <li> <a class="test" href='{{ url_for("tests", cour =key[0] ,toc =n[0] )}}' data-tid="{{n[0] }}"> {{ n[0] }}</a> </li>
            {% endfor %}
        </ul>

      </li>
        {% endfor %}
 {% endfor %}

    </ul>
  </div>
    `,
    data: function() {
            return {
               
            };
        },
        watch:{
            '$route' (to, from){
                let user_id = to.params.user_id;
                this.$router.go(to);
            }
        }
});

const Right = Vue.component('levelscontainer', {
    template: `
    
    `,
    data: function() {
            return {
                welcome: 'Let the World See the Best You.'
            };
        },
        watch:{
            '$route' (to, from){
                let user_id = to.params.user_id;
                this.$router.go(to);
            }
        }
});

const Task = vue.component('taskcontainer',{
  template:`
  `,
  data: function(){
    return{};
  },
  
});