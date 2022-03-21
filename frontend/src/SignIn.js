// Import the functions you need from the SDKs you need
import React, { Component, useState } from "react";
import {
  BrowserRouter as BrowserRouter,
  Routes,
  Route,
  Link,
} from "react-router-dom";

import "./App.css";

import { useNavigate, Navigate } from "react-router-dom";
// import { useNavigation } from "@react-navigation/native";
import { auth } from "./Firebase";

import { getAuth, GoogleAuthProvider, signInWithPopup } from "firebase/auth";


function SignIn() {
  const history = useNavigate();

  const signInWithGoogle = () => {
    const provider = new GoogleAuthProvider();
    // const navigate = useNavigate();
    signInWithPopup(auth, provider)
      .then((result) => {
        const name = result.user.displayName;
        const email = result.user.email;
        const profilePic = result.user.photoURL;
        localStorage.setItem("name", name);
        localStorage.setItem("email", email);
        localStorage.setItem("profilePic", profilePic);
        console.log(result);
        console.log("KhoaPham");
        history("/test");
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <div>
      <div className='container dark'>
        <div className='ti'>
          <button onClick={signInWithGoogle}>Sign In With Google</button>
          {/* <h1>{localStorage.getItem("name")}</h1>
          <h1>{localStorage.getItem("email")}</h1>
          <h1>{localStorage.getItem("profilePic")}</h1> */}
        </div>
        {/* <div className='teo'>
          <button onClick={signOut}>Sign Out</button>
          <h1>{localStorage.getItem("name")}</h1>
          <h1>{localStorage.getItem("email")}</h1>
          <h1>{localStorage.getItem("profilePic")}</h1>
        </div> */}
      </div>
    </div>
  );
}

export default SignIn;
