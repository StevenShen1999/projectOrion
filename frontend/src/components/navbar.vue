<template>
    <nav class="navbar navbar-expand-md bg-dark navbar-dark sticky-top" style="background-color: black !important">
        <div class="container">
            <a class="navbar-brand"><router-link class="no-style" to="/">Orion</router-link></a>

            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsedNavbar">
                <span class="navbar-toggler-icon"/>
            </button>

            <div class="collapse navbar-collapse" id="collapsedNavbar">
                <ul class="nav navbar-nav ml-auto">
                    <a class="nav-item nav-link no-style" href="http://www.stevenshen.co/serve" target="_blank">Resume</a>
                    <a class="nav-item nav-link no-style block">Past Projects</a>
                    <a class="nav-item nav-link"><router-link class="no-style" to="/contact" exact>Get In Touch</router-link></a>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
  name: 'navbar'
}
</script>

<style>
.no-style{
    text-decoration: none;
    color: inherit;
}

.no-style:hover{
    text-decoration: none;
    color: inherit;
}

.block:hover {
    cursor:not-allowed;
}
</style>
