var overlay = document.getElementById("overlay");

// Buttons to 'switch' the page
var openSignUpButton = document.getElementById("slide-left-button");
var openSignInButton = document.getElementById("slide-right-button");

// The sidebars
var leftText = document.getElementById("sign-in");
var rightText = document.getElementById("sign-up");

// The forms
var accountForm = document.getElementById("sign-in-info")
var signinForm = document.getElementById("sign-up-info");

// Open the Sign Up page
openSignUp = () =>{
  // Remove classes so that animations can restart on the next 'switch'
  leftText.classList.remove("overlay-text-left-animation-out");
  overlay.classList.remove("open-sign-in");
  rightText.classList.remove("overlay-text-right-animation");
  // Add classes for animations
  accountForm.className += " form-left-slide-out"
  rightText.className += " overlay-text-right-animation-out";
  overlay.className += " open-sign-up";
  leftText.className += " overlay-text-left-animation";
  // hide the sign up form once it is out of view
  setTimeout(function(){
    accountForm.classList.remove("form-left-slide-in");
    accountForm.style.display = "none";
    accountForm.classList.remove("form-left-slide-out");
  }, 700);
  // display the sign in form once the overlay begins moving right
  setTimeout(function(){
    signinForm.style.display = "flex";
    signinForm.classList += " form-right-slide-in";
  }, 200);
}

// Open the Sign In page
openSignIn = () =>{
  // Remove classes so that animations can restart on the next 'switch'
  leftText.classList.remove("overlay-text-left-animation");
  overlay.classList.remove("open-sign-up");
  rightText.classList.remove("overlay-text-right-animation-out");
  // Add classes for animations
  signinForm.classList += " form-right-slide-out";
  leftText.className += " overlay-text-left-animation-out";
  overlay.className += " open-sign-in";
  rightText.className += " overlay-text-right-animation";
  // hide the sign in form once it is out of view
  setTimeout(function(){
    signinForm.classList.remove("form-right-slide-in")
    signinForm.style.display = "none";
    signinForm.classList.remove("form-right-slide-out")
  },700);
  // display the sign up form once the overlay begins moving left
  setTimeout(function(){
    accountForm.style.display = "flex";
    accountForm.classList += " form-left-slide-in";
  },200);
}



// When a 'switch' button is pressed, switch page
openSignUpButton.addEventListener("click", openSignUp, false);
openSignInButton.addEventListener("click", openSignIn, false);






console.clear();

// you can find the server side code at 'https://repl.it/@mauriciolobo/expensetracker'
// Just replace with you address and start playing arround
var url = "https://expensetracker--mauriciolobo.repl.co/"

Vue.filter("money", v => {  
  return "$" + parseFloat(v).toFixed(2);
});

var app = new Vue({
  el: "#app",
  
  data() {
    return {
      transactions: [],
      transaction: {}
    };
  },
  
  computed: {
    balance() {
      return this.transactions.reduce((c, p) => c + p.amount, 0);
    },
    
    income() {
      return this.transactions
        .filter(f => f.amount > 0)
        .reduce((c, p) => c + p.amount, 0);
    },
    
    expense() {      
      return this.transactions
        .filter(f => f.amount < 0)
        .reduce((c, p) => c + p.amount, 0);
    }    
  },
  
  methods: {
    
    get(){
      axios.get(url)
        .then(r=>r.data)
        .then(r=>r.map(m=>{return {...m, amount: parseFloat(m.amount)}}))
        .then(r=>this.transactions = r)
    },
    
    add() {
      axios
        .post(url, this.transaction)
        .then(t=>t.data)        
        .then(() => {
          this.transaction = {};
        })
        .then(()=>{
          this.get()
        })
        .catch(console.error);
    }
  },
  
  mounted(){
    this.get()
  }
});
