<template>
  <div class="container-fluid">
    <HeaderBar/>
    <div class="list">hello</div>
    <div class="art">ok</div>
    <ul>
      <li>ll</li>
      <li>kk</li>
      <li>hh</li>
    </ul>
    <button type="button" class="btn btn-default">default</button>
    <button type="button" class="btn btn-success">default</button>
    <button type="button" class="btn btn-info">default</button>
    <span class="input-group-btn">
      <button type="button" class="btn btn-default">Go!</button>
    </span>
    <form action="" method="POST" class="form-horizontal" role="form">
        <div class="form-group">
          <legend>Form title</legend>
        </div>
    
        
    
        <div class="form-group">
          <div class="col-sm-10 col-sm-offset-2">
            <button type="submit" class="btn btn-primary">Submit</button>
          </div>
        </div>
    </form>
    
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
