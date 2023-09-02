<template>
    <Teleport to="#app">

        <div class="modal-backdrop">
            <div class="modal fade-in-element">
                <div class="close-btn icon-btn" @click="$emit('close')">
                    <i class="fas fa-times"></i>
                </div>
                <div class="modal-header">
                    <slot name="header"></slot>
                </div>
                <div class="modal-body">
                    <slot name="body"></slot>
                </div>
                <div class="modal-footer">
                    <slot name="footer"></slot>
                </div>
            </div>
        </div>
    </Teleport>
</template>
<script>
export default{
    name: "BaseModal"
}
</script>
<style lang="scss">
@import "@/styles/modal.scss";
</style>