package financiamento;

import java.io.Serializable;

public class Apartamento extends Financiamento implements Serializable {

    private double taxaMensalAp;
    private double prazoMeses;
    private int numeroAndar;
    private int numeroVagasGaragem;

    public Apartamento(double valorImovel, int prazoFinanciamento, double taxaJurosAnual, int numeroAndar, int numeroVagasGaragem) {
        super(valorImovel, prazoFinanciamento, taxaJurosAnual);
        this.taxaMensalAp = (this.getTaxaJurosAnual() / 12) / 100;
        this.prazoMeses = this.getPrazoFinanciamento() * 12;
        this.numeroAndar = numeroAndar;
        this.numeroVagasGaragem = numeroVagasGaragem;
    }

    @Override
    public double calcular_valor_mensal(){
        double valorParcela = ((this.getValorImovel() * taxaMensalAp) * (Math.pow((1 + taxaMensalAp), (prazoMeses))))
                / (Math.pow((1+taxaMensalAp), prazoMeses)-1);
        return valorParcela;
    }

    public int getNumeroVagasGaragem() {
        return numeroVagasGaragem;
    }

    public void setNumeroVagasGaragem(int numeroVagasGaragem) {
        this.numeroVagasGaragem = numeroVagasGaragem;
    }

    public int getNumeroAndar() {
        return numeroAndar;
    }

    public void setNumeroAndar(int numeroAndar) {
        this.numeroAndar = numeroAndar;
    }

    @Override
    public String imprimir_dados_financiamento() {
        String output = "";
        output += "Valor do imóvel: " + this.getValorImovel() + "\n";
        output += "Valor total do financiamento: " + this.calcular_total_pagamento() + "\n";
        output += "Valor da parcela mensal: " + this.calcular_valor_mensal() + "\n";
        output += "Andar do apartamento: " + this.numeroAndar + "\n";
        output += "Número de vagas na garagem: " + this.numeroVagasGaragem + "\n";
        output += "-------------------------\n";
        return output;
    }
}
