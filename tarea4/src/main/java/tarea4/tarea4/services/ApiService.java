package tarea4.tarea4.services;


import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;
import org.springframework.stereotype.Service;

import tarea4.tarea4.models.Avistamientos;
import tarea4.tarea4.models.AvistamientosRepository;

@Service
public class ApiService {
    
    private final AvistamientosRepository avistamientosRepository;
    public ApiService(AvistamientosRepository avistamientosRepository) {
        this.avistamientosRepository = avistamientosRepository;
    }

    /*public List<Avistamientos> getAvistamientos(String titleSubString) {
        List<Avistamientos> avistamientos = avistamientosRepository.findAll();
        List<Avistamientos> matchAvistamientos = new ArrayList<Avistamientos>();
        for (Avistamientos conf : avistamientos) {
            if (conf.getNombre().toLowerCase().contains(titleSubString.toLowerCase())) {
                matchAvistamientos.add(conf);
            }
        }
        return matchAvistamientos;
    }*/
    public List<Avistamientos> getAvistamientos(String titleSubString) {

    List<Avistamientos> avistamientos =
            avistamientosRepository.findAll();

    List<Avistamientos> matchAvistamientos =
            new ArrayList<>();

    for (Avistamientos avis : avistamientos) {

        if (avis.getNombre().toLowerCase().contains(titleSubString.toLowerCase())
                || avis.getAve().toLowerCase().contains(titleSubString.toLowerCase())
                || avis.getComuna().toLowerCase().contains(titleSubString.toLowerCase())) {

            matchAvistamientos.add(avis);
        }
    }

    return matchAvistamientos;
}
}
