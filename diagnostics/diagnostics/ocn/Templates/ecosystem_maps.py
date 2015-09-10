<h3>{{ title }}</h3>

<table class="plot">
<th colspan="{{ cols }}">{{ plot_title_s1 }}</th>
{% for r in rowList %}
    <tr>
    {% for c in colList  %}
        {% set label, image = plot_table_s1_t1[r:c] %}
        {% if 'Error' in label %}
           <td>{{ label }}</td>
        {% elif label == '' %}
           <td></td>
        {% else %}
           <td><a href="{{ image }}">{{ label }}</td>
        {% endif %}
    {% endfor %}
    </tr>
{% endfor %}
</table>

<p/>
<table class="plot">
    <tr>
    {% for c in colList  %}
    {% set label, image = plot_table_s1_t2[c] %}
        {% if 'Error' in label %}
           <td>{{ label }}</td>
        {% elif label == '' %}
           <td></td>
        {% else %}
           <td><a href="{{ image }}">{{ label }}</td>
        {% endif %}
    {% endfor %}
    </tr>
</table>

<p/>
<table class="plot">
    <tr>
    {% for c in colList  %}
    {% set label, image = plot_table_s1_t3[c] %}
        {% if 'Error' in label %}
           <td>{{ label }}</td>
        {% elif label == '' %}
           <td></td>
        {% else %}
           <td><a href="{{ image }}">{{ label }}</td>
        {% endif %}
    {% endfor %}
    </tr>
</table>

<p/>
<table class="plot">
<th colspan="{{ cols }}">{{ plot_title_s2 }}</th>
{% for i in range(num_rows_s2) %}
    <tr>
    {% for order, label, plot in plot_table_s2[i] %}
       {% if order == 0 %}
          <td><b>{{ plot }}</b></td>	
       {% elif 'Error' in plot %}
          <td>{{ plot }}</td>	
       {% else %}
       	  <td><a href="{{ plot }}">{{ label }}</a></td>
       {% endif %}
    {% endfor %}
    </tr>
{% endfor %}


</table>

<hr>