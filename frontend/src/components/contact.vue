<template>
    <div id="contact">
        <div class="jumbotron">
            <h1 class="h1-responsive font-weight-bold text-center">Get In Touch</h1>
            <div style="width: 75%; margin: 0 auto;">
                <p class="w-responsive text-center mx-0">If you would like to get in touch with me, feel free to send me a message using the panel to the bottom left of this section, or using the social media links on the right.</p>
            </div>
        </div>

        <div class="container">
            <div class="row">
                <div class="col-6" style="border-right: 1px solid lightgrey">
                    <form v-if="!submitted" @submit.prevent="sendMail">
                        <div class="form-group">
                            <label for="emailInput"><b>Your email address</b></label>
                            <input type="email" class="form-control" id="emailInput" v-model="message.email" required />
                        </div>
                        <div class="form-group">
                            <label for="nameInput"><b>Your name</b></label>
                            <input type="text" class="form-control" id="nameInput" v-model="message.name" required />
                        </div>
                        <div class="form-group">
                            <label for="messageContent"><b>Your message</b></label>
                            <textarea class="form-control" id="emailInput" v-model="message.payload" required />
                        </div>
                        <button type="submit" class="btn btn-primary">Send</button>
                    </form>
                    <div v-else class="d-flex flex-column justify-content-center align-items-center" style="height: 100%">
                        <div style="display: block">
                            <p v-if="success" class="display-5"><b>Success</b></p>
                            <p v-else class="display-5" style="color: red;"><small>Failed, server error</small></p>
                        </div>
                        <button class="btn btn-secondary" style="display: block" @click="restart">Send Another Message</button>
                    </div>
                </div>
                <div class="col-6 d-flex justify-content-center align-items-center">
                    <ul class="list-unstyled">
                        <li>
                            <a href="https://www.linkedin.com/in/steven-shen-0215b140/" class="fa fa-linkedin" target="_blank" rel="noopener noreferrer"/>
                        </li>
                        <li>
                            <a href="https://github.com/StevenShen1999" class="fa fa-github" target="_blank" rel="noopener noreferrer" />
                        </li>
                        <li>
                            <a href="" class="fa fa-twitter" target="_blank" rel="noopener noreferrer" />
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "contact",
    data() {
        return {
            message: {
                email: '',
                name: '',
                payload: ''
            },
            success: false,
            submitted: false
        }
    },
    methods: {
        sendMail(){
            console.log("Entered")
            // TODO: Finish hooking this up with the backend
            this.$http.post("http://127.0.0.1:5000/send", {
                message: this.message
            }).then((data) => {
                if (data.status == 200){
                    this.success = true
                    this.submitted = true
                }
            })
        }, 
        restart(){
            this.submitted = false
            this.message = {
                email: '',
                name: '',
                payload: ''

            }
        }
    }
}
</script>

<style>
.fa {
  padding: 20px;
  font-size: 30px;
  width: 50px;
  text-align: center;
  text-decoration: none;
}
</style>