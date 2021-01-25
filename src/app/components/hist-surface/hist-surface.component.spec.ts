import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HistSurfaceComponent } from './hist-surface.component';

describe('HistSurfaceComponent', () => {
  let component: HistSurfaceComponent;
  let fixture: ComponentFixture<HistSurfaceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HistSurfaceComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HistSurfaceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
