package tarea4.tarea4.models;

import java.time.LocalDateTime;

import org.springframework.web.multipart.MultipartFile;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.SequenceGenerator;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotNull;

@Entity
@Table
public class Avistamientos {

    @Id
    @SequenceGenerator(
        name = "confession_sequence",
        sequenceName = "confession_sequence",
        allocationSize = 1
    )
    @GeneratedValue(
        strategy = GenerationType.SEQUENCE,
        generator = "confession_sequence"
    )
    private Long id;

    @NotNull
    private String nombre;

    @NotNull
    private LocalDateTime dia;
    
    @NotNull
    private String ave;
    
    @NotNull
    private String comuna;

    public Avistamientos() {
    }

    public Avistamientos(String nombre, 
                    LocalDateTime dia,
                    String ave,
                    String comuna
                    ) {

        this.nombre = nombre;
        this.dia = dia;
        this.ave = ave;
        this.comuna = comuna;
        
    }

    public Long getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public LocalDateTime getDia() {
        return dia;
    }

    public String getAve() {
        return ave;
    }

    public String getComuna() {
        return comuna;
    }

    public static Boolean validateConfession(String confText) {
        // Ejercicio: implementar validacion de confesiones :)
        return true;
    }
}
