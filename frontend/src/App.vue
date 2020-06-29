<template>
    <div id="app">
        <navbar />
        <router-view />
        <br /><br />
        <foot />
    </div>
</template>

<script>
import navbar from './components/navbar'
import foot from './components/foot'

export default {
  name: 'app',
  components: {
    navbar,
    foot
  },
  data () {
    return {
    }
  }
}
</script>

<style>
</style>
