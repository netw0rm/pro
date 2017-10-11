<template>
  <div class="container">
    <HeaderBar/>
    <div class="list">hello</div>
    <div class="art">ok</div>
    <ul>
      <li>ll</li>
      <li>kk</li>
      <li>hh</li>
    </ul>
    <button type="button" class="btn btn-default">default</button>
    <SlideBar/>
    <FooterBar/>
  </div>
</template>

<script>
import HeaderBar from '~/components/HeaderBar.vue'
import FooterBar from '~/components/FooterBar.vue'
export default {
  components: {
    HeaderBar,
    FooterBar
  }

}
</script>

<style>
.list {
  margin: 1px;
  font-size: 10em;
  color: forestgreen;
}
.art {
  font-size: 8em;
  color: burlywood;
}

</style>
