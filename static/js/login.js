delegateEvent = (node, cssPath, eventName, callbackFn) => {
  const evHandler = ev => {
    if (ev.target.matches(cssPath)) {
      callbackFn.call(ev.target, ev);
    }
  };
  node.addEventListener(eventName, evHandler);

  return () => node.removeEventListener(eventName, evHandler);
};

const signInBlock = document.getElementById("sign-in-block");
const registerBlock = document.getElementById("register-block");
const signInBut = document.getElementById("sign-in-button");
const registerBut = document.getElementById("register-button");

delegateEvent(document.querySelector(".Login-block"), "#sign-in-button", "click", ev=>{
    if (!ev.target.classList.contains("Login-block__toggle--selected")){
        ev.target.classList.add("Login-block__toggle--selected");
        registerBut.classList.remove("Login-block__toggle--selected");
        signInBlock.style.display = "flex";
        registerBlock.style.display = "none";
    }
});


delegateEvent(document.querySelector(".Login-block"), "#register-button", "click", ev=>{
    if (!ev.target.classList.contains("Login-block__toggle--selected")){
        ev.target.classList.add("Login-block__toggle--selected");
        signInBut.classList.remove("Login-block__toggle--selected");
        registerBlock.style.display = "flex";
        signInBlock.style.display = "none";
    }
});