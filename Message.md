Method 1 - No JS

<!-- Messages from backend Metho 1 No JS -->

{% for message in messages %}

<div class="d-flex justify-content-between align-items-center mt-4 alert alert-primary alert-dismiable fade show ext-center {{message.tags}}" role=""alert>
    {{message}}
    <button type="button" style="font-size: 10px;" class="btn-close" data-bs-dismis="alert" aria-label="Close"></button>
</div>
{% endfor %}
