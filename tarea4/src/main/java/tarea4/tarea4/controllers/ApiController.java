package tarea4.tarea4.controllers;


import org.springframework.web.bind.annotation.RestController;

import tarea4.tarea4.models.Avistamientos;

import tarea4.tarea4.services.ApiService;
import java.util.List;
import java.util.Map;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;



@RestController
public class ApiController {
    private final ApiService apiService;
    public ApiController(ApiService apiService) {
        this.apiService = apiService;

    }

    @GetMapping("/get-avis/{title_substring}")
    public Map<String, List<Avistamientos>> getConfessionEndpoint(@PathVariable("title_substring") String titleSubstring) {
        List<Avistamientos> avistamientos = apiService.getAvistamientos(titleSubstring);
        return Map.of("data", avistamientos); // Encapsula la lista en un mapa con clave "data"
    }

   
}
