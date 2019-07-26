<template lang="html">

  <section class="items">
    <h1>items Component</h1>
    
    <div v-for="item in items.data">
      <p>{{ item.title }}</p>
      <p>{{ item.description }}</p>
      <p>{{ item.price }}</p>
      <p>{{ item.created_date }}</p>
      <p>{{ item.reviews.length }}</p>
      
      <span v-for="image in item.attachments">
        <div class="thumbnail col-sm-4 row">
          <img :src="`data:image/png;base64,${image.base64_image}`" style="max-width:100%;max-height:100%;" alt="`${image.image}`" class="card-img-top img-fluid"/>
        </div>
      </span>
    </div>
  </section>

</template>

<script lang="js">
  import axios from "axios";

  export default  {
    name: 'items',
    props: [],
    mounted() {
      axios
        .get('http://127.0.0.1:8000/items')
        .then(response => (this.items = response))
        .catch(err => {
          console.log(err); 
        })
    },
    data() {
      return {
        items: null
      }
    },
    methods: {

    },
    computed: {

    }
}
</script>

<style scoped>
  .items {

  }
</style>
