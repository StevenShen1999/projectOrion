<template>
    <nav class="navbar navbar-expand-md bg-dark navbar-dark sticky-top" style="background-color: black !important">
        <div class="container">
            <a class="navbar-brand"><router-link to="/">Orion</router-link></a>

            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsedNavbar">
                <span class="navbar-toggler-icon"/>
            </button>

            <div class="collapse navbar-collapse" id="collapsedNavbar">
                <ul class="nav navbar-nav ml-auto">
                    <a class="nav-item nav-link" href="http://127.0.0.1:5000/serve" target="_blank">Resume</a>
                    <a class="nav-item nav-link">Past Projects</a>
                    <a class="nav-item nav-link"><router-link to="/contact" exact>Get In Touch</router-link></a>
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

</style>
