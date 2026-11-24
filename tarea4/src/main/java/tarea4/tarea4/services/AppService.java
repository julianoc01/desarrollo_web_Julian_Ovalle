package tarea4.tarea4.services;


import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.security.MessageDigest;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Formatter;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;
import org.springframework.util.ResourceUtils;
import org.springframework.web.multipart.MultipartFile;

import tarea4.tarea4.models.Avistamientos;
import tarea4.tarea4.models.AvistamientosRepository;


@Service
public class AppService {

    private final String pathStatic;
    private final AvistamientosRepository avistamientosRepository;

    public AppService(AvistamientosRepository avistamientosRepository) throws IOException {
        this.avistamientosRepository = avistamientosRepository;
        // Dynamically resolve the absolute path for the static directory
        Path staticDir = Paths.get(ResourceUtils.getFile("classpath:static").getAbsolutePath());
        this.pathStatic = staticDir.toString();
        System.out.println("Static path resolved to: " + this.pathStatic);
    }

    public List<Map<String, String>> getAvistamientosData(Integer pageSize) {
        List<Avistamientos> Avistamientos = avistamientosRepository.findAllByOrderByIdDesc(PageRequest.of(0, pageSize)).getContent();
        List<Map<String, String>> AvistamientosData = new ArrayList<>();
        
        for (Avistamientos conf : Avistamientos) {
            Map<String, String> avisData = new HashMap<>();
            avisData.put("id", conf.getId().toString());
            avisData.put("nombre", conf.getNombre());
            avisData.put("dia", conf.getDia().toString());
            avisData.put("ave", conf.getAve());
            avisData.put("comuna", conf.getComuna());

            
            //confData.put("image_filename", conf.getImg());

            AvistamientosData.add(avisData);
        }
        return AvistamientosData;


    }


    public void handlePostRequest(
        String nombre,
        LocalDateTime dia,
        String ave,
        String comuna) throws Exception {

       

        if (Avistamientos.validateConfession(nombre)) {
            

            // Save the confession in the database
            Avistamientos Avistamiento = new Avistamientos(
                nombre,
                dia,
                ave,
                comuna
            );
            avistamientosRepository.save(Avistamiento);
            System.out.println("Avistamiento saved successfully.");
        } else {
            throw new IllegalArgumentException("Avistamiento validation failed.");
        }
    }
}
