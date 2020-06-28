<template>
    <nav class="navbar navbar-expand-lg bg-dark navbar-dark sticky-top">
        <div class="container">
            <a class="navbar-brand" href="#">Orion</a>

            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsedNavbar">
                <span class="navbar-toggler-icon"/>
            </button>

            <div class="collapse navbar-collapse" id="collapsedNavbar">
                <ul class="nav navbar-nav ml-auto">
                    <a class="nav-item nav-link" href="#">Past Projects</a>
                    <a class="nav-item nav-link" href="#">Resume</a>
                    <a class="nav-item nav-link" href="#">About Me</a>
                    <a class="nav-item nav-link" href="#">Get In Touch</a>
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